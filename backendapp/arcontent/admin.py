from django.contrib import admin
from backendapp.travels.widgets import AdminImageWidget

from .models import ARTrip

class ARTripAdmin(admin.ModelAdmin):
    list_display = ('titleko', 'titleeng', 'titleven', 'created', 'picture_tag', 'category')
    icon_name = 'location_city'
    search_fields = ('titleko',)
    list_per_page = 10

    # form 안에 이미지 나타내기..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'picture':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ARTripAdmin,self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(ARTrip, ARTripAdmin)
