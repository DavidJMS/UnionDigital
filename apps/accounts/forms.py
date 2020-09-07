# utilities
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
# models
from .models import EmployeeProfile
from django.contrib.auth.models import User

class EmployeeLogin(AuthenticationForm):

    username = forms.CharField(
        min_length=4, 
        max_length=50,
        error_messages={
            'required': 'Este campo es requerido',
            'min_length': 'Introduzca al menos 4 caracteres',
            'max_length': 'El límite de caracteres es de 50'
            }
        )
    
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Este campo es requerido',
            'min_length': 'Introduzca al menoss 4 caracteres'
            }
        )
    
    def cleaned_password(self):
        password = self.cleaned_data.get('password')
        print('Entro en cleaned')
        if (len(password) <4):
            print('El raise deberia de funcionar')
            raise ValueError('El mínimo son 4 caracteres')

class SignupForm(forms.Form):

    username = forms.CharField(
        min_length=4, 
        max_length=50,
        error_messages={
            'required': 'Este campo es requerido',
            'min_length': 'Introduzca al menos 4 caracteres',
            'max_length': 'El límite de caracteres es de 50'
            }
        )
    password = forms.CharField(
        min_length=4,
        max_length= 50,
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Este campo es requerido',
            'min_length': 'Introduzca al menos 4 caracteres',
            'max_length': 'El límite de caracteres es de 50',
            }
        )
    password_confirmation = forms.CharField(
        min_length= 4,
        max_length= 50,
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Este campo es requerido',
            'min_length': 'Introduzca al menos 4 caracteres',
            'max_length': 'El límite de caracteres es de 50',
            }
        )
    first_name = forms.CharField(
        min_length=2, 
        max_length=50,
        error_messages={
            'required': 'Este campo es requerido',
            'min_length': 'Introduzca al menos 2 caracteres',
            'max_length': 'El límite de caracteres es de 50'
            })
    last_name = forms.CharField(
        min_length=2, 
        max_length=50,
        error_messages={
            'required': 'Este campo es requerido',
            'min_length': 'Introduzca al menos 2 caracteres',
            'max_length': 'El límite de caracteres es de 50'
            })
    email = forms.CharField(
        min_length=6,
        max_length=70,
        error_messages={
            'required': 'Este campo es requerido',
            'min_length': 'Introduzca al menos 6 caracteres',
            'max_length': 'El límite de caracteres es de 50'
            })
    
    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Usuario ya es uso')
        return username

    def clean(self):
        data = super().clean()
        print(super().clean())
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')
        if not password_confirmation:
            raise forms.ValidationError('Este campo es requerido')
        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')
        data.pop('password_confirmation')
        # Make a password with a real algorit equal at hash password
        data['password'] = make_password(password)
        return data
    
    def save(self):
        data = self.cleaned_data
        user = User.objects.create(**data)
        profile = EmployeeProfile(user=user)
        profile.save()
        