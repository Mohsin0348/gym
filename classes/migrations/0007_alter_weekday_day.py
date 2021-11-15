# Generated by Django 3.2.8 on 2021-11-09 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_alter_baseclass_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekday',
            name='day',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], default='6', max_length=1, unique=True),
        ),
    ]
