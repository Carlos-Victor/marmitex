from __future__ import absolute_import

from company.tests.factories import CompanyFactory
from factory import Faker, SubFactory, post_generation
from factory.django import DjangoModelFactory
from menu.models import MenuDay, PacketLunch
from utils.tests.factories import UserFactory


class PacketLunchFactory(DjangoModelFactory):
    protein_name = Faker("name")
    description = Faker("name")
    added_by = SubFactory(UserFactory)
    value = "10.0"
    company = SubFactory(CompanyFactory)

    class Meta:
        model = PacketLunch
        abstract = False


class MenuDayFactory(DjangoModelFactory):
    company = SubFactory(CompanyFactory)
    day_week = "sun"
    added_by = SubFactory(UserFactory)

    class Meta:
        model = MenuDay
        abstract = False

    @post_generation
    def packet_lunch(self, create, extracted, **kwargs):
        if extracted:
            for packet_lunch in extracted:
                self.packet_lunch.add(packet_lunch)
