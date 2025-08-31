from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.home.forms.fields import LoginusernameField
from apps.home.forms.fields import LoginpasswordField
from apps.home.forms.widgets import LoginusernameinputWidget
from apps.home.forms.widgets import LoginpasswordinputWidget


# subclass a form and use custom field and widget classes instead of defaults
class LoginForm(forms.Form):

    # override init method to override attribute names so they can be customized with css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "loginusernamewidget"})
        self.fields["password"].widget.attrs.update({"class": "loginpasswordwidget"})

    username = LoginusernameField(
        min_length=4,
        max_length=20,
        widget = LoginusernameinputWidget(
            attrs = {
                "placeholder": "Username",
                "class": "form-control"
            }
        )
    )
    password = LoginpasswordField(
        widget = LoginpasswordinputWidget(
            attrs = {
                "placeholder": "Password",
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):

    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Username",
                "class": "form-control"
            }
        ))

    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
        
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
