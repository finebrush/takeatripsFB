from django.conf.urls import url, include
from django.urls import path
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'clientapp'

# Redirect any request that goes into here to static/index.html
urlpatterns = [
    path('', views.mytrip, name='mytrip'),
    path('mytrip_tourplan01/', views.mytrip_tourplan01, name='mytrip_tourplan01'),
    path('mytrip_tourplan02/', views.mytrip_tourplan02, name='mytrip_tourplan02'),
    path('mytrip_tourplan03/', views.mytrip_tourplan03, name='mytrip_tourplan03'),
    path('mytrip_tourplan04/', views.mytrip_tourplan04, name='mytrip_tourplan04'),
    path('mytrip_tourplan05/', views.mytrip_tourplan05, name='mytrip_tourplan05'),
    path('mytrip_detail/<int:tourplan_id>/', views.mytrip_detail, name='mytrip_detail'),

    path('trips/', views.trips, name='trips'),
    path('trip100/', views.trip100, name='trip100'),

    path('citymain/<int:city_id>/', views.citymain, name='citymain'),
    path('citymain/<int:citydetails_id>/tripguide/<str:partnum>/', views.tripguide, name='tripguide'),
    path('citymain/<int:citydetails_id>/tripguidedetail/<str:partnum>/<int:tripguide_id>/', views.tripguidedetail, name='tripguidedetail'),
    path('citymain/<int:citydetails_id>/tripguidedetail/<str:partnum>/<int:tripguide_id>/like/', views.tripguide_like, name='tripguide_like'),

    path('citymain/<int:citydetails_id>/tripcurator/', views.tripcurator, name='tripcurator'),
    path('citymain/<int:citydetails_id>/tripcurator/<int:tripcurator_id>/', views.tripcuratordetail, name='tripcuratordetail'),
    path('citymain/<int:citydetails_id>/tripcurator/<int:tripcurator_id>/like/', views.tripcurator_like, name='tripcurator_like'),

    path('citymain/<int:citydetails_id>/tripcourse/', views.tripcourse, name='tripcourse'),
    path('citymain/<int:citydetails_id>/tripcourse/<int:tripcourse_id>/', views.tripcoursedetail, name='tripcoursedetail'),
    path('citymain/<int:citydetails_id>/tripcourse/<int:tripcourse_id>/like/', views.tripcourse_like, name='tripcourse_like'),

    path('citymain/<int:citydetails_id>/gotocity/', views.gotocity, name='gotocity'),

    # path('citymain/<int:citydetails_id>/topbak/', views.topbak, name='topbak'),
    path('citymain/<int:citydetails_id>/topbak/<str:partnum>/', views.topbak, name='topbak'),

    path('citymain/<int:citydetails_id>/search/', views.searchlist, name='searchlist'),
    path('citymain/userlike/', views.userlike, name='userlike'),
    path('citymain/userlike/del', views.userlike_del, name='userlike_del'),

    # url(r'^post_like_toggle/<int:post_id>/$', views.post_like_toggle, name="post_like_toggle"),
    # url(r'^$', TemplateView.as_view(template_name='client/cintro.html'), name='cbase'),
    # url(r'^main/$', TemplateView.as_view(template_name='client/cmain.html'), name='cmain'),
    url(r'^main/$', views.cmain, name='cmain'),
    url(r'^likepoi/$', views.likePOI, name='likepoi'), 
    url(r'^detail/$', TemplateView.as_view(template_name='client/cdetail.html'), name='cdetail'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
