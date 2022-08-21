from __future__ import absolute_import

from company.api.serializers import CompanySerializer
from menu.models import MenuDay, PacketLunch
from rest_framework import serializers


class PacketLunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketLunch
        fields = ["protein_name", "description", "value"]


class MenuDaySerializer(serializers.ModelSerializer):

    company = CompanySerializer()
    packet_lunch = PacketLunchSerializer(
        many=True,
    )

    class Meta:
        model = MenuDay
        fields = ["company", "packet_lunch"]
