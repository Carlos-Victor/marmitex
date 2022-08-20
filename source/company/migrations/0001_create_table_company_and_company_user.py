# Generated by Django 4.1 on 2022-08-20 17:11

from __future__ import absolute_import

import company.utils
import django.db.models.deletion
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=160, verbose_name="Nome")),
                ("slogan", models.CharField(max_length=160, verbose_name="Slogan")),
                (
                    "logo",
                    models.ImageField(
                        upload_to=company.utils.get_directory_path_logo,
                        verbose_name="Logo",
                    ),
                ),
                (
                    "operating_days",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("sun", "Domingo"),
                            ("mon", "Segunda"),
                            ("tue", "Terça"),
                            ("wed", "Quarta"),
                            ("thus", "Quinta"),
                            ("fri", "Sexta"),
                            ("sat", "Sábado"),
                        ],
                        max_length=22,
                        verbose_name="Dias de funcionamento",
                    ),
                ),
                ("opening_time", models.TimeField(verbose_name="Horário de abertura")),
                (
                    "closing_time",
                    models.TimeField(verbose_name="Horário de encerramento"),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, verbose_name="Telefone"
                    ),
                ),
                (
                    "date_added",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="data de inserção"
                    ),
                ),
                (
                    "added_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="inserido por",
                    ),
                ),
            ],
            options={
                "verbose_name": "companhia",
                "verbose_name_plural": "companhias",
            },
        ),
        migrations.CreateModel(
            name="CompanyUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_added",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="data de inserção"
                    ),
                ),
                (
                    "added_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="inserido por",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.company",
                        verbose_name="Companhia",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_company",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="usuário",
                    ),
                ),
            ],
            options={
                "verbose_name": "Companhia do usuário",
                "verbose_name_plural": "Companhias do usuário",
            },
        ),
    ]
