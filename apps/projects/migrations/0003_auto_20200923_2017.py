# Generated by Django 2.2 on 2020-09-24 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20200918_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='workproposals',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=45),
        ),
        migrations.AddField(
            model_name='workproposals',
            name='status',
            field=models.CharField(choices=[('Cotizado', 'Cotizado'), ('Sin Cotizar', 'Sin cotizar'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_phone', models.CharField(blank=True, max_length=50)),
                ('customer_email', models.EmailField(blank=True, max_length=45)),
                ('quotation', models.FileField(null=True, upload_to='process/documents')),
                ('status', models.CharField(choices=[('En Desarrollo', 'En Desarrollo'), ('Evaluando', 'Evaluando'), ('Terminado', 'Terminado')], max_length=20, null=True)),
                ('requeriments', models.FileField(null=True, upload_to='process/documents')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('chat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.ChatProject')),
                ('employess', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chatproject',
            name='messages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Message'),
        ),
    ]
