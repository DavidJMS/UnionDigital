# From Django
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView

# Forms
from .forms import SignupForm
# Models


# Views

class LoginView(LoginView):

    template_name = 'accounts/login.html'

class SignupView(FormView):

    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = 'accounts:login'

    def form_valid(self, **kwargs):
        
        form.save()
        return self.form_valid(form)
