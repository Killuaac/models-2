# Generated by Django 5.0 on 2023-12-13 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.gender'),
            preserve_default=False,
        ),
    ]
