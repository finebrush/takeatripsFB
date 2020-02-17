from dal import autocomplete
from django.db.models import Q
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ( ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, ListCreateAPIView, 
        RetrieveUpdateDestroyAPIView )
from rest_framework.filters import SearchFilter

from backendapp.travels.models import City, InfoTravel, TravelCurator, TravelPlan, TCImage, POIpoint
from backendapp.arcontent.models import ARTrip

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
from .serializers import ( CitySerializer, InfoTravelSerializer, TravelCuratorSerializer, TravelPlanSerializer, 
            ARTripSerializer, TCImageSerializer, POIpointSerializer )

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class InfoTravelViewSet(viewsets.ModelViewSet):
    name = "TripGuides-List"
    queryset = InfoTravel.objects.filter(asset__isnull=False)
    filter_backends = [SearchFilter, DjangoFilterBackend] 
    filter_fields = ['city', 'part'] 
    search_fields = ['companyko', 'companyeng', 'companyven']
    serializer_class = InfoTravelSerializer

class TravelCuratorViewSet(viewsets.ModelViewSet):
    name = "TripCulator-List"
    queryset = TravelCurator.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend] 
    filter_fields = ['city',] 
    search_fields = ['titleko', 'titleeng', 'titleven']
    serializer_class = TravelCuratorSerializer

class TCImageViewSet(viewsets.ModelViewSet):
    name = "TCImage-List"
    queryset = TCImage.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['travelcurator__id']
    serializer_class = TCImageSerializer

class TravelPlanViewSet(viewsets.ModelViewSet):
    name = "TripCoordinator-List"
    queryset = TravelPlan.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend] 
    filter_fields = ['city',] 
    search_fields = ['titleko', 'titleeng', 'titleven']
    serializer_class = TravelPlanSerializer

class POIpointViewSet(viewsets.ModelViewSet):
    name = "POIpoint-List"
    queryset = POIpoint.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['travelplan__id']
    serializer_class = POIpointSerializer

class ARTripViewSet(viewsets.ModelViewSet):
    name = "ARTrip-List"
    queryset = ARTrip.objects.filter(share__isnull=False)
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['category', 'city']
    search_fields = ['titleko', 'titleeng', 'titleven']
    serializer_class = ARTripSerializer
