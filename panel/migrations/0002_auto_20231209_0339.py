# Generated by Django 3.2.23 on 2023-12-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='text',
            name='title',
        ),
        migrations.AddField(
            model_name='text',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='نص'),
        ),
    ]
