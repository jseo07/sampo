# Generated by Django 4.2.5 on 2023-10-06 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mapapp", "0002_alter_locations_table"),
    ]

    operations = [
        migrations.RenameModel(old_name="Locations", new_name="location",),
    ]
