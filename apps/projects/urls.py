from django.urls import path
from . import views
urlpatterns = [
    path(route ='proosal/list/', view = views.ListProposal.as_view(), name='list_proposal'),
    path(route ='proposal/new/', view = views.CreateProposal.as_view(), name ='create_proposal'),
]