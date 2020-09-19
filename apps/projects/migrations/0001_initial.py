# Generated by Django 2.2 on 2020-09-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkProposals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_phone', models.CharField(blank=True, max_length=50)),
                ('budget', models.CharField(blank=True, max_length=50)),
                ('start_date', models.DateTimeField(blank=True)),
                ('finish_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
