from __future__ import absolute_import

from django.contrib import admin

from .forms import CompanyForm
from .models import Company, CompanyUser
from .utils.admin import MarmitexModelAdminMixin

# Register your models here.


class CompanyAdmin(MarmitexModelAdminMixin, admin.ModelAdmin):
    form = CompanyForm

    class Media:
        css = {"all": ("admin/css/admin.css",)}

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)

        return Company.objects.filter(companyuser__user=request.user)

    def has_add_permissions(self, request):
        return request.user.is_superuser


class CompanyUserAdmin(MarmitexModelAdminMixin, admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permissions(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyUser, CompanyUserAdmin)
