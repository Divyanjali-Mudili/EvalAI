# Generated by Django 2.2.20 on 2022-12-12 22:47

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0022_add_submission_model_db_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="environment_log_file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=base.utils.RandomFileName(
                    "submission_files/environment_log_file_{id}"
                ),
            ),
        ),
    ]
