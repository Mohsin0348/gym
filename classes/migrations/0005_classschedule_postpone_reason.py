# Generated by Django 3.2.8 on 2021-11-07 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20211106_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='classschedule',
            name='postpone_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
