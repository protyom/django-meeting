# Generated by Django 2.2.3 on 2019-07-30 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20190730_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]