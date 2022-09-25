# Generated by Django 3.2.5 on 2022-09-25 21:50

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_suburb'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
