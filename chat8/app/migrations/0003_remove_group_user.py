# Generated by Django 4.0.2 on 2022-06-22 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_group_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
    ]