from __future__ import absolute_import

from company.models import Company
from company.tests.factories import CompanyFactory, CompanyUserFactory
from django.core.exceptions import ValidationError
from django.test import TestCase
from utils.tests.factories import UserFactory


class CompanyTest(TestCase):
    def setUp(self):
        super().setUp()

    def test_unicode(self):
        company = CompanyFactory.create()

        self.assertEqual(str(company), company.name)

    def test_added_by_is_superuser_clean(self):
        user = UserFactory.create()
        company = Company(
            name="test",
            logo="",
            operating_days=["sun"],
            opening_time="08:00:00",
            closing_time="09:00:00",
            phone="85999999999",
            added_by=user,
        )

        with self.assertRaisesMessage(
            ValidationError, "Companhia deve ser adicionado apenas por um administrador"
        ):
            company.clean()

        user.is_superuser = True
        user.save()

        company = Company(
            name="test",
            logo="",
            operating_days=["sun"],
            opening_time="08:00:00",
            closing_time="09:00:00",
            phone="85999999999",
            added_by=user,
        )

        company.clean()

    def test_closeing_small_opening_clean(self):
        user = UserFactory.create(is_superuser=True)
        company = Company(
            name="test",
            logo="",
            operating_days=["sun"],
            opening_time="08:00:00",
            closing_time="07:59:59",
            phone="85999999999",
            added_by=user,
        )

        with self.assertRaisesMessage(
            ValidationError,
            "Horário de encerramento não pode ser menor que o de abertura",
        ):
            company.clean()


class CompanyUserTest(TestCase):
    def setUp(self):
        super().setUp()

    def test_unicode(self):
        company_user = CompanyUserFactory.create()

        self.assertEqual(
            str(company_user),
            f"{company_user.company.name} - {company_user.user.email}",
        )
