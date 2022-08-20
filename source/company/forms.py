from __future__ import absolute_import

from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):
    operating_days = forms.MultipleChoiceField(
        choices=Company.DAY_WEEKS,
        widget=forms.SelectMultiple(attrs={"style": "width: 200px; height: 150px"}),
    )

    class Meta:
        exclude = []
        model = Company
