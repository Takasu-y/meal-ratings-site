# Generated by Django 3.2.9 on 2021-12-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealsite', '0002_alter_meal_typicalmealtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='typicalMealTime',
            field=models.IntegerField(choices=[(1, 'morning'), (2, 'afternoon'), (3, 'evening')], verbose_name='時間'),
        ),
    ]
