from __future__ import absolute_import

class MarmitexModelAdminMixin(object):
    readonly_fields = ["date_added", "added_by"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.added_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if not instance.id:
                instance.added_by = request.user
            instance.save()
        formset.save_m2m()
