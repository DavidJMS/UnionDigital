# From Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views_generic 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest

# Forms
from .forms import SignupForm, EmployeeLogin
from django import forms
# Models
from .models import EmployeeProfile

# Views
class LoginView(LoginView, SuccessMessageMixin):
    """
        View for login users
    """
    template_name = 'accounts/login.html'
    form_class = EmployeeLogin
    success_message = 'Bienvenido %(username)s'

class LogoutView(LogoutView):
    """
        View for login users
    """
    template_name = 'accounts/login.html'

class SignupView(SuccessMessageMixin, views_generic.FormView):
    """
        View for sign up users, only persons of company can sign up
    """
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')
    success_message = "%(username)s Regitrado exitosamente"

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class DetailView(LoginRequiredMixin, views_generic.detail.DetailView):
    """
        View for see details of users.
        Details in Profile and User Model.
    """
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    template_name = 'accounts/detail.html'
    context_object_name = 'user'

class ProfileUpdateView(LoginRequiredMixin, views_generic.edit.UpdateView):
    """
        View for update a profile of user in system.
    """
    model = EmployeeProfile
    fields = ['position','biography','website','picture','phone_number']
    template_name = 'accounts/update_profile.html'

    def get_object(self):
        # Method to get a pk object
        return self.request.user.employeeprofile

    # Falta el metodo para succes url...