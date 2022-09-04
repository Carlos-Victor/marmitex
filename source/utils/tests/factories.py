from __future__ import absolute_import

from django.contrib.auth import get_user_model
from factory import Faker
from factory.django import DjangoModelFactory

User = get_user_model()


class UserFactory(DjangoModelFactory):
    email = Faker("email")
    username = Faker("name")

    class Meta:
        model = User
        abstract = False
