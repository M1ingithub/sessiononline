from django import forms
from django.template.loader import get_template

# baseclass for textinput widgets. subclassed from django default textinput widget
class CustomtextinputWidget(forms.TextInput):

    # use custom html template for the widget
    template_name = "components/widgets/customtextinputwidget.html"

# subclass a TextInput widget to be used in LoginForm
class LoginusernameinputWidget(CustomtextinputWidget):


    # define css source file for the widget
    # doesn't do shit. fix or go with index.scss added css for the widget which works
    class Media:
        css = {
            "all": ["/css/components/loginwidgets.css"],
        }

    # to customize the HTML output of your custom widget, use the get_context method to customize the widget’s context before rendering
    def get_context(self, name, value, attrs=None):
        context = super().get_context(name, value, attrs)
        return context


class LoginpasswordinputWidget(CustomtextinputWidget):

    # add a max_length parameter to the widget
    def __init__(self, max_length=None, *args, **kwargs):
        self.max_length = max_length
        super().__init__(*args, **kwargs)

    # define css source file for the widget
    # doesn't do shit. fix or go with index.scss added css for the widget which works
    class Media:
        css = {
            "all": ["/css/components/passwordwidgets.css"],
        }

    # to customize the HTML output of your custom widget, use the get_context method to customize the widget’s context before rendering
    def get_context(self, name, value, attrs=None):
        context = super().get_context(name, value, attrs)
        if self.max_length:
            context['max_length'] = self.max_length
        return context