# Generated by Django 3.2.4 on 2021-07-24 19:03

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='value',
            field=tinymce.models.HTMLField(),
        ),
    ]
