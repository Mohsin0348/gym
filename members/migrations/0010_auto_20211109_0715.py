# Generated by Django 3.2.8 on 2021-11-09 07:15

import easy_thumbnails.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_auto_20211107_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='uom',
            field=models.CharField(choices=[('gram', 'Gram'), ('piece', 'Piece'), ('ml', 'Ml'), ('litre', 'Litre'), ('pound', 'Pound'), ('calorie', 'Calorie')], max_length=16),
        ),
        migrations.AlterField(
            model_name='trackbodymeasurement',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='body_measurements/2021-11-09/', verbose_name='ProfilePicture'),
        ),
        migrations.AlterField(
            model_name='tracknutritionplan',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='nutrition_plans/2021-11-09/', verbose_name='ProfilePicture'),
        ),
    ]