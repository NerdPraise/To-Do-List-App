from django import forms
from listapp.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input--style-3'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input--style-3'}))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'class': 'input--style-3'}))
    password2 = forms.CharField(label=_("Password Again"), widget=forms.PasswordInput(attrs={'class': 'input--style-3'}))

    pass

    class Meta:
        model = User
        fields = ("username","email", "password1", "password2",)