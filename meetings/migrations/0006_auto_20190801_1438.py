# Generated by Django 2.2.3 on 2019-08-01 14:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0005_auto_20190801_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='students',
            field=models.ManyToManyField(blank=True, limit_choices_to={'role': 'STD'}, related_name='user_meetings', to=settings.AUTH_USER_MODEL),
        ),
    ]
