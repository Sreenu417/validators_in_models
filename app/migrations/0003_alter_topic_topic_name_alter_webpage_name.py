# Generated by Django 4.1.4 on 2023-04-26 19:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_accessrecord"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="topic_name",
            field=models.CharField(
                max_length=100,
                primary_key=True,
                serialize=False,
                validators=[django.core.validators.MaxLengthValidator(11)],
            ),
        ),
        migrations.AlterField(
            model_name="webpage",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
