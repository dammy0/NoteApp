# Generated by Django 5.0 on 2023-12-29 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Note', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='second_content',
        ),
    ]
