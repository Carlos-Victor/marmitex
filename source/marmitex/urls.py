"""marmitex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from __future__ import absolute_import

from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from menu.api import viewsets
from menu.api.viewsets import IsSuperUser

admin.site.index_title = "Marmitex"
admin.site.site_header = "Administração Marmitex"
admin.site.site_title = "Marmitex"
admin.site.site_url = ""

schema_view = get_schema_view(
    openapi.Info(
        title="Doc API Marmitex",
        default_version=" v1",
        description="No endpoint de menu-day é retornado apenas o menu do dia da semana atual, baseado no subdomain da requisição",
        contact=openapi.Contact(email="carlosvictortecprof@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(IsSuperUser,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        r"doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/menu-day/<str:slug>/", viewsets.MenuDayViewSet.as_view(), name="menu-day"
    ),
]
