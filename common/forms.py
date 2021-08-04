from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    phone = forms.CharField(label="전화번호")
    address = forms.CharField(label="주소")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "last_name", "phone", "address")