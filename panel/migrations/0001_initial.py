# Generated by Django 3.2.23 on 2023-12-06 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='عنوان')),
                ('caption', models.TextField(verbose_name='شرح')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='اسم المستخدم')),
                ('image', models.ImageField(default='user/logo.svg', upload_to='user/', verbose_name='صورة')),
                ('biography', models.TextField(verbose_name='سيرة شخصية')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000, verbose_name='رابط')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='عنوان')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='عنوان')),
                ('image', models.ImageField(default='user/logo.svg', upload_to='gallery/', verbose_name='صورة')),
                ('caption', models.TextField(verbose_name='شرح')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
        migrations.CreateModel(
            name='FAQUer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='سؤال')),
                ('answer', models.TextField(verbose_name='جواب')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.mainlink')),
            ],
        ),
    ]
