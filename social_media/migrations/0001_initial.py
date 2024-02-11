# Generated by Django 3.2.23 on 2023-12-30 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('link', models.CharField(max_length=1000, verbose_name='رابط')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='X',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('link', models.CharField(max_length=1000, verbose_name='رابط')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='WhatsApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('link', models.CharField(max_length=1000, verbose_name='رابط')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Tiktok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('link', models.CharField(max_length=1000, verbose_name='رابط')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Telegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('link', models.CharField(max_length=1000, verbose_name='رابط')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Snapchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('link', models.CharField(max_length=1000, verbose_name='رابط')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('number', models.IntegerField(max_length=15, verbose_name='رقم الهاتف')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Linkedin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('link', models.CharField(max_length=1000, verbose_name='رابط')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('link', models.CharField(max_length=1000, verbose_name='رابط')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('link', models.CharField(max_length=1000, verbose_name='رابط')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('email', models.EmailField(max_length=1000, verbose_name='بریدالالکترونی')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
    ]