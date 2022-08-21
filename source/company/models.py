from __future__ import absolute_import

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

from .utils import get_directory_path_logo

# Create your models here.
User = get_user_model()


class Company(models.Model):
    DAY_WEEKS = (
        ("sun", "Domingo"),
        ("mon", "Segunda"),
        ("tue", "Terça"),
        ("wed", "Quarta"),
        ("thu", "Quinta"),
        ("fri", "Sexta"),
        ("sat", "Sábado"),
    )
    name = models.CharField("Nome", max_length=160)
    slogan = models.CharField("Slogan", max_length=160)
    logo = models.ImageField(
        "Logo", upload_to=get_directory_path_logo, blank=False, null=False
    )
    operating_days = MultiSelectField(
        "Dias de funcionamento", choices=DAY_WEEKS, max_length=28, max_choices=7
    )
    opening_time = models.TimeField(
        "Horário de abertura",
        auto_now=False,
        auto_now_add=False,
        null=False,
        blank=False,
    )
    closing_time = models.TimeField(
        "Horário de encerramento",
        auto_now=False,
        auto_now_add=False,
        null=False,
        blank=False,
    )
    phone = PhoneNumberField("Telefone", blank=False)
    slug_website = models.SlugField("Slug site", unique=True)
    date_added = models.DateTimeField("data de inserção", auto_now_add=True)
    added_by = models.ForeignKey(
        User,
        verbose_name="inserido por",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "companhia"
        verbose_name_plural = "companhias"

    def __str__(self):
        return self.name

    def clean(self):
        self.slug_website = getattr(self, "slug_website", "").lower()

        if (
            not self.pk
            and getattr(self, "added_by", None)
            and not self.added_by.is_superuser
        ):
            raise ValidationError(
                "Companhia deve ser adicionado apenas por um administrador"
            )

        if (
            self.opening_time
            and self.closing_time
            and self.closing_time < self.opening_time
        ):
            raise ValidationError(
                "Horário de encerramento não pode ser menor que o de abertura"
            )


class CompanyUser(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="usuário",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name="user_company",
    )
    company = models.ForeignKey(
        Company,
        verbose_name="Companhia",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    added_by = models.ForeignKey(
        User,
        verbose_name="inserido por",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    date_added = models.DateTimeField("data de inserção", auto_now_add=True)

    class Meta:
        verbose_name = "Companhia do usuário"
        verbose_name_plural = "Companhias do usuário"

    def __str__(self):
        return f"{self.company.name} - {self.user.email}"
