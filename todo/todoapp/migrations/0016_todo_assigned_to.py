# Generated by Django 5.1 on 2024-09-13 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0015_remove_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
