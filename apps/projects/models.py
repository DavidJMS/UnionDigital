from django.db import models

# Create your models here.
class WorkProposals(models.Model):

    """Proposals of our customer"""
    
    title = models.CharField(max_length=50)
    detail = models.TextField()
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=50, blank=True) 
    budget = models.CharField(max_length=50, blank= True) 
    quotation = models.FileField(upload_to='process/documents',null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    finish_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name: 'Propustas'
        verbose_name_plural: 'Propuestas'
        ordering: ['-crated']

    def __str__(self):
        return self.title