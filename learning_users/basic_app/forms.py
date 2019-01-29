from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

#Form.py is a collection of elements inside <form>...</form> in the HTML.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
