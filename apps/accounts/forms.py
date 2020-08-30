from django import forms
# models
from .models import EmployeeProfile
from django.contrib.auth.models import User

class SignupForm(forms.Form):

    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(min_length=4,max_length=70,)
    password_confirmation = forms.CharField(min_length=4,max_length=70)
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.CharField(min_length=6,max_length=70)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        data = super().clean()
        password = data['password']
        print(data)
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')
        data.pop('password_confirmation')
        return data
    
    def save(self):
        data = self.cleaned_data
        user = User.objects.create(**data)
        profile = EmployeeProfile(user=user)
        profile.save()
        