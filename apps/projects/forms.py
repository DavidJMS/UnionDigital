# from Django
from django.forms import ModelForm

# my models
from .models import WorkProposals
class CreateProposalForm(ModelForm):

    class Meta:
        model = WorkProposals
        fields = [
            'title',
            'detail',
            'customer_name',
            'customer_phone',
            'budget',
            'start_date',
            'finish_date'
        ]
        exclude = [
            'created',
            'modified',
            'quotation'
        ]
        


