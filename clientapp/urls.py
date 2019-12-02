from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'clientapp'

# Redirect any request that goes into here to static/index.html
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='client/cintro.html'), name='cbase'),
    # url(r'^main/$', TemplateView.as_view(template_name='client/cmain.html'), name='cmain'),
    url(r'^main/$', views.cmain, name='cmain'),
    url(r'^likepoi/$', views.likePOI, name='likepoi'), 
    url(r'^detail/$', TemplateView.as_view(template_name='client/cdetail.html'), name='cdetail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
