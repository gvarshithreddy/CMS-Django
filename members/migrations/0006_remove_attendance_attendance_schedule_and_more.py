# Generated by Django 5.0.1 on 2024-02-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_subject_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='attendance_schedule',
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendance_schedule',
            field=models.ManyToManyField(related_name='attendance_schedule', to='members.schedulestudent'),
        ),
    ]
