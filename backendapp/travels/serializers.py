from rest_framework import serializers

from backendapp.travels.models import ( POIpoint, City, InfoTravel, Likeit, TravelCurator, Liketc, TCImage, TravelPlan, 
            Liketp, POIpoint )
from backendapp.arcontent.models import ARTrip

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class InfoTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoTravel # 모델 설정
        fields = '__all__' # 필드 설정

class TravelCuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelCurator
        fields = '__all__'

class TravelPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPlan
        fields = '__all__'

class ARTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARTrip
        fields = '__all__'

class TCImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCImage
        fields = '__all__'

class POIpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = POIpoint
        fields = '__all__'