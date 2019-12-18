from django.contrib import admin
from backendapp.travels.widgets import AdminImageWidget

from mapwidgets.widgets import GooglePointFieldWidget, GooglePointFieldInlineWidget
from fieldsets_with_inlines import FieldsetsInlineMixin

from django.contrib.gis.db import models

from .models import ARTrip

CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 10),
        ("mapCenterLocation", [37.59675, 126.99488]),
    ),
}

class ARTripAdmin(admin.ModelAdmin):
    list_display = ('titleko', 'titleeng', 'titleven', 'created', 'picture_tag', 'category')
    icon_name = 'location_city'
    search_fields = ('titleko',)
    list_per_page = 10

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }

    # form 안에 이미지 나타내기..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'picture':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ARTripAdmin,self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(ARTrip, ARTripAdmin)
