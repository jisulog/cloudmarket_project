from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    names = forms.CharField(label="유저이름")
    phone = forms.CharField(label="전화번호")
    address = forms.CharField(label="주소")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "names", "phone", "address")