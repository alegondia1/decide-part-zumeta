# Generated by Django 2.0 on 2020-12-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]