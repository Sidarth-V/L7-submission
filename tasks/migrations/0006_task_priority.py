# Generated by Django 4.0.1 on 2022-03-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_task_status_taskhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
