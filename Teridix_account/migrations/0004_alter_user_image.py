# Generated by Django 4.0.2 on 2022-02-26 06:46

import Teridix_account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teridix_account', '0003_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Teridix_account.models.upload_image_path),
        ),
    ]
