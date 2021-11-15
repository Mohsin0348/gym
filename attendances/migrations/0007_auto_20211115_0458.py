# Generated by Django 3.2.8 on 2021-11-15 04:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_remove_classschedule_attended_members'),
        ('members', '0012_auto_20211115_0442'),
        ('attendances', '0006_auto_20211115_0442'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField(auto_now_add=True)),
                ('check_out', models.DateTimeField(blank=True, null=True)),
                ('attended_members', models.ManyToManyField(blank=True, null=True, related_name='attended_members', to='members.Member')),
                ('class_schedule', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='class_attendances', to='classes.classschedule')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='classworkout',
            name='class_attendance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='class_workouts', to='attendances.classattendance'),
        ),
    ]