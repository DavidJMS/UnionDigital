# From Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views_generic 
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# Forms
from .forms import SignupForm

# Models
from .models import EmployeeProfile

# Views
class LoginView(LoginView):
    """
        View for login users
    """
    template_name = 'accounts/login.html'

class SignupView(views_generic.FormView):
    """
        View for sign up users, only persons of company can sign up
    """
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin, views_generic.edit.UpdateView):
    """
        View for update a profile of user in system
    """
    model = EmployeeProfile
    fields = ['position','biography','website','picture','phone_number']
    template_name = 'accounts/update_profile.html'

    def get_object(self):
        # Method to get a pk object
        return self.request.user.employeeprofile
