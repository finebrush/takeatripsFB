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

from backendapp.travels.views import TCAutocomplete

# urlpatterns = [
#     path('admin/', include(('vali.urls','vali'), namespace='dashboard')),
#     (url(r'^admin/', include(admin.site.urls)) if django.VERSION < (2, 0)
#      else url(r'^admin/', admin.site.urls)),
#     url(r'^chaining/', include('smart_selects.urls')),
#     # path('tc-infotravel-autocomplete/', TCAutocomplete.as_view(), name='tc-infotravel-autocomplete'),
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = i18n_patterns(
    # path('', include('clientapp.urls', namespace='clientend')),
    # # path('manager/', include('manager.urls', namespace='manager')),
    path('admin/', include(('vali.urls','vali'), namespace='dashboard')),
    path('admin/', include(admin.site.urls)) if django.VERSION < (2, 0)
         else url(r'^admin/', admin.site.urls),
    # path('', RedirectView.as_view(url='admin/', permanent=False), name='index'),
    path('tc-infotravel-autocomplete/', TCAutocomplete.as_view(), name='tc-infotravel-autocomplete'),
    path('chaning/', include('smart_selects.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
