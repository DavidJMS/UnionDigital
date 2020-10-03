from django.urls import path
from . import views
urlpatterns = [
    path(route ='project/list/', view = views.ListProjects.as_view(), name ='list_project'),
    path(route ='project/new/', view = views.CreateProject.as_view(), name ='create_project'),
    path(route ='project/detail/<int:id>/', view = views.DetailProjectView.as_view(), name ='detail_project'),
]