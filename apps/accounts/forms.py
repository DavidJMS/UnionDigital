from django import forms
# models
from .models import EmployeeProfile
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):

    class Meta:

        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exits()
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        data = super().clean()
        password = data['password']
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
        