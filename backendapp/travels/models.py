# -*- coding: utf-8 -*-
import uuid
from django.conf import settings
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models as gismodels

from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, GroupedForeignKey

from taggit.models import TaggedItemBase, CommonGenericTaggedItemBase, TagBase, GenericTaggedItemBase
from backendapp.common.models import CLarge, CMedium, CSmall

from backendapp.travels.choices import SELECT_PART, SELECT_TYPE, SELECT_CATEGORY, SELECT_COURSE

class City(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    titleko = models.CharField(_('소개타이틀(한국어)'), max_length=128)
    titleeng = models.CharField(_('소개타이틀(영어)'), max_length=128)
    titleven = models.CharField(_('소개타이틀(베트남어)'), max_length=128)
    created = models.DateField(_('Created'))
    picture1 = models.ImageField(_('Picture1'), null=True, blank=True)
    picture2 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture3 = models.ImageField(_('Picture3'), null=True, blank=True)
    picture4 = models.ImageField(_('Picture4'), null=True, blank=True)

    location = models.PointField(verbose_name='Rocation',srid = 4326, null=True, blank=True)
    objects = GeoManager()

    photo_thumbnail = ImageSpecField(
        source = 'picture1', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션

    def picture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.picture1.url, self.photo_thumbnail.url))
    picture_tag.allow_tags = True
    picture_tag.short_description = 'Image'

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        db_table = 'city'
        ordering = ('name',)

    def __str__(self):
        return self.name

class SecondTag(TagBase):
    pass

class SecondTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(SecondTag, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_items",)

class ThirdTag(TagBase):
    pass

class ThirdTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(ThirdTag, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_items",)

class InfoTravel(models.Model):
    city = models.ForeignKey(
        'travels.City', verbose_name=_('City'), on_delete=models.CASCADE, null=True, blank=True
    )
    companyko = models.CharField(_('업체명(한국어)'), max_length=64)
    companyeng = models.CharField(_('업체명(영어)'), max_length=64)
    companyven = models.CharField(_('업체명(베트남어)'), max_length=64)
    picture1 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture2 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture3 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture4 = models.ImageField(_('Picture2'), null=True, blank=True)
    part = models.CharField(_('구분'), max_length=64, choices=SELECT_PART)
    typeit = models.IntegerField(_('유형선택'), choices=SELECT_TYPE)
    addressko = models.CharField(_('주소(한국어)'), max_length=128)
    addresseng = models.CharField(_('주소(영어)'), max_length=128)
    addressven = models.CharField(_('주소(베트남어)'), max_length=128)
    # category = models.ForeignKey(CSmall, on_delete=models.CASCADE)
    categorylarge = models.ForeignKey(CLarge, on_delete=models.CASCADE, null=True)
    categorymedium = ChainedForeignKey(
        CMedium, # 연결 할 모델..
        chained_field="categorylarge", # 연결 할 자신의 필드..
        chained_model_field="categorylarge", # 연결 할 모델의 필드..
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    categorysmall = ChainedForeignKey(
        CSmall, # 연결 할 모델..
        chained_field="categorymedium", # 연결 할 자신의 필드..
        chained_model_field="categorymedium", # 연결 할 모델의 필드..
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    # category = models.CharField(_('카테고리'), choices=SELECT_CATEGORY, max_length=8)
    linkweb = models.CharField(_('외부링크(웹사이트)'), max_length=64, null=True, blank=True)
    linkinsta = models.CharField(_('외부링크(인스타그램)'), max_length=64, null=True, blank=True)
    linkyoutube = models.CharField(_('외부링크(유튜브)'), max_length=64, null=True, blank=True)
    trafficko = models.CharField(_('교통정보(한국어)'), max_length=128, null=True, blank=True)
    trafficeng = models.CharField(_('교통정보(영어)'), max_length=128, null=True, blank=True)
    trafficven = models.CharField(_('교통정보(베트남어)'), max_length=128, null=True, blank=True)
    introko = models.TextField(_('소개정보(한국어)'), null=True, blank=True, help_text=_('이곳을 소개해 주세요.'))
    introeng = models.TextField(_('소개정보(영어)'), null=True, blank=True, help_text=_('이곳을 소개해 주세요.'))
    introven = models.TextField(_('소개정보(베트남어)'), null=True, blank=True, help_text=_('이곳을 소개해 주세요.'))
    tagko = TaggableManager(_('태그(한국어)'))
    tageng = TaggableManager(_('태그(영어)'), through=SecondTaggedItem)
    tagven = TaggableManager(_('태그(베트남어)'), through=ThirdTaggedItem)
    itdate = models.DateField(_('Date'))
    # 지도 위에서 POI 로 지정..
    itlocation = models.PointField(verbose_name='Rocation',srid = 4326, null=True, blank=True)
    objects = GeoManager()

    # thumbnail 만들기..
    photo_thumbnail = ImageSpecField(
        source = 'picture1', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션
    # admin에 html 로 나타내기.. admin.py 에서 아래 태그를 list_display 한다..
    def picture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.picture1.url, self.photo_thumbnail.url))
    picture_tag.allow_tags = True
    picture_tag.short_description = 'Image'

    def categorysmallvalue(self):
        return self.categorysmall_id

    class Meta:
        verbose_name = _('InfoTravel')
        verbose_name_plural = _('InfoTravels')
        db_table = 'infotravel'

    def __str__(self):
        return self.companyko


class EatDrinkPart(models.Model):
    part = models.OneToOneField('InfoTravel', on_delete=models.CASCADE)
    biztimeko = models.CharField(_('영업시간(한국어)'), max_length=64)
    biztimeeng = models.CharField(_('영업시간(영어)'), max_length=64)
    biztimeven = models.CharField(_('영업시간(베트남어)'), max_length=64)
    menuko = models.CharField(_('대표메뉴(한국어)'), max_length=64)
    menueng = models.CharField(_('대표메뉴(영어)'), max_length=64)
    menuven = models.CharField(_('대표메뉴(베트남어)'), max_length=64)

class SeePart(models.Model):
    part = models.OneToOneField('InfoTravel', on_delete=models.CASCADE)
    operationtimeko = models.CharField(_('운영시간(한국어)'), max_length=64)
    operationtimeeng = models.CharField(_('운영시간(영어)'), max_length=64)
    operationtimeven = models.CharField(_('운영시간(베트남어)'), max_length=64)

class SleepPart(models.Model):
    part = models.OneToOneField('InfoTravel', on_delete=models.CASCADE)
    inclusionko = models.CharField(_('포함사항(한국어)'), max_length=64)
    inclusioneng = models.CharField(_('포함사항(영어)'), max_length=64)
    inclusionven = models.CharField(_('포함사항(베트남어)'), max_length=64)
    roomtypeko = models.CharField(_('객실타입(한국어)'), max_length=64)
    roomtypeeng = models.CharField(_('객실타입(영어)'), max_length=64)
    roomtypeven = models.CharField(_('객실타입(베트남어)'), max_length=64)

class BuyPart(models.Model):
    part = models.OneToOneField('InfoTravel', on_delete=models.CASCADE)
    biztimeko = models.CharField(_('영업시간(한국어)'), max_length=64)
    biztimeeng = models.CharField(_('영업시간(영어)'), max_length=64)
    biztimeven = models.CharField(_('영업시간(베트남어)'), max_length=64)
    saleitemsko = models.CharField(_('판매상품(한국어)'), max_length=64)
    saleitemseng = models.CharField(_('판매상품(영어)'), max_length=64)
    saleitemsven = models.CharField(_('판매상품(베트남어)'), max_length=64)

class TravelCurator(models.Model):
    # tcname = models.CharField(_('Name'), max_length=64)
    city = models.ForeignKey(
        'travels.City', verbose_name=_('City'), on_delete=models.CASCADE, null=True, blank=True
    )
    titleko = models.CharField(_('제목(한국어)'), max_length=128, null=True)
    titleeng = models.CharField(_('제목(영어)'), max_length=128, null=True)
    titleven = models.CharField(_('제목(베트남어)'), max_length=128, null=True)
    created = models.DateField(_('Created'), null=True)
    writter = models.CharField(_('Writter'), max_length=64)
    introko = models.TextField(_('여행정보(한국어)'), null=True, blank=True, help_text=_('이곳을 소개해 주세요.'))
    introeng = models.TextField(_('여행정보(영어)'), null=True, blank=True, help_text=_('이곳을 소개해 주세요.'))
    introven = models.TextField(_('여행정보(베트남어)'), null=True, blank=True, help_text=_('이곳을 소개해 주세요.'))
    tagko = TaggableManager(_('태그(한국어)'))
    tageng = TaggableManager(_('태그(영어)'), through=SecondTaggedItem)
    tagven = TaggableManager(_('태그(베트남어)'), through=ThirdTaggedItem)

    infotravel = models.ManyToManyField(
        'travels.InfoTravel', verbose_name=_('여행장소 추가')
    )

    class Meta:
        verbose_name = _('TravelCurator')
        verbose_name_plural = _('TravelCurators')
        db_table = 'travelcurator'

    def __str__(self):
        return self.titleko

class TCImage(models.Model):
    travelcurator = models.ForeignKey(
        'travels.TravelCurator', verbose_name=_('TravelCurator'), on_delete=models.CASCADE, null=True, blank=True
    )
    # tcimgtitle = models.CharField(_('Image Title'), max_length=64)
    tcimg = models.ImageField(_('Trave Image'), null=False, blank=False)

    # thumbnail 만들기..
    photo_thumbnail = ImageSpecField(
        source = 'tcimg', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션
    # admin에 html 로 나타내기.. admin.py 에서 아래 태그를 list_display 한다..
    def picture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.tcimg.url, self.photo_thumbnail.url))
    picture_tag.allow_tags = True
    picture_tag.short_description = 'Image'

    class Meta:
        verbose_name = _('대표이미지(TravelCulator)')
        verbose_name_plural = _('대표이미지(TravelCulator)')
        db_table = 'tcimage'

class TravelPlan(models.Model):
    city = models.ForeignKey(
        'travels.City', verbose_name=_('City'), on_delete=models.CASCADE, null=True, blank=True
    )
    titleko = models.CharField(_('소개타이틀(한국어)'), max_length=128, null=True)
    titleeng = models.CharField(_('소개타이틀(영어)'), max_length=128, null=True)
    titleven = models.CharField(_('소개타이틀(베트남어)'), max_length=128, null=True)
    created = models.DateField(_('Created'), null=True)
    course = models.IntegerField(_('코스선택'), choices=SELECT_COURSE, default=1)
    courseinfoko = models.TextField(_('코스정보(한국어)'), null=True, blank=True, help_text=_('코스를 소개해 주세요.'))
    courseinfoeng = models.TextField(_('코스정보(영어)'), null=True, blank=True, help_text=_('코스를 소개해 주세요.'))
    courseinfoven = models.TextField(_('코스정보(베트남어)'), null=True, blank=True, help_text=_('코스를 소개해 주세요.'))
    tagko = TaggableManager(_('태그(한국어)'))
    tageng = TaggableManager(_('태그(영어)'), through=SecondTaggedItem)
    tagven = TaggableManager(_('태그(베트남어)'), through=ThirdTaggedItem)

    # inline(장소) 생성한 개수 -> admin.py 에서 가시화..
    def inlinecount(self):
        from backendapp.travels.models import POIpoint
        pointc = POIpoint.objects.filter(travelplan_id=self.id)
        return pointc.count()
    inlinecount.short_description = '장소'

    class Meta:
        verbose_name = _('TravelPlan')
        verbose_name_plural = _('TravelPlan')
        db_table = 'travelplan'

    def __str__(self):
        return self.titleko

class POIpoint(models.Model):
    travelplan = models.ForeignKey(
        'travels.TravelPlan', verbose_name=_('TravelPlan'), on_delete=models.CASCADE, null=True, blank=True
    )
    pnameko = models.CharField(_('장소명(한국어)'), max_length=40, null=True)
    pnameeng = models.CharField(_('장소명(영어)'), max_length=40, null=True)
    pnameven = models.CharField(_('장소명(베트남어)'), max_length=40, null=True)
    picture1 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture2 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture3 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture4 = models.ImageField(_('Picture2'), null=True, blank=True)

    point = models.PointField(verbose_name='위치', srid=4326, null=True, blank=True)
    objects = GeoManager()

    # thumbnail 만들기..
    photo_thumbnail = ImageSpecField(
        source = 'picture1', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션
    # admin에 html 로 나타내기.. admin.py 에서 아래 태그를 list_display 한다..
    def picture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.picture1.url, self.photo_thumbnail.url))
    picture_tag.allow_tags = True
    picture_tag.short_description = 'Image'

    class Meta:
        verbose_name = _('여행코스')
        verbose_name_plural = _('여행코스')
        db_table = 'poipoint'

    def __str__(self):
        return self.pnameko
