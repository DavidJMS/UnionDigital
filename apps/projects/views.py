# From Django
from django.shortcuts import render
from django.views import generic as views_generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse

# My Forms
from .forms import CreateProjectForm

# My Models
from .models import Project

class CreateProject(SuccessMessageMixin, views_generic.FormView):
    """
        Method to create Project of customer
        Allow anonymus user
    """
    form_class = CreateProjectForm
    template_name = 'projects/create_project.html'
    success_url = reverse_lazy('projects:create_project')
    success_message = 'Propuesta "%(title)s" Regitrada Exitosamente'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class ListProjects(LoginRequiredMixin, views_generic.ListView):
    """
        View to see list of Project for employess
    """
    model = Project
    #ordering = ('-created')
    paginate_by = 6
    context_object_name = 'projects'
    template_name = 'projects/list_projects.html'
    

    def get_queryset(self):
        """
            With this function we filter project by user and status, this return a object iterable,
            if we use queryset function, that will return a queryset
        """
        user = self.request.user
        projects = Project.objects.filter(employess=user,status='En Desarrollo').order_by('-created')
        return projects

class DetailProjectView(LoginRequiredMixin, views_generic.detail.DetailView):
    """
        View to see details about a project for employees
    """
    slug_url_kwarg = 'id'
    slug_field = 'id'
    queryset = Project.objects.all()
    context_object_name = 'project'
    template_name = 'projects/detail.html'