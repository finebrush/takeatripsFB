# -*- coding: utf-8 -*-
from django.contrib import admin

from django.contrib.sites.models import Site
from taggit.models import Tag
from django.contrib.gis import admin
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS

from .widgets import AdminImageWidget
from .forms import TForm

from leaflet.admin import LeafletGeoAdmin

from mapwidgets.widgets import GooglePointFieldWidget, GooglePointFieldInlineWidget
from fieldsets_with_inlines import FieldsetsInlineMixin

from django.contrib.gis.db import models
from .models import ( City, InfoTravel, EatDrinkPart, FunPart, SeePart, SleepPart, BuyPart, 
                        TravelCurator, TCImage, TravelPlan, POIpoint, Likeit )


CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 10),
        ("mapCenterLocation", [37.59675, 126.99488]),
    ),
}

class EatDrinkPartInline(admin.StackedInline):
    model = EatDrinkPart
    extra = 1

class FunPartInline(admin.StackedInline):
    model = FunPart
    extra = 1

class SeePartInline(admin.StackedInline):
    model = SeePart
    extra = 1

class SleepPartInline(admin.StackedInline):
    model = SleepPart
    extra = 1

class BuyPartInline(admin.StackedInline):
    model = BuyPart
    extra = 1

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
    list_display = ('name', 'titleko', 'titleeng', 'titleven', 'created', 'picture_tag', 'location')
    icon_name = 'location_city'
    search_fields = ('name',)
    list_per_page = 10
    # inlines = [InfoBasicInline, InfoTravelInline]
    fieldsets = [
        ('기본 정보',   {'fields': ['name', 'created','titleko', 'titleeng', 'titleven']}),
        ('대표 이미지',  {'fields': ['picture1', 'picture2', 'picture3', 'picture4']}),
        ('위치',       {'fields': ['location']}),
    ]

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }

    # form 안에 이미지 나타내기..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'picture1' or db_field.name == 'picture2' or db_field.name == 'picture3' or db_field.name == 'picture4':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(CityAdmin,self).formfield_for_dbfield(db_field, **kwargs)

class InfoTavelAdmin(admin.ModelAdmin):
    icon_name = 'edit_location'
    # autocomplete_fields = ('ibname', 'city')
    list_display = ('companyko', 'picture_tag', 'part', 'itdate', 'typeit', 'categorysmall', 'asset')
    search_fields = ('companyko', 'companyeng', 'companyven',)
    inlines = [EatDrinkPartInline, FunPartInline, SeePartInline, SleepPartInline, BuyPartInline,]
    list_per_page = 10
    list_filter = ('part',)
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

admin.site.register(City, CityAdmin)
admin.site.register(InfoTravel, InfoTavelAdmin)
admin.site.register(TravelCurator, TravelCuratorAdmin)
admin.site.register(TravelPlan, TravelPlanAdmin)

admin.site.register(POIpoint, POIpointAdmin)
admin.site.register(TCImage, TCImageAdmin)

admin.site.register(Likeit)
# admin.site.unregister(Site)
# admin.site.unregister(Tag)
