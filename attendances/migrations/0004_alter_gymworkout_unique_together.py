# Generated by Django 3.2.8 on 2021-11-14 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0003_auto_20211114_0554'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gymworkout',
            unique_together={('gym_attendance', 'base_type')},
        ),
    ]
