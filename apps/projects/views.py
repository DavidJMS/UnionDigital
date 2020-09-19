# From Django
from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse

# My Forms
from .forms import CreateProposalForm

# My Models
from .models import WorkProposals

class CreateProposal(SuccessMessageMixin, FormView):
    """
        Method to create proposal of customer
        Allow anonymus user
    """
    form_class = CreateProposalForm
    template_name = 'projects/create_proposal.html'
    success_url = reverse_lazy('projects:create_proposal')
    success_message = 'Propuesta "%(title)s" Regitrada Exitosamente'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class ListProposal(LoginRequiredMixin, ListView):
    """
        Method to view a list of proposal for employess
    """
    model = WorkProposals
    ordering = ('-created')
    paginate_by = 10
    context_object_name = 'proposals'
    template_name = 'projects/list_proposal.html'
    