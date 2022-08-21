from __future__ import absolute_import

from company.models import Company
from django.core.exceptions import ValidationError
from django.db import models
from utils.models import MarmitexModel


class PacketLunch(MarmitexModel):
    protein_name = models.CharField("Nome da proteina", max_length=120)
    description = models.TextField("Descrição")
    value = models.DecimalField(
        "Valor", blank=False, null=False, max_digits=4, decimal_places=2
    )

    class Meta:
        verbose_name = "Marmita"
        verbose_name_plural = "Marmitas"

    def __str__(self):
        return f"{self.protein_name} - {self.value}"


class MenuDay(MarmitexModel):
    day_week = models.CharField(
        "Dia da semana", choices=Company.DAY_WEEKS, max_length=4
    )
    packet_lunch = models.ManyToManyField("PacketLunch", verbose_name="Marmita")

    class Meta:
        verbose_name = "Menu do dia"
        verbose_name_plural = "Menu do dia"

    def __str__(self):
        return f"{self.day_week}"

    def clean(self):
        super().clean()
        if (
            not self.pk
            and MenuDay.objects.filter(
                day_week=self.day_week, company=self.company
            ).exists()
        ):
            raise ValidationError("Já existe um menu cadastrado para esse dia.")
