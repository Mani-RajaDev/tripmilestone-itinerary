from django.forms import EmailField, CharField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from . import models


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form excluded "Password Confirmation Field"
    """

    email = EmailField(label="Email address")
    username = CharField(label="Username")

    class Meta:
        model = models.CustomUser
        fields = ["email", "username", "password1"]
        help_texts = {
            "password1": None,
        }


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["password1"].help_text = None

        del self.fields["password2"]


    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get("password1")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password1", error)
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        return username
    

class CustomUserChangeForm(UserChangeForm):
    """
    Custom user change form nothing fancy just based on custom user model
    """

    class Meta:
        model = models.CustomUser
        fields = ["email", "username"]
