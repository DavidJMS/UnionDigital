# From Django
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic as views_generic 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest

# My Forms
from .forms import SignupForm, EmployeeLogin, ChangePasswordForm
from django import forms
# My Models
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
    
    # Method to get a pk object
    def get_object(self):
        
        return self.request.user.employeeprofile

    # Method to redirect success url pass a slug param
    def get_success_url(self):
        username = self.object.user.username
        return reverse('accounts:detail', kwargs={'username':username})

"""def ChangePassword(request):
    
        Def with a method to change password of users.
        receives the user's old password to authenticate the password change using a form
    
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            username = request.user.username
            password = request.method.POST['password_old']
            user = authenticate(request,user=username, password=password)
            if user is not None:
                password_new = form.cleaned_data['password_new']
                user = User.objects.get(username=username)
                user.set_password(password_new)
            else:
                return render(request, 'accounts/password_change.html', {'error':'Clave de usuario incorrecta. Intente nuevamente'})
    else:
        form = ChangePasswordForm()
    return render(request, 'accounts/password_change.html')"""

class ChangePasswordViewSet(LoginRequiredMixin, SuccessMessageMixin, views_generic.FormView):

    template_name = 'accounts/password_change.html'
    form_class = ChangePasswordForm
    success_url = 'accounts:detail'
    success_message = 'Cambio de contraseña realizado correctamente'

    def form_valid(self, form):
        username = self.request.user.username
        password = form.cleaned_data['password_old']
        print(password,username)
        print(form.cleaned_data)
        user = authenticate(self.request,username=username, password=password)
        if user is not None:
            password_new = form.cleaned_data['password_new']
            print(password_new)
            user = User.objects.get(username=username)
            user.set_password(password_new)
            user.save()
            update_session_auth_hash(self.request, user)
            return super().form_valid(form)
        else:
            return render(self.request, 'accounts/password_change.html', {'error':'Clave de usuario incorrecta. Intente nuevamente'})
        