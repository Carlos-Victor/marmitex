from __future__ import absolute_import

from company.models import Company, CompanyUser
from factory import Faker, Sequence, SubFactory
from factory.django import DjangoModelFactory, ImageField
from utils.tests.factories import UserFactory


class CompanyFactory(DjangoModelFactory):
    name = Faker("name")
    logo = ImageField(width=300, height=300)
    slogan = Faker("name")
    operating_days = ["sun"]
    opening_time = "08:00:00"
    closing_time = "09:00:00"
    phone = "85999999999"
    added_by = SubFactory(UserFactory)
    slug_website = Sequence(lambda n: "website%02d" % n)

    class Meta:
        model = Company
        abstract = False


class CompanyUserFactory(DjangoModelFactory):
    company = SubFactory(CompanyFactory)
    user = SubFactory(UserFactory)
    added_by = SubFactory(UserFactory)

    class Meta:
        model = CompanyUser
        abstract = False
