# Generated by Django 3.2.8 on 2021-11-03 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20211103_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodsconsumed',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.food'),
        ),
        migrations.AlterField(
            model_name='foodsconsumed',
            name='plan_track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumed_foods', to='members.tracknutritionplan'),
        ),
        migrations.AlterField(
            model_name='foodtoeat',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.food'),
        ),
        migrations.AlterField(
            model_name='foodtoeat',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods_to_eat', to='members.nutritionplan'),
        ),
        migrations.AlterField(
            model_name='tracknutritionplan',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_tracks', to='members.nutritionplan'),
        ),
        migrations.AlterUniqueTogether(
            name='food',
            unique_together={('name', 'uom')},
        ),
    ]
