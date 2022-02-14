# Generated by Django 3.2.4 on 2022-02-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teridix_main', '0002_alter_blog_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='نام کامل')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('message', models.TextField(verbose_name='در چه مواردی میتونیم کمک کنیم!')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
