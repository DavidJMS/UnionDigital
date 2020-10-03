from django.db import models

# Models from tohe app:
from django.contrib.auth.models import User
# Choices:

status_project=(
    ("Sin Cotizar","Sin cotizar"),
    ("Cotizado","Cotizado"),
    ("Cotización Aprobada","Cotización Aprobado"),
    ("Cotización Rechazada","Cotización Rechazada"),
    ("En Desarrollo","En Desarrollo"),
    ("En Revisión","En Revisión"),
    ("Terminado","Terminado"),
)

# Models:

class Project(models.Model):
    """
        Projects to develop for team unión digital
    """
    title           = models.CharField(max_length=50)
    detail          = models.TextField()
    customer_name   = models.CharField(max_length=50)
    customer_phone  = models.CharField(max_length=50, blank=True)
    customer_email  = models.EmailField(max_length=45, blank=True)
    quotation       = models.FileField(upload_to='process/documents',null=True, blank=True)
    status          = models.CharField(max_length=20, null=True, choices=status_project)
    employess       = models.ManyToManyField(User, blank=True)
    requeriments    = models.FileField(upload_to='process/documents',null=True, blank=True)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name: 'Proyecto'
        verbose_name_plural: 'Proyectos'
        ordering: ['-created']

    def __str__(self):
        return self.title

class ChatProject(models.Model):
    name            = models.OneToOneField(Project, on_delete=models.CASCADE)
    created         = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name: 'Sala De Chat'
        verbose_name_plural: 'Salas De Chat'
        ordering: ['-created']

    def __str__(self):
        return self.name.title


class Message(models.Model):
    sala            = models.ForeignKey(ChatProject, on_delete=models.CASCADE, null=True)
    author          = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content         = models.TextField()
    timestamp       = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name: 'Mensaje'
        verbose_name_plural: 'Mensajes'
        ordering    = ['-timestamp']

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:20]