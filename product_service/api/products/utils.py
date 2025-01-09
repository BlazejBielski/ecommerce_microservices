from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OwnerModel(models.Model):
    user_id = models.UUIDField(help_text="User id from auth service")

    class Meta:
        abstract = True
