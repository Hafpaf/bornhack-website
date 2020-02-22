# Generated by Django 3.0.3 on 2020-02-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("program", "0079_eventinstance_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventproposal",
            name="allow_video_recording",
            field=models.BooleanField(
                default=False,
                help_text="Uncheck to avoid video recording. Recordings are made available under the CC BY-SA 4.0 license. Uncheck if you can not accept this license.",
            ),
        ),
    ]
