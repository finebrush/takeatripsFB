from django.utils.translation import gettext_lazy as _

SELECT_PART = (
    ('Eat', _('먹다')),
    ('Drink', _('마시다')),
    ('Fun', _('놀다')),
    ('See', _('보다')),
    ('Sleep', _('자다')),
    ('Buy', _('사다'))
)

SELECT_TYPE = (
    (1, _('Must See')),
    (2, _('Hot'))
)

SELECT_CATEGORY = (
    (1, _('Place')),
    (2, _('랜드마크')),
    (3, _('자연')),
    (4, _('공원')),
    (5, _('박물관')),
    (6, _('종교')),
    (7, _('거리')),
    (8, _('시장')),
    (9, _('교통')),
    (10, _('공공'))
)

SELECT_COURSE = (
    (1, _('1시간')),
    (2, _('반나절')),
    (3, _('하루'))
)

ASSET_CHOICES = (
   ('M', _('자산')),
   ('N', _('공용'))
)
