from __future__ import absolute_import

from company.tests.factories import CompanyFactory, CompanyUserFactory
from django.core.exceptions import ValidationError
from django.test import TestCase
from menu.models import MenuDay, PacketLunch
from menu.tests.factories import MenuDayFactory, PacketLunchFactory
from utils.tests.factories import UserFactory


class PacketLunchTest(TestCase):
    def setUp(self):
        return super().setUp()

    def test_unicode(self):
        packet_lunch = PacketLunchFactory.create()

        self.assertEqual(
            str(packet_lunch), f"{packet_lunch.protein_name} - {packet_lunch.value}"
        )

    def test_clean_user_not_exist_company_generic(self):
        packet_lunch = PacketLunch(
            company=CompanyFactory(),
            added_by=UserFactory(),
            protein_name="teste",
            value="12.0",
        )

        with self.assertRaisesMessage(
            ValidationError, "Usuário deve fazer parte da companhia."
        ):
            packet_lunch.clean()


class MenuDayTest(TestCase):
    def setUp(self):
        return super().setUp()

    def test_unicode(self):
        menu_day = MenuDayFactory.create()

        self.assertEqual(str(menu_day), f"{menu_day.day_week}")

    def test_menu_day_exist(self):
        user = UserFactory()
        company_user = CompanyUserFactory(user=user)

        menu_day = MenuDay(
            company=company_user.company,
            added_by=user,
            day_week="sum",
        )

        MenuDayFactory.create(
            packet_lunch=[PacketLunchFactory.create()],
            company=company_user.company,
            added_by=user,
        )

        with self.assertRaisesMessage(
            ValidationError, "Já existe um menu cadastrado para esse dia."
        ):
            menu_day.clean()
