# from Django
from django.forms import ModelForm

# my models
from .models import Project
class CreateProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = [
            'title',
            'detail',
            'customer_name',
            'customer_phone',
            'customer_email',
        ]
        exclude = [
            'created',
            'modified',
            'quotation',
            'status',
            'employess',
            'requeriments'
        ]
        


