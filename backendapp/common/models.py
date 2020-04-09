from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

from backendapp.travels.choices import SELECT_PART, SELECT_TYPE, SELECT_CATEGORY, SELECT_ORDER_NUM

class Category(models.Model):
    large = models.CharField(_('대분류'), max_length=64)
    medium = models.CharField(_('중분류'), max_length=64)
    small = models.CharField(_('소분류'), max_length=64)

    class Meta:
        verbose_name = _('카테고리')
        verbose_name_plural = _('카테고리')
        db_table = 'category'

    def __str__(self):
        return self.large

class CLarge(models.Model):
    name = models.CharField(max_length=128)
    nameeng = models.CharField(max_length=128, default='')
    nameven = models.CharField(max_length=128, default='')

    class Meta:
        verbose_name = _('대분류')
        verbose_name_plural = _('대분류')
        db_table = 'clarge'

    def __str__(self):
        return self.name

class CMedium(models.Model):
    categorylarge = models.ForeignKey(CLarge, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    nameeng = models.CharField(max_length=128, default='')
    nameven = models.CharField(max_length=128, default='')

    class Meta:
        verbose_name = _('중분류')
        verbose_name_plural = _('중분류')
        db_table = 'cmedium'

    def __str__(self):
        return self.name

class CSmall(models.Model):
    categorylarge = models.ForeignKey(CLarge, on_delete=models.CASCADE)
    categorymedium = ChainedForeignKey(
        CMedium, # 연결 할 모델..
        chained_field="categorylarge", # 연결 할 자신의 필드..
        chained_model_field="categorylarge", # 연결 할 모델의 필드..
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
        )
    name = models.CharField(max_length=128)
    nameeng = models.CharField(max_length=128, default='')
    nameven = models.CharField(max_length=128, default='')

    class Meta:
        verbose_name = _('소분류')
        verbose_name_plural = _('소분류')
        db_table = 'csmall'

    def __str__(self):
        return self.name

class PinEat(models.Model):
    objects = models.Manager()
    ordering = models.PositiveSmallIntegerField(choices=SELECT_ORDER_NUM, default=0)
    nameko = models.CharField(max_length=128)
    nameeng = models.CharField(max_length=128, null=True, blank=True)
    nameven = models.CharField(max_length=128, null=True, blank=True)
    picture = models.ImageField(_('Picture'), upload_to="%Y/%m/%d", null=True, blank=True)

    photo_thumbnail = ImageSpecField(
        source = 'picture', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션
    
    def picture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.picture.url, self.photo_thumbnail.url))
    picture_tag.allow_tags = True
    picture_tag.short_description = 'Image'

    class Meta:
        verbose_name = _('PinEat')
        verbose_name_plural = _('PinEat')
        ordering = ('ordering',)

    def __str__(self):
        return self.nameko

class PinDrink(models.Model):
    objects = models.Manager()
    ordering = models.PositiveSmallIntegerField(choices=SELECT_ORDER_NUM, default=0)
    nameko = models.CharField(max_length=128)
    nameeng = models.CharField(max_length=128, null=True, blank=True)
    nameven = models.CharField(max_length=128, null=True, blank=True)
    picture = models.ImageField(_('Picture'), upload_to="%Y/%m/%d", null=True, blank=True)

    photo_thumbnail = ImageSpecField(
        source = 'picture', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션

    def picture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.picture.url, self.photo_thumbnail.url))
    picture_tag.allow_tags = True
    picture_tag.short_description = 'Image'

    class Meta:
        verbose_name = _('PinDrink')
        verbose_name_plural = _('PinDrink')
        ordering = ('ordering',)

    def __str__(self):
        return self.nameko

class PinFun(models.Model):
    objects = models.Manager()
    ordering = models.PositiveSmallIntegerField(choices=SELECT_ORDER_NUM, default=0)
    nameko = models.CharField(max_length=128)
    nameeng = models.CharField(max_length=128, null=True, blank=True)
    nameven = models.CharField(max_length=128, null=True, blank=True)
    picture = models.ImageField(_('Picture'), upload_to="%Y/%m/%d", null=True, blank=True)

    photo_thumbnail = ImageSpecField(
        source = 'picture', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션

    def picture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.picture.url, self.photo_thumbnail.url))
    picture_tag.allow_tags = True
    picture_tag.short_description = 'Image'

    class Meta:
        verbose_name = _('PinFun')
        verbose_name_plural = _('PinFun')
        ordering = ('ordering',)

    def __str__(self):
        return self.nameko

class PinBuy(models.Model):
    objects = models.Manager()
    ordering = models.PositiveSmallIntegerField(choices=SELECT_ORDER_NUM, default=0)
    nameko = models.CharField(max_length=128)
    nameeng = models.CharField(max_length=128, null=True, blank=True)
    nameven = models.CharField(max_length=128, null=True, blank=True)
    picture = models.ImageField(_('Picture'), upload_to="%Y/%m/%d", null=True, blank=True)

    photo_thumbnail = ImageSpecField(
        source = 'picture', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션

    def picture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.picture.url, self.photo_thumbnail.url))
    picture_tag.allow_tags = True
    picture_tag.short_description = 'Image'

    class Meta:
        verbose_name = _('PinBuy')
        verbose_name_plural = _('PinBuy')
        ordering = ('ordering',)

    def __str__(self):
        return self.nameko

# ----------------------------------------TEST-----------------------------

class TmpTest(models.Model):
    name = models.CharField(max_length=50, null=True)
    choices1 = models.CharField(max_length=50, choices=SELECT_PART, verbose_name='choices Large')
    categorylarge = models.ForeignKey(CLarge, on_delete=models.CASCADE, null=True)
    categorymedium = models.ForeignKey(CMedium, on_delete=models.CASCADE, null=True)

    @property
    def choicesel(self):
        return str(self.choices1) # Eat, Drink, See, Sleep...

    def __str__(self):
        return str(self.name)

class TmpAdd(models.Model):
    name = models.CharField(max_length=30)
    tmptest = models.ForeignKey(TmpTest, on_delete=models.CASCADE, null=True)
    # has_submenu=models.BooleanField(default=1)

class TmpTag(models.Model):
    name = models.CharField(max_length=30)
    tmptest = models.ManyToManyField(TmpTest)
