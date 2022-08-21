from __future__ import absolute_import

from django.contrib import admin
from menu.models import MenuDay, PacketLunch
from utils.admin import MarmitexModelAdminMixin


class PacketLunchInline(admin.TabularInline):
    model = MenuDay.packet_lunch.through
    extra = 1
    verbose_name = "Marmita"
    verbose_name_plural = "Marmitas"


class MenuDayAdmin(MarmitexModelAdminMixin, admin.ModelAdmin):

    raw_id_fields = ("company",)
    inlines = [PacketLunchInline]

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        return MenuDay.objects.filter(company__companyuser__user=request.user)


class PacketLunchAdmin(MarmitexModelAdminMixin, admin.ModelAdmin):
    raw_id_fields = ("company",)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        return PacketLunch.objects.filter(company__companyuser__user=request.user)


admin.site.register(MenuDay, MenuDayAdmin)
admin.site.register(PacketLunch, PacketLunchAdmin)
