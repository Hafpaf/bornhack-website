# Generated by Django 3.1 on 2020-08-13 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("economy", "0014_posreport_comments"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="posreport", options={"ordering": ["date", "pos"]},
        ),
    ]
