# Generated by Django 2.2 on 2020-09-24 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200924_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sala',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ChatProject'),
        ),
    ]