# Generated by Django 2.1.11 on 2019-12-20 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluebutton', '0003_auto_20191208_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crosswalk',
            name='_fhir_id',
            field=models.CharField(db_column='fhir_id', db_index=True, default=None, max_length=80, unique=True, null=False),
        ),
    ]
