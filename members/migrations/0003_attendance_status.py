# Generated by Django 5.0.1 on 2024-02-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_attendance_subject_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
