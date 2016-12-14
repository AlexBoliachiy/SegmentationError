from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .account_manager import UserManager


class Account(AbstractBaseUser):
    about_me = models.TextField()
    love_lang = models.TextField()
    objects = UserManager()


