# Generated by Django 3.0.8 on 2020-11-07 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_register_attended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_location',
            field=models.CharField(default='Perth, WA, Australia', max_length=300),
        ),
    ]
