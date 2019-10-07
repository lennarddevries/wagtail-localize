# Generated by Django 2.1.9 on 2019-06-21 09:16

from django.db import migrations, models
import django.db.models.deletion
import wagtail_localize.experimental.sites.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtail_localize", "0001_initial"),
        ("wagtailcore", "0040_page_draft_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Site",
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
                (
                    "hostname",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="hostname"
                    ),
                ),
                (
                    "port",
                    models.IntegerField(
                        default=80,
                        help_text="Set this to something other than 80 if you need a specific port number to appear in URLs (e.g. development on port 8000). Does not affect request handling (so port forwarding still works).",
                        verbose_name="port",
                    ),
                ),
                (
                    "site_name",
                    models.CharField(
                        blank=True,
                        help_text="Human-readable name for the site.",
                        max_length=255,
                        null=True,
                        verbose_name="site name",
                    ),
                ),
                (
                    "is_default_site",
                    models.BooleanField(
                        default=False,
                        help_text="If true, this site will handle requests for all other hostnames that do not have a site entry of their own",
                        verbose_name="is default site",
                    ),
                ),
            ],
            options={"verbose_name": "site", "verbose_name_plural": "sites"},
        ),
        migrations.CreateModel(
            name="SiteLanguage",
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
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="is active"),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtail_localize.Language",
                        verbose_name="language",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        default=wagtail_localize.experimental.sites.models.default_region_id,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtail_localize.Region",
                        verbose_name="region",
                    ),
                ),
                (
                    "root_page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.Page",
                        verbose_name="root page",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="languages",
                        to="wagtail_localize_sites.Site",
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="site", unique_together={("hostname", "port")}
        ),
    ]
