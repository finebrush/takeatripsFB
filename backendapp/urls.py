import django
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles

from rest_framework import routers

from backendapp.travels.views import TCAutocomplete, CityViewSet, InfoTravelViewSet, TravelCuratorViewSet, TravelPlanViewSet

router = routers.DefaultRouter() 
router.register('citys', CityViewSet)
router.register('tripguides', InfoTravelViewSet)
router.register('tripcurators', TravelCuratorViewSet)
router.register('tripcoordinators', TravelPlanViewSet)

urlpatterns = [
    path('', include('clientapp.urls', namespace='clientapp')),
    path('blog/', include('blogapp.urls', namespace='blogapp')),
    path('login/', include('allauth.urls')),
    path('accounts/', include('accounts.urls', namespace='account')),
    
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', include(('vali.urls','vali'), namespace='dashboard')),
    path('admin/', include(admin.site.urls)) if django.VERSION < (2, 0)
         else url(r'^admin/', admin.site.urls),
    path('tc-infotravel-autocomplete/', TCAutocomplete.as_view(), name='tc-infotravel-autocomplete'),
    path('chaning/', include('smart_selects.urls')),

    path('api/', include(router.urls)),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('admin/', include(('vali.urls','vali'), namespace='dashboard')),
#     path('admin/', include(admin.site.urls)) if django.VERSION < (2, 0)
#          else url(r'^admin/', admin.site.urls),
# ]
# urlpatterns += i18n_patterns(
#     path('', include('clientapp.urls', namespace='clientapp')),
#     path('blog/', include('blogapp.urls', namespace='blogapp')),
#     path('login/', include('allauth.urls')),
#     path('accounts/', include('accounts.urls', namespace='account')),
#     path('tc-infotravel-autocomplete/', TCAutocomplete.as_view(), name='tc-infotravel-autocomplete'),
#     path('chaning/', include('smart_selects.urls')),
#     prefix_default_language=False,
# ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
