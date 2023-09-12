from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom User Model Manager where email is the unique indetifier
    for authentication instead of the username
    """

    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))

        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        user = self.create_user(username, email, password=password, **extra_fields)

        user.is_staff = True
        user.save()
        return user
