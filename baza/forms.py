from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField()
    txt=forms.CharField(max_length=100)
class ProfileForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
class ParolForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    parol=forms.CharField(max_length=100)
    parol_1=forms.CharField(max_length=100)