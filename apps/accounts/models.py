from django.contrib.auth.models import User
from django.db import models

class EmployeeProfile(models.Model):
    """
        Profiles of 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=120, blank=True)
    biography = models.TextField(blank=True)
    website = models.URLField(max_length=200, blank=True)
    picture = models.ImageField(upload_to='accounts/employee', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Perfil Del Empleado'
        verbose_name_plural = 'Perfiles De Los Empleados'
        ordering = ['-created']

    def __str__(self):
        return self.user.username
        