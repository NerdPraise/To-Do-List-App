from django import forms
from listapp.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.core.files.images import get_image_dimensions

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input--style-3'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input--style-3'}))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'class': 'input--style-3'}))
    password2 = forms.CharField(label=_("Password Again"), widget=forms.PasswordInput(attrs={'class': 'input--style-3'}))
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ("username","email", "password1", "password2", "image")
    def clean_avatar(self):
        avatar = cleaned_data["image"]

        try:
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, GIF or PNG image.')
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(u'Avatar file size may not exceed 20k.')
        except AttributeError:
            pass
        return avatar


class UserSignForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder':'Password'}))