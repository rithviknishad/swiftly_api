# Generated by Django 3.2.12 on 2022-02-12 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('typeform', '0002_form_is_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='name',
            new_name='title',
        ),
    ]
