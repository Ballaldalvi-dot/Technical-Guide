# Generated by Django 5.1 on 2024-09-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0017_todo_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]
