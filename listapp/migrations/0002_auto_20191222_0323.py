# Generated by Django 3.0 on 2019-12-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(),
        ),
    ]
