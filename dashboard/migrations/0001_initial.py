# Generated by Django 3.2.23 on 2023-11-23 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20231123_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='الإسم')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='الموجد')),
            ],
        ),
    ]