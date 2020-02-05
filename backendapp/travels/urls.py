from django.conf.urls import url, include
from django.urls import path
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'travels'

# Redirect any request that goes into here to static/index.html
urlpatterns = [
    # path('city/<int:cityid>/', views.InfoTravelCityViewSet, name='InfoTravelCityViewSet'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
