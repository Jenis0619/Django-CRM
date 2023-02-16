# Generated by Django 2.1.2 on 2019-01-28 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Case",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, verbose_name="Name")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("New", "New"),
                            ("Assigned", "Assigned"),
                            ("Pending", "Pending"),
                            ("Closed", "Closed"),
                            ("Rejected", "Rejected"),
                            ("Duplicate", "Duplicate"),
                        ],
                        max_length=64,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Normal", "Normal"),
                            ("High", "High"),
                            ("Urgent", "Urgent"),
                        ],
                        max_length=64,
                    ),
                ),
                (
                    "case_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Question", "Question"),
                            ("Incident", "Incident"),
                            ("Problem", "Problem"),
                        ],
                        default="",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("closed_on", models.DateField()),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created on"),
                ),
                ("is_active", models.BooleanField(default=False)),
                (
                    "account",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.Account",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
    ]
