# Generated by Django 2.0 on 2020-12-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0010_auto_20201230_1737'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionCandidate',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='polla',
        ),
        migrations.AddField(
            model_name='voting',
            name='candidates',
            field=models.ManyToManyField(related_name='votings', to='voting.Candidate'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Polla',
        ),
    ]