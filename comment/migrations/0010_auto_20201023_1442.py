# Generated by Django 3.1.1 on 2020-10-23 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0009_auto_20200811_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='moderator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flags_moderated', to=settings.AUTH_USER_MODEL),
        ),
    ]