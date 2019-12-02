from django import forms

from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import AdminFileWidget

# http://www.psychicorigami.com/2009/06/20/django-simple-admin-imagefield-thumbnail/
class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            # output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="200px" /></a> %s ' % \
            #     (image_url, image_url, file_name), _('Change:')))
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="200px" /></a> ' % \
                (image_url, image_url, file_name))
        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))
