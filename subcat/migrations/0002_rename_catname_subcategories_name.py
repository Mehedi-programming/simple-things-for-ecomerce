# Generated by Django 5.1 on 2024-11-10 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subcat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategories',
            old_name='catName',
            new_name='Name',
        ),
    ]
