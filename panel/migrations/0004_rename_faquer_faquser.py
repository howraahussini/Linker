# Generated by Django 3.2.23 on 2023-12-10 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('panel', '0003_remove_gallery_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FAQUer',
            new_name='FAQUser',
        ),
    ]
