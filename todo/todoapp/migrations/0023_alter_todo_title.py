# Generated by Django 5.1 on 2024-09-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0022_delete_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
