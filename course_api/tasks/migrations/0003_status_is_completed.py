# Generated by Django 3.2.12 on 2022-04-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_status_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
