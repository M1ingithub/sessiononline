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
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser
    is_vendor
    last_login
    date_joined = models.DateTimeField(default=timezone.now)
    pgppubkey
    language
    theme
    maincurrency
    feedbacks
    products
    receivedorders
    openedorders
    masterwallet

    # Set the USERNAME_FIELD -- which defines the unique identifier for the User model -- to username
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
