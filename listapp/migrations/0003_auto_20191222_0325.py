# Generated by Django 3.0 on 2019-12-22 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0002_auto_20191222_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
