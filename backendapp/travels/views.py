from dal import autocomplete
from django.db.models import Q
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter

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
    name = "TripGuides-List"
    queryset = InfoTravel.objects.filter(asset__isnull=False)
    filter_backends = [SearchFilter, DjangoFilterBackend] 
    filter_fields = ['city', 'part'] 
    search_fields = ['companyeng']
    serializer_class = InfoTravelSerializer

class TravelCuratorViewSet(viewsets.ModelViewSet):
    queryset = TravelCurator.objects.all()
    serializer_class = TravelCuratorSerializer

class TravelPlanViewSet(viewsets.ModelViewSet):
    queryset = TravelPlan.objects.all()
    serializer_class = TravelPlanSerializer
