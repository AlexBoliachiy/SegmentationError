from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    about_me = models.TextField()
    love_lang = models.TextField()
    user = models.OneToOneField(User)


