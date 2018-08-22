from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"type":"text",
               "class" :"username",
               "id":"username",
               "name":"username",
               "placeholder":"Username..."}))
    firstname = forms.CharField(widget=forms.TextInput(
        attrs={"type":"text",
               "class": "firstname",
               "id":"firstname",
               "name":"firstname",
               "placeholder":"enter your firstname ..."}))
    lastname = forms.CharField(widget=forms.TextInput(
        attrs={"type": "text",
               "class": "lastname",
               "id": "lastname",
               "name": "lastname",
               "placeholder": "enter your lastname.."}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"type":"text",
               "class": "email",
               "id":"email",
               "name":"email",
               "placeholder":"Email..."}))
    mobile = forms.CharField(widget=forms.TextInput(
        attrs={"type":"text",
               "id":"mobilenumber",
               "class": "mobile",
               "name":"mobilenumber",
               "placeholder":"Mobilenumber..."}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ "type":"password",
                                                                  "class": "password",
                                                                  "id":"password",
                                                                  "name":"password",
                                                                  "placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ "type":"password",
                                                                   "class": "password2",
                                                                  "id":"password2",
                                                                  "name":"password2",
                                                                  "placeholder":"Confirm  Password..."}))

    def clean_username(self):
        username =self.cleaned_data.get("username")
        qs = User.objects.filter(username= username)
        if qs.exists():
            raise forms.ValidationError("username exists try new one")
        return  username

    def clean_email(self):
        email =self.cleaned_data.get("email")
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("email is taken try new one")
        return  email


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("passwords must match")
        return data