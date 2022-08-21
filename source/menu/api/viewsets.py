from __future__ import absolute_import

from datetime import datetime

from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from menu.api.serializers import MenuDaySerializer
from menu.models import MenuDay
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class MenuDayViewSet(APIView):

    queryset = MenuDay.objects.all()
    serializer_class = MenuDaySerializer
    http_method_names = ["get", "head"]

    @swagger_auto_schema(responses={200: MenuDaySerializer(many=True)})
    def get(self, request, *args, **kwargs):
        day_week = datetime.today().strftime("%A").lower()[0:3]
        try:
            menu = MenuDay.objects.get(day_week=day_week)
        except MenuDay.DoesNotExist as err:
            raise Http404

        serializer = self.serializer_class(menu)

        return Response(serializer.data)
