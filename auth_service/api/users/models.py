from django.contrib.auth.validators import UnicodeUsernameValidator
import uuid
from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager["CustomUser"]):

    use_in_migrations = True

    def create_user(self, email, password, username, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.is_active = False
        user.password = make_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password=None, **kwargs):
        user = self.model(email=email, username=username, password=password)

        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save()

        return user


class CustomUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(_("username"), max_length=150, unique=True, validators=[UnicodeUsernameValidator()])

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
