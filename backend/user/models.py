from typing import List
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from uuid import uuid4
import logging


class User(AbstractUser):

    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = []

    class Meta:
        ordering = ('email',)

    def get_full_name(self) -> str:
        return super().get_full_name()

    def get_short_name(self) -> str:
        return super().get_short_name()

    def get_username(self) -> str:
        return f"{self.email}"

    def __str__(self):
        return f"{self.email}"


class Profile(models.Model):

    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
