# Generated by Django 2.2.13 on 2020-09-02 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dot_ext', '0018_auto_20200828_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='authflowuuid',
            name='auth_pkce_method',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
