# Generated by Django 5.1 on 2024-09-11 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_alter_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]