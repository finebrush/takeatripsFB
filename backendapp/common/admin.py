from django.contrib import admin
from django import forms

from .models import Category, CLarge, CMedium, CSmall, TmpTest, TmpAdd, TmpTag

# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('large', 'medium', 'small')
    search_fields = ('large', 'medium', 'small',)
    list_per_page = 10

@admin.register(CLarge)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CMedium)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('categorylarge', 'name',)

@admin.register(CSmall)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('categorylarge', 'categorymedium', 'name',)

# ----------------------------------------TEST-----------------------------

class TmpAddInline(admin.TabularInline):
    model = TmpAdd
    ordering = ('id',)
    extra = 1

# class CategoryChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return "Category: {}".format(obj.name)

# @admin.register(TmpTest)
class TmpTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'choices1', 'choicesel', 'categorylarge',)
    inlines = [TmpAddInline]

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'categorymedium':
    #         return CategoryChoiceField(queryset=CMedium.objects.filter(categorylarge=2))
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
                'https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
                '/static/admin/js/test.js', # 필드 선택에 따라 inline show/hide..
            )
# ManyToManyField 를 inline 으로 추가하기..
class TmpTagInline(admin.TabularInline):
    model = TmpTag.tmptest.through
    # fields = ['tmptest.choices1', ]
    extra = 1
    max_num = 10

# @admin.register(TmpTag)
class TmpTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [TmpTagInline]
    exclude = ('tmptest',)

# @admin.register(TmpAdd)
# class TmpAddAdmin(admin.ModelAdmin):
#     list_display = ('name', 'tmptest',)
#
#     class Media:
#         js = ('/static/admin/js/hide_attribute.js',)

# admin.site.register(Category, CategoryAdmin)
