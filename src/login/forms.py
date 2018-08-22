from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "type": "text", "name":"email", "placeholder":"Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"input100", "type":"password", "name":"pass", "placeholder":"Password"}))