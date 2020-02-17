from django import forms
from backendapp.travels.models import City, InfoTravel, TravelCurator

from dal import autocomplete
from mapwidgets.widgets import GooglePointFieldWidget

from django_summernote.widgets import SummernoteWidget

class TForm(forms.ModelForm):
	class Meta:
		model = TravelCurator
		fields = '__all__'
		widgets = {
			'infotravel' : autocomplete.ModelSelect2Multiple(
				url='tc-infotravel-autocomplete'
			)
		}
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'titleko': SummernoteWidget(),
			'titleeng': SummernoteWidget(),
			'titleven': SummernoteWidget(),
        }
		
# class POIpointAdminForm(forms.ModelForm):
# 	class Meta:
# 		model = POIpoint
# 		fields = ("point",)
# 		widgets = {
#             'point': GooglePointFieldWidget,
#         }
