# Generated by Django 3.2.7 on 2021-10-01 08:33

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("economy", "0030_alter_coinifyinvoice_original_payment_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountingExport",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "date_from",
                    models.DateField(
                        help_text="The start date for this accounting export (YYYY-MM-DD)."
                    ),
                ),
                (
                    "date_to",
                    models.DateField(
                        help_text="The end date for this accounting export (YYYY-MM-DD)."
                    ),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True,
                        help_text="Any economy team comment for this export. Optional.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "archive",
                    models.FileField(
                        help_text="The zipfile containing the exported accounting info (html+CSV files)",
                        upload_to="accountingexports/",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
