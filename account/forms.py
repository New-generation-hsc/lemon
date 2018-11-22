from django import forms
from django.contrib.auth.models import User

class AccountForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    confirm = forms.CharField(required=True)

    def clean_username(self):
        name = self.cleaned_data['username'].strip()
        if User.objects.filter(username=name).exists():
            raise forms.ValidationError("username already exists")
        return name

    def clean(self):
        data = super().clean()
        if data['password'] != data['confirm']:
            raise forms.ValidationError("password doesn't match")
        return data