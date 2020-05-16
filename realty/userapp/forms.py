from django.contrib.auth.forms import UserCreationForm
from .models import ApartmentUser

class RegistrationForm(UserCreationForm):

    class Meta:
        model = ApartmentUser
        fields = ('username', 'password1', 'password2', 'email')