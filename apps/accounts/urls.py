from django.urls import path
from . import views
urlpatterns = [
    path(route ='login/', view = views.LoginView.as_view(), name  ='login'),
    path(route ='signup/', view = views.SignupView.as_view(), name  ='signup'),
]