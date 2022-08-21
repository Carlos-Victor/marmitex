from __future__ import absolute_import

from company.tests.factories import CompanyUserFactory
from django.urls import reverse
from freezegun import freeze_time
from menu.api.serializers import MenuDaySerializer
from menu.tests.factories import MenuDayFactory, PacketLunchFactory
from rest_framework.test import APITestCase
from utils.tests.factories import UserFactory


class MenuDayTests(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        company_user = CompanyUserFactory(user=self.user)
        self.company = company_user.company
        self.packet_lunch = PacketLunchFactory(company=self.company)
        self.menu_day = MenuDayFactory(
            company=self.company, added_by=self.user, packet_lunch=[self.packet_lunch]
        )
        return super().setUp()

    @freeze_time("2022-08-21")
    def test_sucess_menu_day(self):

        url = reverse("menu-day", args=(self.company.slug_website,))

        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), MenuDaySerializer(self.menu_day).data)

    def test_slug_not_exist(self):
        url = reverse("menu-day", args=("teste",))

        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, 404)


class SwaggerApiTests(APITestCase):
    def setUp(self):
        self.user = UserFactory(is_superuser=True)
        return super().setUp()

    def test_not_permission_doc(self):

        url = reverse("schema-swagger-ui")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)
