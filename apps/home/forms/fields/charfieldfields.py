from django import forms
from django.core.exceptions import ValidationError


# baseclass for Charfields. subclassed from django default CharField
class CustomcharField(forms.CharField):
    pass

# subclass a CharField field to be used in LoginForm
class LoginusernameField(CustomcharField):
    pass


# subclass a CharField field to be used in LoginForm
class LoginpasswordField(CustomcharField):
    pass



class RegisterusernameField(CustomcharField):

    # override init method to add new class attributes
    def __init__(self, min_length=None, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length

    # define custom validation logic
    def validate(self, value):
        super().validate(value)

        # check if input is alphanumeric
        if not value.isalnum():
            raise ValidationError(
                ("Invalid value: %(value)s"),
                code="invalid",
                params={"value": "42"},
            )

        # check if input is over minlength
        if self.min_length is not None and len(value) < self.min_length:
            raise ValidationError(f"This field must be at least {self.min_length} characters long.")

        # check if input is under maxlength
        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(f"This field must be at least {self.max_length} characters long.")

class RegisterpasswordField(CustomcharField):
    pass

class Registerpassword2Field(CustomcharField):
    pass