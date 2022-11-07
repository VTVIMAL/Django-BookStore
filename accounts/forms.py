from django.contrib.auth import get_user_model # used to import CustomUser, looks for AUTH_USER_MODEL in setting.py
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# from .models import CustomUser # we do not need this line because we imported the get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ( "email", "username")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ( "email", "username" )