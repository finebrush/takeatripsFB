from rest_framework import serializers
import datetime

from backendapp.travels.models import ( POIpoint, City, InfoTravel, Likeit, TravelCurator, Liketc, TCImage, TravelPlan, 
            Liketp, POIpoint, TourPlan )
from backendapp.arcontent.models import ARTrip
from backendapp.common.models import PinBuy, PinDrink, PinEat, PinFun

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

class TourPlanSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(default=datetime.date.today())
    end_date = serializers.DateField(default=datetime.date.today())
    # pineat = PinEatSerializer(many=True, read_only=True)
    # pindrink = PinDrinkSerializer(many=True, read_only=True)
    # pinfun = PinFunSerializer(many=True, read_only=True)
    # pinbuy = PinBuySerializer(many=True, read_only=True)
    # pickit = InfoTravelSerializer(many=True, read_only=True)
    # picktp = TravelPlanSerializer(many=True, read_only=True)
    class Meta:
        model = TourPlan
        # fields = '__all__'
        fields = ('id', 'city', 'user', 'room', 'start_date', 'end_date', 'pineat', 'pindrink', 'pinfun', 'pinbuy', 'pickit', 'picktp',)
        extra_kwargs = {'pineat': {'required': False}, 'pindrink': {'required': False}, 'pinfun': {'required': False}, 
                'pinbuy': {'required': False}, 'pickit': {'required': False}, 'picktp': {'required': False}}

class PinEatSerializer(serializers.ModelSerializer):
    pineat = TourPlanSerializer(many=True, read_only=True)
    class Meta:
        model = PinEat
        fields = '__all__'

class PinDrinkSerializer(serializers.ModelSerializer):
    pindrink = TourPlanSerializer(many=True, read_only=True)
    class Meta:
        model = PinDrink
        fields = '__all__'

class PinFunSerializer(serializers.ModelSerializer):
    pinfun = TourPlanSerializer(many=True, read_only=True)
    class Meta:
        model = PinFun
        fields = '__all__'

class PinBuySerializer(serializers.ModelSerializer):
    pinbuy = TourPlanSerializer(many=True, read_only=True)
    class Meta:
        model = PinBuy
        fields = '__all__'
        

