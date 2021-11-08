# Generated by Django 3.2.8 on 2021-11-05 09:25

import django.db.models.deletion
import easy_thumbnails.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
        ('members', '0006_auto_20211104_0800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracknutritionplan',
            name='checked',
        ),
        migrations.AlterField(
            model_name='nutritionplan',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='plans_added', to='hr.employee'),
        ),
        migrations.AlterField(
            model_name='nutritionplan',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='plans_updated', to='hr.employee'),
        ),
        migrations.AlterField(
            model_name='trackbodymeasurement',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='body_measurements/2021-11-05/', verbose_name='ProfilePicture'),
        ),
        migrations.AlterField(
            model_name='tracknutritionplan',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='nutrition_plans/2021-11-05/', verbose_name='ProfilePicture'),
        ),
    ]