from django.urls import path
from . import views
urlpatterns = [
    path(route ='login/', view = views.LoginView.as_view(), name ='login'),
    path(route ='logout/', view = views.LogoutView.as_view(), name ='logout'),
    path(route ='signup/', view = views.SignupView.as_view(), name ='signup'),
    path(route ='detail/<str:username>/', view = views.DetailView.as_view(), name ='detail'),
    path(route ='profile/update/', view = views.ProfileUpdateView.as_view(), name ='update_profile'),
    path(route ='password/change/', view = views.ChangePasswordViewSet.as_view(), name ='password_change'),
]