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

from backendapp.travels.choices import SELECT_PART, SELECT_TYPE, SELECT_CATEGORY, SELECT_COURSE, ASSET_CHOICES, SELECT_GOTOCITY

class City(models.Model):
    nameko = models.CharField(_('Name(한국어)'), max_length=64, default='')
    nameeng = models.CharField(_('Name(영어)'), max_length=64, null=True, blank=True)
    nameven = models.CharField(_('Name(베트남어)'), max_length=64, null=True, blank=True)
    logo = models.ImageField(_('Logo-Image'), upload_to="%Y/%m/%d", null=True, blank=True)
    titleko = models.TextField(_('소개타이틀(한국어)'), help_text=_('이곳을 소개해 주세요.'))
    titleeng = models.TextField(_('소개타이틀(영어)'), help_text=_('이곳을 소개해 주세요.'))
    titleven = models.TextField(_('소개타이틀(베트남어)'), help_text=_('이곳을 소개해 주세요.'))
    gotocity = models.PositiveIntegerField(_('Select City'), choices=SELECT_GOTOCITY, null=True)
    created = models.DateField(_('Created'))
    picture1 = models.ImageField(_('Picture1'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture2 = models.ImageField(_('Picture2'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture3 = models.ImageField(_('Picture3'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture4 = models.ImageField(_('Picture4'), upload_to="%Y/%m/%d", null=True, blank=True)

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
        ordering = ('nameko',)

    def __str__(self):
        return self.nameko

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
        'travels.City', verbose_name=_('City'), on_delete=models.CASCADE, null=True, blank=True, related_name='city'
    )
    companyko = models.CharField(_('업체명(한국어)'), max_length=64)
    companyeng = models.CharField(_('업체명(영어)'), max_length=64)
    companyven = models.CharField(_('업체명(베트남어)'), max_length=64)
    picture1 = models.ImageField(_('Picture1'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture2 = models.ImageField(_('Picture2'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture3 = models.ImageField(_('Picture3'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture4 = models.ImageField(_('Picture4'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture5 = models.ImageField(_('Picture5'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture6 = models.ImageField(_('Picture6'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture7 = models.ImageField(_('Picture7'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture8 = models.ImageField(_('Picture8'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture9 = models.ImageField(_('Picture9'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture10 = models.ImageField(_('Picture10'), upload_to="%Y/%m/%d", null=True, blank=True)
    asset = models.CharField(_('정보형태'), max_length=64, choices=ASSET_CHOICES, null=True)
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
    like_infotravel = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_infotravel', through='Likeit')
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

    @property
    # get method 표현..
    def like_count(self):
        return self.like_infotravel.count()

    def categorysmallvalue(self):
        return self.categorysmall_id

    class Meta:
        verbose_name = _('TripGuide')
        verbose_name_plural = _('TripGuide')
        db_table = 'infotravel'

    def __str__(self):
        return self.companyko

class Likeit(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    infotravel = models.ForeignKey(InfoTravel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'infotravel'))

class EatDrinkPart(models.Model):
    part = models.OneToOneField('InfoTravel', on_delete=models.CASCADE)
    biztimeko = models.CharField(_('영업시간(한국어)'), max_length=128)
    biztimeeng = models.CharField(_('영업시간(영어)'), max_length=128)
    biztimeven = models.CharField(_('영업시간(베트남어)'), max_length=128)
    menuko = models.CharField(_('대표메뉴(한국어)'), max_length=128)
    menueng = models.CharField(_('대표메뉴(영어)'), max_length=128)
    menuven = models.CharField(_('대표메뉴(베트남어)'), max_length=128)

class FunPart(models.Model):
    part = models.OneToOneField('InfoTravel', on_delete=models.CASCADE)
    biztimeko = models.CharField(_('영업시간(한국어)'), max_length=128)
    biztimeeng = models.CharField(_('영업시간(영어)'), max_length=128)
    biztimeven = models.CharField(_('영업시간(베트남어)'), max_length=128)
    programko = models.CharField(_('프로그램(한국어)'), max_length=128)
    programeng = models.CharField(_('프로그램(영어)'), max_length=128)
    programven = models.CharField(_('프로그램(베트남어)'), max_length=128)

class SeePart(models.Model):
    part = models.OneToOneField('InfoTravel', on_delete=models.CASCADE)
    operationtimeko = models.CharField(_('운영시간(한국어)'), max_length=128)
    operationtimeeng = models.CharField(_('운영시간(영어)'), max_length=128)
    operationtimeven = models.CharField(_('운영시간(베트남어)'), max_length=128)

class SleepPart(models.Model):
    part = models.OneToOneField('InfoTravel', on_delete=models.CASCADE)
    inclusionko = models.CharField(_('포함사항(한국어)'), max_length=128)
    inclusioneng = models.CharField(_('포함사항(영어)'), max_length=128)
    inclusionven = models.CharField(_('포함사항(베트남어)'), max_length=128)
    roomtypeko = models.CharField(_('객실타입(한국어)'), max_length=128)
    roomtypeeng = models.CharField(_('객실타입(영어)'), max_length=128)
    roomtypeven = models.CharField(_('객실타입(베트남어)'), max_length=128)

class BuyPart(models.Model):
    part = models.OneToOneField('InfoTravel', on_delete=models.CASCADE)
    biztimeko = models.CharField(_('영업시간(한국어)'), max_length=128)
    biztimeeng = models.CharField(_('영업시간(영어)'), max_length=128)
    biztimeven = models.CharField(_('영업시간(베트남어)'), max_length=128)
    saleitemsko = models.CharField(_('판매상품(한국어)'), max_length=128)
    saleitemseng = models.CharField(_('판매상품(영어)'), max_length=128)
    saleitemsven = models.CharField(_('판매상품(베트남어)'), max_length=128)

class TravelCurator(models.Model):
    objects = models.Manager()
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
    like_travelcurator = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_travelcurator', through='Liketc')

    infotravel = models.ManyToManyField(
        'travels.InfoTravel', verbose_name=_('여행장소 추가')
    )

    @property
    def infotravel_count(self):
        return self.infotravel.count()

    @property
    def tcimage_totals(self):
        return TCImage.objects.filter(travelcurator_id=self.id)

    @property
    # get method 표현..
    def like_count(self):
        return self.like_travelcurator.count()

    class Meta:
        verbose_name = _('TripCurator')
        verbose_name_plural = _('TripCurators')
        db_table = 'travelcurator'

    def __str__(self):
        return self.titleko

class Liketc(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    travelcurator = models.ForeignKey(TravelCurator, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'travelcurator'))

class TCImage(models.Model):
    objects = models.Manager()
    travelcurator = models.ForeignKey(
        'travels.TravelCurator', verbose_name=_('TravelCurator'), on_delete=models.CASCADE, null=True, blank=True
    )
    # tcimgtitle = models.CharField(_('Image Title'), max_length=64)
    tcimg = models.ImageField(_('Trave Image'), upload_to="%Y/%m/%d", null=False, blank=False)

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
    objects = models.Manager()
    city = models.ForeignKey(
        'travels.City', verbose_name=_('City'), on_delete=models.CASCADE, null=True, blank=True
    )
    titleko = models.CharField(_('소개타이틀(한국어)'), max_length=128, null=True)
    titleeng = models.CharField(_('소개타이틀(영어)'), max_length=128, null=True)
    titleven = models.CharField(_('소개타이틀(베트남어)'), max_length=128, null=True)
    created = models.DateField(_('Created'), null=True)
    course = models.CharField(_('코스선택'), max_length=64, choices=SELECT_COURSE, default=1)
    courseinfoko = models.TextField(_('코스정보(한국어)'), null=True, blank=True, help_text=_('코스를 소개해 주세요.'))
    courseinfoeng = models.TextField(_('코스정보(영어)'), null=True, blank=True, help_text=_('코스를 소개해 주세요.'))
    courseinfoven = models.TextField(_('코스정보(베트남어)'), null=True, blank=True, help_text=_('코스를 소개해 주세요.'))
    tagko = TaggableManager(_('태그(한국어)'))
    tageng = TaggableManager(_('태그(영어)'), through=SecondTaggedItem)
    tagven = TaggableManager(_('태그(베트남어)'), through=ThirdTaggedItem)
    like_travelplan = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_travelplan', through='Liketp')

    # inline(장소) 생성한 개수 -> admin.py 에서 가시화..
    def inlinecount(self):
        from backendapp.travels.models import POIpoint
        pointc = POIpoint.objects.filter(travelplan_id=self.id)
        return pointc.count()
    inlinecount.short_description = '장소'

    @property
    def poipoint_totals(self):
        return POIpoint.objects.filter(travelplan_id=self.id)

    @property
    # get method 표현..
    def like_count(self):
        return self.like_travelplan.count()

    class Meta:
        verbose_name = _('TravelCourse')
        verbose_name_plural = _('TravelCourse')
        db_table = 'travelplan'

    def __str__(self):
        return self.titleko

class Liketp(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    travelplan = models.ForeignKey(TravelPlan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'travelplan'))

class POIpoint(models.Model):
    travelplan = models.ForeignKey(
        'travels.TravelPlan', verbose_name=_('TravelPlan'), on_delete=models.CASCADE, null=True, blank=True
    )
    pnameko = models.CharField(_('장소명(한국어)'), max_length=40, null=True)
    pnameeng = models.CharField(_('장소명(영어)'), max_length=40, null=True)
    pnameven = models.CharField(_('장소명(베트남어)'), max_length=40, null=True)
    picture1 = models.ImageField(_('Picture1'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture2 = models.ImageField(_('Picture2'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture3 = models.ImageField(_('Picture3'), upload_to="%Y/%m/%d", null=True, blank=True)
    picture4 = models.ImageField(_('Picture4'), upload_to="%Y/%m/%d", null=True, blank=True)

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
