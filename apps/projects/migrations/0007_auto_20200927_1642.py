# Generated by Django 2.2 on 2020-09-27 21:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200926_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='employess',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='quotation',
            field=models.FileField(blank=True, null=True, upload_to='process/documents'),
        ),
        migrations.AlterField(
            model_name='project',
            name='requeriments',
            field=models.FileField(blank=True, null=True, upload_to='process/documents'),
        ),
    ]
