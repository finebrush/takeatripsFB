# -*- coding: utf-8 -*-
from django.contrib import admin

from django.contrib.sites.models import Site
from taggit.models import Tag
from django.contrib.gis import admin
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS

from .widgets import AdminImageWidget
from .forms import TForm, CityForm

from leaflet.admin import LeafletGeoAdmin

from mapwidgets.widgets import GooglePointFieldWidget, GooglePointFieldInlineWidget
from fieldsets_with_inlines import FieldsetsInlineMixin

from django.contrib.gis.db import models
from .models import ( City, InfoTravel, EatDrinkPart, EatPart, DrinkPart, FunPart, SeePart, SleepPart, BuyPart, 
                        TravelCurator, TCImage, TravelPlan, POIpoint, Likeit, TourPlan )

from import_export.admin import ImportExportModelAdmin
from import_export import resources

from django.contrib.admin.filters import SimpleListFilter

CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 10),
        ("mapCenterLocation", [37.59675, 126.99488]),
    ),
}

class InfotravelResource(resources.ModelResource):
    class Meta:
        model = InfoTravel
        fields = ['city', 'companyko', 'companyeng', 'companyven', 'picture1', 'asset', 'part' , 'typeit', 'addressko', 
            'addresseng', 'addressven', 'linkweb', 'linkinsta', 'linkyoutube', 'trafficko',
            'trafficeng', 'trafficven', 'introko', 'introeng', 'introven', 'itdate', 'itlocation']

# class EatDrinkPartInline(admin.StackedInline):
#     model = EatDrinkPart
#     extra = 1

class EatPartInline(FieldsetsInlineMixin, admin.StackedInline):
    model = EatPart
    extra = 1
    
    fieldsets_with_inlines = [
        ('기본정보', {'fields': ['biztimeko', 'biztimeeng', 'biztimeven']}),
        ('일반정보', {'fields': ['menuko', 'menueng', 'menuven']}),
        ('핀', {'fields': ['pin',]})
    ]
    # filter_horizontal = ('pin', ) #ManyToMany 일때 ..

class DrinkPartInline(FieldsetsInlineMixin, admin.StackedInline):
    model = DrinkPart
    extra = 1

    fieldsets_with_inlines = [
        ('기본정보', {'fields': ['biztimeko', 'biztimeeng', 'biztimeven']}),
        ('일반정보', {'fields': ['menuko', 'menueng', 'menuven']}),
        ('핀', {'fields': ['pin',]})
    ]

class FunPartInline(FieldsetsInlineMixin, admin.StackedInline):
    model = FunPart
    extra = 1

    fieldsets_with_inlines = [
        ('기본정보', {'fields': ['biztimeko', 'biztimeeng', 'biztimeven']}),
        ('일반정보', {'fields': ['programko', 'programeng', 'programven']}),
        ('핀', {'fields': ['pin',]})
    ]

class SeePartInline(admin.StackedInline):
    model = SeePart
    extra = 1

class SleepPartInline(admin.StackedInline):
    model = SleepPart
    extra = 1

class BuyPartInline(FieldsetsInlineMixin, admin.StackedInline):
    model = BuyPart
    extra = 1

    fieldsets_with_inlines = [
        ('기본정보', {'fields': ['biztimeko', 'biztimeeng', 'biztimeven']}),
        ('일반정보', {'fields': ['saleitemsko', 'saleitemseng', 'saleitemsven']}),
        ('핀', {'fields': ['pin',]})
    ]

class TCImageInline(admin.StackedInline):
    model = TCImage
    ordering = ('id',)
    extra = 0

class POIpointInline(admin.StackedInline):
    model = POIpoint
    ordering = ('id',)
    extra = 0

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldInlineWidget}
    }

class CityAdmin(admin.ModelAdmin):
    form = CityForm
    list_display = ('nameko', 'titleko', 'titleeng', 'titleven', 'created', 'picture_tag', 'location')
    icon_name = 'location_city'
    search_fields = ('nameko',)
    list_per_page = 10
    # inlines = [InfoBasicInline, InfoTravelInline]
    fieldsets = [
        ('기본 정보',   {'fields': ['gotocity', 'nameko', 'nameeng', 'nameven', 'created', 'logo', 'titleko', 'titleeng', 'titleven']}),
        ('대표 이미지',  {'fields': ['picture1', 'picture2', 'picture3', 'picture4']}),
        ('위치',       {'fields': ['location']}),
    ]

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }

    # form 안에 이미지 나타내기..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'picture1' or db_field.name == 'picture2' or db_field.name == 'picture3' or db_field.name == 'picture4' or db_field.name == 'logo':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(CityAdmin,self).formfield_for_dbfield(db_field, **kwargs)

class NullFilterSpec(SimpleListFilter):
    title = u''

    parameter_name = u''

    def lookups(self, request, model_admin):
        return (
            ('1', 'Has value' ),
            ('0', 'None' ),
        )

    def queryset(self, request, queryset):
        kwargs = {
        '%s'%self.parameter_name : None,
        }
        if self.value() == '0':
            return queryset.filter(**kwargs)
        if self.value() == '1':
            return queryset.exclude(**kwargs)
        return queryset

class StartNullFilterSpec(NullFilterSpec):
    title = u'Asset'
    parameter_name = u'asset'

class InfoTavelAdmin(ImportExportModelAdmin):
    resource_class = InfotravelResource
    icon_name = 'edit_location'
    # autocomplete_fields = ('ibname', 'city')
    list_display = ('companyko', 'picture_tag', 'part', 'itdate', 'typeit', 'categorysmall', 'asset')
    search_fields = ('companyko', 'companyeng', 'companyven',)
    inlines = [EatPartInline, DrinkPartInline, FunPartInline, SeePartInline, SleepPartInline, BuyPartInline,]
    list_per_page = 10
    list_filter = ('part','city',StartNullFilterSpec, )
    # radio_fields = {'asset': admin.VERTICAL} # HORIZONTAL, VERTICAL

    fieldsets = [
        ('기본 정보',   {'fields': ['city', 'itdate', 'companyko', 'companyeng', 'companyven']}),
        ('대표 이미지',  {'fields': ['picture1', 'picture2', 'picture3', 'picture4', 'picture5', 'picture6', 'picture7', 'picture8', 'picture9', 'picture10']}),
        ('일반 정보',  {'fields': ['asset', 'part', 'typeit', 'addressko', 'addresseng','addressven', 'categorylarge', 'categorymedium', 'categorysmall',
                                    'linkweb', 'linkinsta', 'linkyoutube', 'trafficko', 'trafficeng', 'trafficven',
                                    'introko', 'introeng', 'introven', 'tagko', 'tageng', 'tagven']}),
        ('위치',       {'fields': ['itlocation']}),
    ]

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }

    # (2) Show thumbnail in changeview..form 에서 이미지 보여줌..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'picture1' or db_field.name == 'picture2' or db_field.name == 'picture3' or db_field.name == 'picture4':
            # remove request to avoid "__init__() got an unexpected keyword argument 'request'" error
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(InfoTavelAdmin,self).formfield_for_dbfield(db_field, **kwargs)

    class Media:
        js = (
                'https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
                '/static/admin/js/fbinlineonoff.js',
            )

class TravelCuratorAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    form = TForm
    list_display = ('titleko', 'created')
    icon_name = 'departure_board'

    # filter_horizontal = ('infotravel',) # 좌측 리스트에서 우측 선택리스트로 보내면서 선택하기..

    # inlines = [TCImageInline]
    fieldsets_with_inlines = [
        ('기본정보', {'fields': ['city', 'titleko', 'titleeng', 'titleven', 'created', 'writter']}),
        # ('대표이미지', {'fields': ['picture1', 'picture2', 'picture3', 'picture4']}),
        TCImageInline,
        ('일반정보', {'fields': ['introko', 'introeng', 'introven', 'tagko', 'tageng', 'tagven']}),
        ('여행장소', {'fields': ['infotravel',]})
    ]

class TCImageAdmin(admin.ModelAdmin):
    icon_name = 'edit_location'
    list_display = ('travelcurator', 'picture_tag')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'tcimg':
            # remove request to avoid "__init__() got an unexpected keyword argument 'request'" error
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(TCImageAdmin,self).formfield_for_dbfield(db_field, **kwargs)

class TravelPlanAdmin(admin.ModelAdmin):
    icon_name = 'edit_location'
    list_display = ('titleko', 'inlinecount', 'created')
    inlines = [POIpointInline]

class POIpointAdmin(admin.ModelAdmin):
    icon_name = 'edit_location'
    list_display = ('pnameko', 'point')
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }

    # (2) Show thumbnail in changeview..form 에서 이미지 보여줌..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'picture1' or db_field.name == 'picture2' or db_field.name == 'picture3' or db_field.name == 'picture4':
            # remove request to avoid "__init__() got an unexpected keyword argument 'request'" error
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(POIpointAdmin,self).formfield_for_dbfield(db_field, **kwargs)

class TourPlanAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    icon_name = 'edit_location'
    list_per_page = 10
    search_fields = ('room',)

    filter_horizontal = ('pineat', 'pindrink', 'pinfun', 'pinbuy', 'pickit', 'picktp')
    fieldsets_with_inlines = [
        ('기본정보', {'fields': ['user', 'city', 'room', 'start_date', 'end_date']}),
        ('일반정보', {'fields': ['pineat', 'pindrink', 'pinfun', 'pinbuy', 'pickit', 'picktp']})
    ]

# class EatPartAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
#     icon_name = 'edit_location'
#     filter_horizontal = ('pin', )
#     fieldsets_with_inlines = [
#         ('기본정보', {'fields': ['part', 'biztimeko', 'biztimeeng', 'biztimeven']}),
#         ('일반정보', {'fields': ['menuko', 'menueng', 'menuven']}),
#         ('pin', {'fields': ['pin',]})
#     ]

admin.site.register(City, CityAdmin)
admin.site.register(InfoTravel, InfoTavelAdmin)
admin.site.register(TravelCurator, TravelCuratorAdmin)
admin.site.register(TravelPlan, TravelPlanAdmin)
admin.site.register(TourPlan, TourPlanAdmin)

admin.site.register(POIpoint, POIpointAdmin)
admin.site.register(TCImage, TCImageAdmin)

admin.site.register(Likeit)
# admin.site.register(EatPart, EatPartAdmin)

# admin.site.unregister(Site)
# admin.site.unregister(Tag)
