# Generated by Django 4.1.7 on 2023-03-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
