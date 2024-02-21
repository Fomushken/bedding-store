from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name='Date of birth')
