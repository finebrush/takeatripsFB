from dal import autocomplete

from backendapp.travels.models import City, InfoTravel, TravelCurator, TravelPlan

class TCAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Country.objects.none()

        qs = InfoTravel.objects.all()

        if self.q:
            qs = qs.filter(companyko__contains=self.q)

        return qs

# API ...
from rest_framework import viewsets
from .serializers import CitySerializer, InfoTravelSerializer, TravelCuratorSerializer, TravelPlanSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class InfoTravelViewSet(viewsets.ModelViewSet):
    queryset = InfoTravel.objects.filter(asset__isnull=False)
    serializer_class = InfoTravelSerializer

class TravelCuratorViewSet(viewsets.ModelViewSet):
    queryset = TravelCurator.objects.all()
    serializer_class = TravelCuratorSerializer

class TravelPlanViewSet(viewsets.ModelViewSet):
    queryset = TravelPlan.objects.all()
    serializer_class = TravelPlanSerializer