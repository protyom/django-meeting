# Generated by Django 2.2.3 on 2019-07-31 09:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_auto_20190730_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='students',
            field=models.ManyToManyField(blank=True, limit_choices_to={'role': 'STD'}, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]