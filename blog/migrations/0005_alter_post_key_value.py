# Generated by Django 4.1 on 2023-06-28 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_post_key_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="key_value",
            field=models.FloatField(
                default=1687938165.596743,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]