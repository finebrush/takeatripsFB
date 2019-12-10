# -*- coding: utf-8 -*-
import uuid
from django.conf import settings
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

from django_random_queryset import RandomManager

from backendapp.travels.choices import SELECT_CATEGORY

class ARTrip(models.Model):
    objects = RandomManager()
    share = models.BooleanField(_('공개여부'), default=True)
    titleko = models.CharField(_('소개타이틀(한국어)'), max_length=128)
    titleeng = models.CharField(_('소개타이틀(영어)'), max_length=128)
    titleven = models.CharField(_('소개타이틀(베트남어)'), max_length=128)
    created = models.DateField(_('Created'))
    category = models.PositiveIntegerField(_('구분'), choices=SELECT_CATEGORY)
    picture = models.ImageField(_('Picture'), upload_to="%Y/%m/%d", null=True, blank=True)
    file = models.FileField(_('AR File'), upload_to="%Y/%m/%d", null=True, blank=True)

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
        verbose_name = _('ARTrip')
        verbose_name_plural = _('ARTrip')
        db_table = 'artrip'
        ordering = ('titleko',)

    def __str__(self):
        return self.titleko

