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

SELECT_COURSE = (
    ('One-Hours', _('1시간')),
    ('Half-Day', _('반나절')),
    ('One-Day', _('하루'))
)

ASSET_CHOICES = (
   ('M', _('자산')),
   ('N', _('공용'))
)

SELECT_CATEGORY_TEMP = (
    (1, _('문화유적')),
    (2, _('랜드마크')),
    (3, _('거리')),
    (4, _('공원')),
    (5, _('박물관')),
    (6, _('종교')),
    (7, _('자연')),
    (8, _('시장')),
    (9, _('교통')),
    (10, _('공공')),
    (11, _('Place'))
)
SELECT_CATEGORY = (
    ('Cultural-Heritage', _('문화유적')),
    ('Landmark', _('랜드마크')),
    ('Street', _('거리')),
    ('Park', _('공원')),
    ('Museum', _('박물관')),
    ('Religion', _('종교')),
    ('Nature', _('자연')),
    ('Market', _('시장')),
    ('Traffic', _('교통')),
    ('Public', _('공공')),
    ('Place', _('장소'))
)

SELECT_GOTOCITY = (
    (1, _('Seoul')),
    (2, _('Busan'))
)