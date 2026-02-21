from django import template
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.home.forms.forms.addcommunityform import AddCommunityForm
from apps.home.models.communitymodel import CommunityModel
from django.contrib.auth.models import User
import django_tables2 as tables
from django_tables2 import SingleTableView
from apps.home.table.table import CommunityTable
import requests
import json
from datetime import datetime


class CommunityListView(SingleTableView):
    model = CommunityModel
    table_class = CommunityTable
    template_name = 'home/table.html'
    # update database in terms of changed users, name and description every time the page is loaded
    # also delete dublicate entries
    def databaseupdate():
        communities = CommunityModel.objects.all()
        for community in communities:
            r = requests.get(community.url+'rooms')
            rjson = r.json()
            # update rooms' data via url
            def search(rjson2, roomtoken2):
                for k in rjson2:
                    for a in k:
                        if k[a] == roomtoken2:
                            return k
            therightroomdict = search(rjson, community.token)
            community.active_users = therightroomdict['active_users']
            community.description = therightroomdict['description']
            community.name = therightroomdict['name']
            community.save()
            # delete dublicates
            count = 0
            for community2 in communities:
                asd = community2.custom_id
                if community2.name == community.name and community2.token == community.token and community2.url == community.url:
                    count = count + 1
                if count >= 2:
                    CommunityModel.objects.get(custom_id=asd).delete()
    databaseupdate()


class ReportView(View):
    def get(self, request):
        context = {} # Turha paska, mutta ei renderaa ilman context muuttujaa
        html_template = loader.get_template('home/report.html')
        return HttpResponse(html_template.render(context, request))
    
class AboutView(View):
    def get(self, request):
        context = {} # Turha paska, mutta ei renderaa ilman context muuttujaa
        html_template = loader.get_template('home/about.html')
        return HttpResponse(html_template.render(context, request))

@method_decorator(login_required, name='dispatch')
class AddCommunityView(ListView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = '/login/'
    def post(self, request):
        context = {}
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = AddCommunityForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                cd = form.cleaned_data
                # extract url from community url
                communityurlstring = cd['url']
                substring = "/"
                occurance = 3
                val = -1
                for i in range(0, occurance): 
                    val = communityurlstring.find(substring, val + 1)
                url1 = communityurlstring[:val+1]
                # extract token from community url
                minusstring = communityurlstring.replace(url1, "")
                val2 = minusstring.find("?", 1)
                roomtoken1 = minusstring[:val2]
                # collect rooms' data via url
                r = requests.get(url1+'rooms')
                rjson = r.json()
                # find which one of the rooms was added by searching for token in the rooms dictionary inputted by user 
                def search(rjson2, roomtoken2):
                    for k in rjson2:
                        for a in k:
                            if k[a] == roomtoken2:
                                return k
                                # for g in b[roomtoken2]:  # for v in rjson2[k[a]]:    
                therightroomdict = search(rjson, roomtoken1)
                # create database entry for each room
                currentuser = request.user.username
                new_community = CommunityModel(
                    communityurl = cd['url'],
                    url = url1,
                    active_users = therightroomdict['active_users'],
                    description = therightroomdict['description'],
                    created = datetime.utcfromtimestamp(therightroomdict['created']).strftime('%Y-%m-%d %H:%M:%S'),
                    # created = datetime.fromtimestamp(tempcreated),
                    name = therightroomdict['name'],
                    token = therightroomdict['token'],
                    user = currentuser
                )
                new_community.save()
        return redirect(reverse('home'))
    def get(self, request):
        form = AddCommunityForm()
        context = {'form': form}
        return render(request, 'home/addcommunity.html', context)