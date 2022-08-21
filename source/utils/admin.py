from __future__ import absolute_import

from django import forms


class MarmitexModelAdminMixin(object):
    readonly_fields = ["date_added"]

    def get_form(self, request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:
            form.base_fields["added_by"].widget = forms.HiddenInput()
            post = request.POST.copy()
            post["added_by"] = str(request.user.id)
            request.POST = post
        return form

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if not instance.id:
                instance.added_by = request.user
            instance.save()
        formset.save_m2m()
