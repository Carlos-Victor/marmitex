from __future__ import absolute_import


def populate_permissions(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from menu.constants import GROUP_NAME

    group_app, _ = Group.objects.get_or_create(name=GROUP_NAME)

    for content_type in ContentType.objects.filter(
        app_label__in=["menu", "company"]
    ).exclude(model="companyuser"):
        permissions = Permission.objects.filter(content_type=content_type)
        group_app.permissions.add(*permissions)
