# Generated by Django 3.2.12 on 2022-02-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typeform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
