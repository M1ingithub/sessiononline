from django import forms


class AddCommunityForm(forms.Form):
    url = forms.CharField(max_length=200, label="", widget=forms.TextInput(attrs={'class': 'community_url_field'}))

