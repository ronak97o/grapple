from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class" : "form-control",
               "id" :"form_user_name",
               "placeholder" : "User Name"}))
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={"class" : "form-control",
               "id" :"form_full_name",
               "placeholder" : "Full Name"}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"class" : "form-control",
               "id" :"form_email",
               "placeholder" : "email"}))
    mobile = forms.CharField(widget=forms.TextInput(
        attrs={"class" : "form-control",
               "id" :"form_mobile_nuber",
               "placeholder" : "Mobile Number"}))
