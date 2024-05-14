# Generated by Django 5.0.6 on 2024-05-12 22:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nominate", "0022_alter_rank_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="finalist",
            name="short_name",
            field=models.CharField(
                default=None,
                help_text="A short name for display in reports and admin interfaces. Plain text only.",
                max_length=120,
                null=True,
            ),
        ),
    ]