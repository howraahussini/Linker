# Generated by Django 3.2.23 on 2023-12-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_rename_faquer_faquser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='caption',
            field=models.TextField(blank=True, null=True, verbose_name='شرح'),
        ),
    ]
