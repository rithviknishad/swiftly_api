# Generated by Django 3.2.12 on 2022-04-24 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20220421_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='board',
        ),
    ]