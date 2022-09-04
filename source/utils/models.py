from __future__ import absolute_import

from company.models import CompanyUser, User
from django.core.exceptions import ValidationError
from django.db import models


class MarmitexModel(models.Model):
    company = models.ForeignKey(
        "company.Company", verbose_name="Companhia", on_delete=models.CASCADE
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
        abstract = True

    def clean(self):
        if not CompanyUser.objects.filter(
            user=self.added_by, company=self.company
        ).exists():
            raise ValidationError("Usuário deve fazer parte da companhia.")
