# Generated by Django 2.0 on 2021-01-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]