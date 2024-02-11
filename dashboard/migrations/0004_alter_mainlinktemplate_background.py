# Generated by Django 3.2.23 on 2024-01-21 22:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20240122_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainlinktemplate',
            name='background',
            field=models.ImageField(upload_to='background/', validators=[django.core.validators.MaxValueValidator(10485760)], verbose_name='خلفیه'),
        ),
    ]