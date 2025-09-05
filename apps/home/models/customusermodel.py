""""
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.home.models.customusermanager import CustomUserManager


class CustomUserModel(AbstractBaseUser):

    username
    password
    groups
    user_permissions
    is_superuser
    is_vendor
    last_login

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # Set the USERNAME_FIELD -- which defines the unique identifier for the User model -- to username
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
"""