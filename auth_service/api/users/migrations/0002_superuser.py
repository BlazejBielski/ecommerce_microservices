import os

from django.db import migrations


def create_superuser(apps, schema_editor):
    User = apps.get_model("users", "CustomUser")

    DJ_SU_NAME = os.environ.get("DJ_SU_NAME")
    DJ_SU_PASSWORD = os.environ.get("DJ_SU_PASSWORD")
    DJ_SU_EMAIL = os.environ.get("DJ_SU_EMAIL")

    User.objects.create_superuser(
        username=DJ_SU_NAME,
        email=DJ_SU_EMAIL,
        password=DJ_SU_PASSWORD,
    )
    User.is_active = True


def delete_superuser(apps, schema_editor):
    User = apps.get_model("users", "CustomUser")
    DJ_SU_EMAIL = os.environ.get("DJ_SU_EMAIL")

    admin = User.objects.get(email=DJ_SU_EMAIL)
    if admin.is_superuser:
        admin.delete()
    else:
        raise IndexError("User with id = 1 is not an admin")


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]
    operations = [
        migrations.RunPython(create_superuser, delete_superuser),
    ]
