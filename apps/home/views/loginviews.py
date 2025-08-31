from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.home.forms.forms.loginform import LoginForm, SignUpForm
from django.views import View


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def post(self, request):
        logout(request)
        return render(request, 'accounts/logout.html')

class LoginView(View):
    def post(self, request):
        form = LoginForm(request.POST or None)

        msg = None
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'

        # move to registration
        elif form.is_valid() == False:
            msg = form.errors
            if 'username' in form.errors:
                for e in form.errors['username']:
                    print(e)

        return render(request, "accounts/login.html", {"form": form, "msg": msg})

    def get(self, request):
        form = LoginForm(request.GET or None)
        return render(request, "accounts/login.html", {"form": form})

class RegisterView(View):
    def post(self, request):
        msg = None
        success = False
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
        return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

    def get(self, request):
        form = SignUpForm()
        return render(request, "accounts/register.html", {"form": form})