# Generated by Django 5.0 on 2024-02-06 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0008_rename_con_kon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='kon',
            new_name='con',
        ),
    ]
