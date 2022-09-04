from __future__ import absolute_import

from company.models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "name",
            "slogan",
            "logo",
            "operating_days",
            "opening_time",
            "closing_time",
            "phone",
        ]
