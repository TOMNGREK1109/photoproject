from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUSerCreationForm(UserCreationForm):
    model = CustomUser

    fields = ('username', 'email', 'password1', 'password2')