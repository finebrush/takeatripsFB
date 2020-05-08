from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from django.utils import timezone
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import *
from django.core import serializers
import random
from django.utils import translation
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.http import HttpResponse
from backendapp.travels.models import ( POIpoint, City, InfoTravel, Likeit, TravelCurator, Liketc, 
                            TCImage, TravelPlan, Liketp, POIpoint, TourPlan, EatPart, DrinkPart, FunPart, BuyPart )
from backendapp.arcontent.models import ARTrip
from backendapp.common.models import PinEat, PinDrink, PinFun, PinBuy

### ------ home / myTrips ----------------------------------------------------------------------------------------------------
def mytrip(request):
    city_id = 1 # 서울을 기준으로 ..
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))
    # print(tourplans)
    picture_url = ''
    tourplans = ''

    if request.user.is_authenticated: # 로그인 했다면..
        social = SocialAccount.objects.filter(user=request.user)
        tourplans = TourPlan.objects.filter(user=request.user)
        
        if social.exists(): # social 로그인 했는지 체크..   
            if social[0].provider == 'facebook':
                picture_url = "http://graph.facebook.com/{0}/picture?width={1}&height={1}".format(social[0].uid, 256)
            elif social[0].provider == 'google':
                picture_url = social[0].extra_data.picture
        # print(social[0].extra_data)
        # print(picture_url)
    
    return render(request, 'client/mytrip.html', {'citydetails':citydetails, 'current_user': current_user, 'itdetails':itdetails,
                'sns_picture':picture_url, 'tourplans':tourplans })

def mytrip_modify(request, tourplan_id):
    city_id = 1 # 서울을 기준으로 ..
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    tourplan = TourPlan.objects.get(id=tourplan_id)
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))

    sleep_itdetails = itdetails.filter(part='Sleep')
    pineats = PinEat.objects.all()
    pindrinks = PinDrink.objects.all()
    pinfuns = PinFun.objects.all()
    pinbuys = PinBuy.objects.all()

    totalnumbers = []
    numbers = []
    tp_pineats = tourplan.pineat.all()
    for tp_pineat in tp_pineats:
        numbers.append(tp_pineat.id)
    totalnumbers.append(numbers)

    numbers = []
    tp_pindrinks = tourplan.pindrink.all()
    for tp_pindrink in tp_pindrinks:
        numbers.append(tp_pindrink.id)
    totalnumbers.append(numbers)
    
    numbers = []
    tp_pinfuns = tourplan.pinfun.all()
    for tp_pinfun in tp_pinfuns:
        numbers.append(tp_pinfun.id)
    totalnumbers.append(numbers)
    
    numbers = []
    tp_pinbuys = tourplan.pinbuy.all()
    for tp_pinbuy in tp_pinbuys:
        numbers.append(tp_pinbuy.id)
    totalnumbers.append(numbers)
    
    # 검색할 타이틀을 배열로 저장..
    itdetail_names = []
    for sleep_itdetail in sleep_itdetails:
        itdetail_names.append(sleep_itdetail.companyko)
    
    return render(request, 'client/mytrip_modify.html', {'citydetails':citydetails, 'current_user': current_user, 
            'itdetails':itdetails, 'tourplan':tourplan, 'sleep_itdetails':sleep_itdetails, 'itdetail_names':itdetail_names,
            'pineats':pineats, 'pindrinks':pindrinks, 'pinfuns':pinfuns, 'pinbuys':pinbuys, 'totalnumbers':totalnumbers })

def mytrip_tourplan01(request):
    city_id = 1 # 서울을 기준으로 ..
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))

    sleep_itdetails = itdetails.filter(part='Sleep')

    # 검색할 타이틀을 배열로 저장..
    itdetail_names = []
    for sleep_itdetail in sleep_itdetails:
        itdetail_names.append(sleep_itdetail.companyko)
    
    return render(request, 'client/mytrip_tourplan01.html', {'citydetails':citydetails, 'current_user': current_user, 
            'itdetails':itdetails, 'sleep_itdetails':sleep_itdetails, 'itdetail_names':itdetail_names })

def mytrip_tourplan02(request):
    city_id = 1 # 서울을 기준으로 ..
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    pineats = PinEat.objects.all()
    
    return render(request, 'client/mytrip_tourplan02.html', {'citydetails':citydetails, 'current_user': current_user, 'pineats':pineats})

def mytrip_tourplan03(request):
    city_id = 1 # 서울을 기준으로 ..
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    pindrinks = PinDrink.objects.all()
    
    return render(request, 'client/mytrip_tourplan03.html', {'citydetails':citydetails, 'current_user': current_user, 'pindrinks':pindrinks})

def mytrip_tourplan04(request):
    city_id = 1 # 서울을 기준으로 ..
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    pinfuns = PinFun.objects.all()
    
    return render(request, 'client/mytrip_tourplan04.html', {'citydetails':citydetails, 'current_user': current_user, 'pinfuns':pinfuns})

def mytrip_tourplan05(request):
    city_id = 1 # 서울을 기준으로 ..
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    pinbuys = PinBuy.objects.all()

    tourplans = TourPlan.objects.all()
    # print(tourplans[0].pineat.all())
    # print(TourPlan.objects.values('room', 'pineat__nameko'))
    # print(tourplans.values('pineat__nameko'))
    
    return render(request, 'client/mytrip_tourplan05.html', {'citydetails':citydetails, 'current_user': current_user, 'pinbuys':pinbuys})

def mytrip_detail(request, city_id, tourplan_id):
    # city_id = 1 # 서울을 기준으로 ..
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))
    artrips = ARTrip.objects.filter(share=True)
    arcontents = artrips.random(8)
    travelcurators = TravelCurator.objects.filter(city_id=city_id)
    travelplans = TravelPlan.objects.filter(city_id=city_id)

    # 먹다/마시다/놀다/사다 대표 이미지..
    eat_itdetail = itdetails.filter(part='Eat').last()
    drink_itdetail = itdetails.filter(part='Drink').last()
    fun_itdetail = itdetails.filter(part='Fun').last()
    buy_itdetail = itdetails.filter(part='Buy').last()

    # infotravel likes..
    itcitylikes = Likeit.objects.filter(infotravel__city_id=city_id) # 해당 도시의 likes
    userlike_its = itcitylikes.filter(user=request.user)# 해당 도시의 likes 중 user의 likes
    # travelplan likes..
    tpcitylikes = Liketp.objects.filter(travelplan__city_id=city_id) 
    userlike_tps = tpcitylikes.filter(user=request.user)

    picture_url = ''
    weekdayko = ['월', '화', '수', '목', '금', '토', '일']
    weekdayeng = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    if request.user.is_authenticated: # 로그인 했다면..
        social = SocialAccount.objects.filter(user=request.user)
        # 유저가 생성한 여행계획 중 한개..
        tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))

        wstartko = weekdayko[tourplan.start_date.weekday()]
        wendko = weekdayko[tourplan.end_date.weekday()]
        wstarteng = weekdayeng[tourplan.start_date.weekday()]
        wendeng = weekdayeng[tourplan.end_date.weekday()]

        if social.exists(): # social 로그인 했는지 체크..   
            if social[0].provider == 'facebook':
                picture_url = "http://graph.facebook.com/{0}/picture?width={1}&height={1}".format(social[0].uid, 256)
            elif social[0].provider == 'google':
                picture_url = social[0].extra_data.picture
    
    # 도시마다 must 구분..
    if city_id == 1: # if seoul..
        itmusts = InfoTravel.objects.filter( Q(city_id=1) & Q(typeit=1) & Q(asset__isnull=False)) # tripguide 중 seoul 이고 must 이고 asset true 인것..
        ithots = InfoTravel.objects.filter( Q(city_id=1) & Q(typeit=2) & Q(asset__isnull=False))
    elif city_id == 2: # if busan..
        itmusts = InfoTravel.objects.filter( Q(city_id=2) & Q(typeit=1) & Q(asset__isnull=False))
        ithots = InfoTravel.objects.filter( Q(city_id=2) & Q(typeit=2) & Q(asset__isnull=False))
    
    return render(request, 'client/mytrip_detail.html', {'city_id':city_id, 'citydetails':citydetails, 'current_user': current_user, 'itdetails':itdetails, 'arcontents':arcontents,
            'travelcurators':travelcurators, 'itmusts':itmusts, 'travelplans':travelplans, 'sns_picture':picture_url, 'tourplan':tourplan,
            'eat_itdetail':eat_itdetail, 'drink_itdetail':drink_itdetail, 'fun_itdetail':fun_itdetail, 'buy_itdetail':buy_itdetail, 'ithots':ithots,
            'userlike_its':userlike_its, 'userlike_tps':userlike_tps, 'wstartko':wstartko, 'wendko':wendko, 'wstarteng':wstarteng, 'wendeng':wendeng })


### ------ myTripGuide ----------------------------------------------------------------------------------------------------
def mytripguide(request, city_id, tourplan_id, pinnum):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    weekday = ['월', '화', '수', '목', '금', '토', '일']
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))
    wstart = weekday[tourplan.start_date.weekday()]
    wend = weekday[tourplan.end_date.weekday()]

    if pinnum == 0: # 0선택없음 / 1먹다 / 2마시다 / 3놀다 / 4사다..선택했을 경우..
        pinstyles = tourplan.pineat.all()
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False)) 
    elif pinnum == 1:
        pinstyles = tourplan.pineat.all()
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Eat') & Q(asset__isnull=False))
    elif pinnum == 2:
        pinstyles = tourplan.pindrink.all()
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Drink') & Q(asset__isnull=False))
    elif pinnum == 3:
        pinstyles = tourplan.pinfun.all()
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Fun') & Q(asset__isnull=False))
    elif pinnum == 4:
        pinstyles = tourplan.pinbuy.all()
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Buy') & Q(asset__isnull=False)) 
        
    locations = []
    for itdetail in itdetails:
        point = []
        point.append(itdetail.companyko)
        point.append(itdetail.itlocation.x)
        point.append(itdetail.itlocation.y)
        # 좋아요 체크 여부..
        if current_user in itdetail.like_infotravel.all():
            point.append(1)
        else:
            point.append(0)
        point.append(itdetail.id)

        locations.append(point)

    return render(request, 'client/mytripguide.html', {'citydetails':citydetails, 'current_user': current_user,
                            'itdetails':itdetails, 'tourplan':tourplan, 'wstart':wstart, 'wend':wend, 'locations':locations,
                            'pinstyles':pinstyles , 'pinnum':pinnum })

def mytripguide_list(request, city_id, tourplan_id, pinnum, style_id):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    weekday = ['월', '화', '수', '목', '금', '토', '일']
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))
    wstart = weekday[tourplan.start_date.weekday()]
    wend = weekday[tourplan.end_date.weekday()]

    itdetails = InfoTravel.objects.none() # 빈 쿼리셋 만듬기..
    temparts = EatPart.objects.filter(pin__id=style_id) # pineat id 로 EatPart 모델 가져오기..
    if pinnum == 0: # 0선택없음 / 1먹다 / 2마시다 / 3놀다 / 4사다..선택했을 경우..
        pinstyles = tourplan.pineat.all()
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False)) 
    elif pinnum == 1:
        pinstyles = tourplan.pineat.all()
        if style_id == 0: # style 이 선택되지 않았을 경우..
            itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Eat') & Q(asset__isnull=False))
        else: # style 이 선택 되어졌을 경우..
            ittemps = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Eat') & Q(asset__isnull=False))
            for tempart in temparts: # 가져온 EatPart 도델이 해당하는 InfoTravel 모델 가져와서 병합...
                itdetails = itdetails.union(ittemps.filter(eatpart__id=tempart.id))
    elif pinnum == 2:
        pinstyles = tourplan.pindrink.all() 
        if style_id == 0:
            itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Drink') & Q(asset__isnull=False))
        else:
            ittemps = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Drink') & Q(asset__isnull=False))
            for tempart in temparts: # 가져온 EatPart 도델이 해당하는 InfoTravel 모델 가져와서 병합...
                itdetails = itdetails.union(ittemps.filter(drinkpart__id=tempart.id)) 
    elif pinnum == 3:
        pinstyles = tourplan.pinfun.all() 
        if style_id == 0:
            itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Fun') & Q(asset__isnull=False))
        else:
            ittemps = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Fun') & Q(asset__isnull=False))
            for tempart in temparts: # 가져온 EatPart 도델이 해당하는 InfoTravel 모델 가져와서 병합...
                itdetails = itdetails.union(ittemps.filter(funpart__id=tempart.id)) 
    elif pinnum == 4:
        pinstyles = tourplan.pinbuy.all()
        if style_id == 0:
            itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Buy') & Q(asset__isnull=False)) 
        else:
            ittemps = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Buy') & Q(asset__isnull=False))
            for tempart in temparts: # 가져온 EatPart 도델이 해당하는 InfoTravel 모델 가져와서 병합...
                itdetails = itdetails.union(ittemps.filter(buypart__id=tempart.id)) 
  
    # print(itdetails)

    locations = []
    for itdetail in itdetails:
        point = []
        point.append(itdetail.companyko)
        point.append(itdetail.itlocation.x)
        point.append(itdetail.itlocation.y)
        # 좋아요 체크 여부..
        if current_user in itdetail.like_infotravel.all():
            point.append(1)
        else:
            point.append(0)
        point.append(itdetail.id)

        locations.append(point)

    return render(request, 'client/mytripguide_list.html', {'citydetails':citydetails, 'current_user': current_user,
                            'itdetails':itdetails, 'tourplan':tourplan, 'wstart':wstart, 'wend':wend, 'locations':locations,
                            'pinstyles':pinstyles, 'pinnum':pinnum, 'style_id':style_id })

def mytripguide_pick(request, city_id, tourplan_id, pinnum):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    weekday = ['월', '화', '수', '목', '금', '토', '일']
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))
    wstart = weekday[tourplan.start_date.weekday()]
    wend = weekday[tourplan.end_date.weekday()]

    itdetails = InfoTravel.objects.none() # 빈 쿼리 생성..
    tmplikes = Likeit.objects.filter(user=request.user) # 유저의 like 여행정보..
    tpdetails = TravelPlan.objects.none()
    tmpliketps = Liketp.objects.filter(user=request.user)
    
    if pinnum == 1:
        for tmplike in tmplikes: # like 모델에 있는 여행정보 id 로 여행정보 모델 가져오기..
            itdetails = itdetails.union(InfoTravel.objects.filter(Q(id=tmplike.infotravel.id) & Q(part='Eat')))
    elif pinnum == 2:
        for tmplike in tmplikes: # like 모델에 있는 여행정보 id 로 여행정보 모델 가져오기..
            itdetails = itdetails.union(InfoTravel.objects.filter(Q(id=tmplike.infotravel.id) & Q(part='Drink')))
    elif pinnum == 3:
        for tmplike in tmplikes: # like 모델에 있는 여행정보 id 로 여행정보 모델 가져오기..
            itdetails = itdetails.union(InfoTravel.objects.filter(Q(id=tmplike.infotravel.id) & Q(part='Fun')))
    elif pinnum == 4:
        for tmplike in tmplikes: # like 모델에 있는 여행정보 id 로 여행정보 모델 가져오기..
            itdetails = itdetails.union(InfoTravel.objects.filter(Q(id=tmplike.infotravel.id) & Q(part='Buy')))
    elif pinnum == 5:
        for tmpliketp in tmpliketps:
                tpdetails = tpdetails.union(TravelPlan.objects.filter(Q(id=tmpliketp.travelplan.id)))
  
    locations = []
    if pinnum != 5:
        for itdetail in itdetails:
            point = []
            point.append(itdetail.companyko)
            point.append(itdetail.itlocation.x)
            point.append(itdetail.itlocation.y)
            # 좋아요 체크 여부..
            if current_user in itdetail.like_infotravel.all():
                point.append(1)
            else:
                point.append(0)
            point.append(itdetail.id)
            locations.append(point)
    else:
        for tpdetail in tpdetails:
            point = [] # 큐레이터 집합..
            point.append(tpdetail.titleko)

            ppoint = [] # tripguide 집합..
            for poipoint in tpdetail.poipoint_totals:
                tpoint = [] # tripguide 정보..
                tpoint.append(poipoint.pnameko)
                tpoint.append(poipoint.point.x)
                tpoint.append(poipoint.point.y)
                ppoint.append(tpoint)

            point.append(ppoint)
            # 좋아요 체크 여부..
            if current_user in tpdetail.like_travelplan.all():
                point.append(1)
            else:
                point.append(0)
            point.append(tpdetail.id)
            locations.append(point)
    # print(locations)

    return render(request, 'client/mytripguide_pick.html', {'citydetails':citydetails, 'current_user': current_user,
                            'itdetails':itdetails, 'tourplan':tourplan, 'wstart':wstart, 'wend':wend, 'locations':locations,
                            'pinnum':pinnum, 'tpdetails':tpdetails })

def mytripguide_detail(request, city_id, tourplan_id, tripguide_id, fromwhere):
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))
    itdetail = InfoTravel.objects.get(id=tripguide_id)
    # print(itdetail.like_infotravel.all())
    if tourplan_id == 0:
        fromhtml = False # mytrips에서 mytripguide_detail 로 바로 진입..
    else:
        fromhtml = True # mytrip_detail에서 mytripguide_detail 로 진입..
    
    return render(request, 'client/mytripguide_detail.html', {'city_id':city_id, 'tourplan_id':tourplan_id, 'itdetails':itdetails, 'itdetail':itdetail, 'fromwhere':fromwhere })

@login_required
def mytripguide_like(request, city_id, tourplan_id, tripguide_id, fromwhere):
    post = get_object_or_404(InfoTravel, pk=tripguide_id)
    # print(post.like_infotravel.all())
    if request.user in post.like_infotravel.all():
        deltrip = Likeit.objects.get(infotravel_id=tripguide_id, user=request.user)
        deltrip.delete()
        # print(Likeit.objects.get(infotravel_id=tripguide_id, user=request.user))
    else:
        savetrip = Likeit.objects.create(infotravel_id=tripguide_id, user_id=request.user.id)
        savetrip.save()
        # print(Likeit.objects.get(user=request.user))
    
    return redirect('/mytripguide_detail/'+str(city_id)+'/'+str(tourplan_id)+'/'+str(tripguide_id)+'/'+str(fromwhere)+'/')

### ------ my HotTrip ----------------------------------------------------------------------------------------------------
def myhottrip(request, city_id, tourplan_id, pinnum):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    weekday = ['월', '화', '수', '목', '금', '토', '일']
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))
    wstart = weekday[tourplan.start_date.weekday()]
    wend = weekday[tourplan.end_date.weekday()]
    
    if pinnum == 1: # typeit 1:must 2:hot 3:nomal
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Eat') & Q(typeit=2) & Q(asset__isnull=False))
    elif pinnum == 2:
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Drink') & Q(typeit=2) & Q(asset__isnull=False))
    elif pinnum == 3:
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Fun') & Q(typeit=2) & Q(asset__isnull=False))
    elif pinnum == 4:
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Buy') & Q(typeit=2) & Q(asset__isnull=False))
  
    # print(itdetails)

    locations = []
    for itdetail in itdetails:
        point = []
        point.append(itdetail.companyko)
        point.append(itdetail.itlocation.x)
        point.append(itdetail.itlocation.y)
        # 좋아요 체크 여부..
        if current_user in itdetail.like_infotravel.all():
            point.append(1)
        else:
            point.append(0)
        point.append(itdetail.id)

        locations.append(point)

    return render(request, 'client/myhottrip.html', {'citydetails':citydetails, 'current_user': current_user,
                            'itdetails':itdetails, 'tourplan':tourplan, 'wstart':wstart, 'wend':wend, 'locations':locations,
                            'pinnum':pinnum })

### ------ my HotTrip ----------------------------------------------------------------------------------------------------
def mymusttrip(request, city_id, tourplan_id, pinnum):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    weekday = ['월', '화', '수', '목', '금', '토', '일']
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))
    wstart = weekday[tourplan.start_date.weekday()]
    wend = weekday[tourplan.end_date.weekday()]
    
    if pinnum == 1: # typeit 1:must 2:hot 3:nomal
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Eat') & Q(typeit=1) & Q(asset__isnull=False))
    elif pinnum == 2:
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Drink') & Q(typeit=1) & Q(asset__isnull=False))
    elif pinnum == 3:
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Fun') & Q(typeit=1) & Q(asset__isnull=False))
    elif pinnum == 4:
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Buy') & Q(typeit=1) & Q(asset__isnull=False))
  
    # print(itdetails)

    locations = []
    for itdetail in itdetails:
        point = []
        point.append(itdetail.companyko)
        point.append(itdetail.itlocation.x)
        point.append(itdetail.itlocation.y)
        # 좋아요 체크 여부..
        if current_user in itdetail.like_infotravel.all():
            point.append(1)
        else:
            point.append(0)
        point.append(itdetail.id)

        locations.append(point)

    return render(request, 'client/mymusttrip.html', {'citydetails':citydetails, 'current_user': current_user,
                            'itdetails':itdetails, 'tourplan':tourplan, 'wstart':wstart, 'wend':wend, 'locations':locations,
                            'pinnum':pinnum })

### ------ myCurator ----------------------------------------------------------------------------------------------------
def mycurator(request, city_id, tourplan_id):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    travelplans = TravelPlan.objects.filter(city_id=city_id)

    weekday = ['월', '화', '수', '목', '금', '토', '일']
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))
    wstart = weekday[tourplan.start_date.weekday()]
    wend = weekday[tourplan.end_date.weekday()]
    
    return render(request, 'client/mycurator.html', {'citydetails':citydetails, 'current_user': current_user,
                            'travelplans':travelplans, 'tourplan':tourplan, 'wstart':wstart, 'wend':wend })

def mycurator_detail(request, city_id, tourplan_id, travelplan_id):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))
    travelplans = TravelPlan.objects.filter(city_id=city_id)
    travelplan = TravelPlan.objects.get(id=travelplan_id)

    weekday = ['월', '화', '수', '목', '금', '토', '일']
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))
    wstart = weekday[tourplan.start_date.weekday()]
    wend = weekday[tourplan.end_date.weekday()]

    locations = []
    for poipoint in travelplan.poipoint_totals:
        point = []
        point.append(poipoint.pnameko)
        point.append(poipoint.point.x)
        point.append(poipoint.point.y)

        locations.append(point)

    pictures = []
    for poipoint in travelplan.poipoint_totals:
        picture = []
        picture.append(poipoint.picture1.name) # path 저장시 name 으로..
        picture.append(poipoint.picture2.name)
        picture.append(poipoint.picture3.name)
        picture.append(poipoint.picture4.name)
        # print(picture)
        pictures.append(picture)
    
    return render(request, 'client/mycurator_detail.html', {'citydetails':citydetails, 'current_user': current_user,
                            'travelplans':travelplans, 'travelplan':travelplan, 'itdetails':itdetails, 'tourplan':tourplan, 
                            'wstart':wstart, 'wend':wend, 'locations':locations, 'pictures':pictures })

@login_required
def mycurator_like(request, city_id, tourplan_id, travelplan_id):
    post = get_object_or_404(TravelPlan, pk=travelplan_id)
    # print(post.like_infotravel.all())
    if request.user in post.like_travelplan.all():
        deltrip = Liketp.objects.get(travelplan_id=travelplan_id, user=request.user)
        deltrip.delete()
        # print(Likeit.objects.get(infotravel_id=tripguide_id, user=request.user))
    else:
        savetrip = Liketp.objects.create(travelplan_id=travelplan_id, user_id=request.user.id)
        savetrip.save()
        # print(Likeit.objects.get(user=request.user))
    
    return redirect('/mycurator_detail/'+str(city_id)+'/'+str(tourplan_id)+'/'+str(travelplan_id))

### ------ myTrip100 ----------------------------------------------------------------------------------------------------
def mytrip100(request, city_id, tourplan_id, pinnum):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    weekday = ['월', '화', '수', '목', '금', '토', '일']
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))
    wstart = weekday[tourplan.start_date.weekday()]
    wend = weekday[tourplan.end_date.weekday()]

    if pinnum == 0: # 0선택없음 / 1먹다 / 2마시다 / 3놀다 / 4사다..선택했을 경우..
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False)) 
    elif pinnum == 1:
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Eat') & Q(asset__isnull=False)) #-> eat tripguide 만..
    elif pinnum == 2:
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Drink') & Q(asset__isnull=False))
    elif pinnum == 3:
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Fun') & Q(asset__isnull=False))
    elif pinnum == 4:
        itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Buy') & Q(asset__isnull=False)) 

    ## 페이지로 넘길때 사용.
    # paginator = Paginator(itdetails, 6)
    # page = request.POST.get('page')
    # itdetails = paginator.get_page(page)

    locations = []
    for itdetail in itdetails:
        point = []
        point.append(itdetail.companyko)
        point.append(itdetail.itlocation.x)
        point.append(itdetail.itlocation.y)
        # 좋아요 체크 여부..
        if current_user in itdetail.like_infotravel.all():
            point.append(1)
        else:
            point.append(0)
        point.append(itdetail.id)

        locations.append(point)
    
    return render(request, 'client/mytrip100.html', {'citydetails':citydetails, 'current_user': current_user, 'pinnum':pinnum,
                            'itdetails':itdetails, 'tourplan':tourplan, 'wstart':wstart, 'wend':wend, 'locations':locations })

# 페이지로 넘길때 사용...
def post_list_ajax(request, city_id, tourplan_id): #Ajax 로 호출하는 함수
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))

    # itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(part='Eat') & Q(asset__isnull=False)) #-> eat tripguide 만..
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False)) #-> tripguide 모두.데이터부족으로 테스트하기위해..
    paginator = Paginator(itdetails, 6)
    page = request.POST.get('page')
    if int(page) <= paginator.num_pages: # 마지막 페이지 체크하여 크면 빈 데이터 넘긴다..
        eat_itdetails = paginator.get_page(page)
    else:
        eat_itdetails = ""

    return render(request, 'client/post_list_ajax.html', { 'citydetails':citydetails, 'current_user': current_user,
                            'eat_itdetails':eat_itdetails, 'tourplan':tourplan, 'page':page }) #Ajax 로 호출하는 템플릿은 _ajax로 표시.

### ------ my gotocity ----------------------------------------------------------------------------------------------------------
def mygotocity(request, city_id, tourplan_id):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    weekday = ['월', '화', '수', '목', '금', '토', '일']
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))
    wstart = weekday[tourplan.start_date.weekday()]
    wend = weekday[tourplan.end_date.weekday()]

    return render(request, 'client/mygotocity.html', {'citydetails':citydetails, 'current_user': current_user,
                            'tourplan':tourplan, 'wstart':wstart, 'wend':wend })

### ------ Trips ----------------------------------------------------------------------------------------------------------
def trips(request, city_id):
    # city_id = 1 # 서울을 기준으로 ..
    citys = City.objects.all()
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))
    # print(tourplans)
    picture_url = ''
    tourplans = ''
    
    if request.user.is_authenticated: # 로그인 했다면..
        social = SocialAccount.objects.filter(user=request.user)
        tourplans = TourPlan.objects.filter(user=request.user)
        if social.exists(): # social 로그인 했는지 체크..   
            if social[0].provider == 'facebook':
                picture_url = "http://graph.facebook.com/{0}/picture?width={1}&height={1}".format(social[0].uid, 256)
            elif social[0].provider == 'google':
                picture_url = social[0].extra_data.picture
        # print(social[0].extra_data)
        # print(picture_url)
    
    return render(request, 'client/trips.html', {'citys':citys, 'citydetails':citydetails, 'current_user': current_user, 'itdetails':itdetails,
                'sns_picture':picture_url, 'tourplans':tourplans })

### ------ Trip100 ----------------------------------------------------------------------------------------------------
def tripstore(request, city_id):
    # city_id = 1 # 서울을 기준으로 ..
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))
    # print(tourplans)
    picture_url = ''
    tourplans = ''
    
    if request.user.is_authenticated: # 로그인 했다면..
        social = SocialAccount.objects.filter(user=request.user)
        tourplans = TourPlan.objects.filter(user=request.user)
        if social.exists(): # social 로그인 했는지 체크..   
            if social[0].provider == 'facebook':
                picture_url = "http://graph.facebook.com/{0}/picture?width={1}&height={1}".format(social[0].uid, 256)
            elif social[0].provider == 'google':
                picture_url = social[0].extra_data.picture
        # print(social[0].extra_data)
        # print(picture_url)
    
    return render(request, 'client/tripstore.html', {'citydetails':citydetails, 'current_user': current_user, 'itdetails':itdetails,
                'sns_picture':picture_url, 'tourplans':tourplans })
### ------ 기타.. ----------------------------------------------------------------------------------------------------
def searchtrips(request, city_id, tourplan_id):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user

    weekday = ['월', '화', '수', '목', '금', '토', '일']
    tourplan = TourPlan.objects.get(Q(user=request.user) & Q(id=tourplan_id))
    wstart = weekday[tourplan.start_date.weekday()]
    wend = weekday[tourplan.end_date.weekday()]
    
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))

    locations = []
    if request.method=='POST':
        srch = request.POST['srhwd']
        if srch:
            # 한단어만 넣어야 결과가 나옴..한 도시에서만 검색하기 위함..전체->InfoTravel.objects.filter로..
            # matchs = itdetails.filter(Q(tagko__name__icontains=srch) |
            #                                     Q(tageng__name__icontains=srch) |
            #                                     Q(tagven__name__icontains=srch)
            #                                     )

            # 여러 단어 넣으도 결과 나옴, 단 단어가 포함된 결과는 안나오고 딱! 일치한 것만..
            searchwords=srch.split(' ')
            matchs = itdetails.filter(Q(tagko__name__in=searchwords) |
                                                Q(tageng__name__in=searchwords) |
                                                Q(tagven__name__in=searchwords)
                                                ).distinct()

            if matchs:
                for match in matchs:
                    point = []
                    point.append(match.companyko)
                    point.append(match.itlocation.x)
                    point.append(match.itlocation.y)
                    # 좋아요 체크 여부..
                    if current_user in match.like_infotravel.all():
                        point.append(1)
                    else:
                        point.append(0)
                    point.append(match.id)

                    locations.append(point)
                    
                return render(request, 'client/mytripguide_search.html', {'citydetails':citydetails, 'tourplan':tourplan,
                                    'locations':locations, 'current_user':current_user, 'matchs':matchs })
            else:
                messages.error(request, 'no result found!')
        else:
            return HttpResponseRedirect('search/'+city_id+'/')

    return render(request, 'client/mytripguide_search.html', {'citydetails':citydetails, 'tourplan':tourplan, 
                            'locations':locations, 'current_user':current_user, })


### 기존 ...................................................................................................................
def home(request):
    city_id = 1 # 서울을 기준으로 ..
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    topmenuoff = True
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))
    artrips = ARTrip.objects.filter(share=True)
    arcontents = artrips.random(8)
    travelcurators = TravelCurator.objects.filter(city_id=city_id)
    travelplans = TravelPlan.objects.filter(city_id=city_id)

    eat_itdetail = itdetails.filter(part='Eat').last()
    drink_itdetail = itdetails.filter(part='Drink').last()
    fun_itdetail = itdetails.filter(part='Fun').last()
    see_itdetail = itdetails.filter(part='See').last()
    sleep_itdetail = itdetails.filter(part='Sleep').last()
    buy_itdetail = itdetails.filter(part='Buy').last()
    
    return render(request, 'client/trip100.html', {'citydetails':citydetails, 'current_user': current_user, 'itdetails':itdetails, 'arcontents':arcontents,
            'eat_itdetail':eat_itdetail, 'drink_itdetail':drink_itdetail, 'fun_itdetail':fun_itdetail, 'see_itdetail':see_itdetail, 
            'sleep_itdetail':sleep_itdetail, 'buy_itdetail':buy_itdetail, 'topmenuoff':topmenuoff, 'travelcurators':travelcurators, 'travelplans':travelplans })

def chome(request):
    citys = City.objects.filter().order_by('id') # 순차적으로 불러오기..
    current_user = request.user
    topmenuoff = False # 상단 메뉴가 display none..
    
    return render(request, 'client/cindex.html', {'citys': citys , 'current_user': current_user, 'topmenuoff':topmenuoff})

def citymain(request, city_id):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    topmenuoff = True
    itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False))
    artrips = ARTrip.objects.filter(share=True)
    arcontents = artrips.random(8)
    travelcurators = TravelCurator.objects.filter(city_id=city_id)
    travelplans = TravelPlan.objects.filter(city_id=city_id)

    # InfoTravel 에서 part 별 랜덤한 하나의 DB를 전달..
    # num_itdetail = itdetails.filter(part='Eat').count()
    # rand_entitie = random.sample(range(num_itdetail), 1)
    # eat_itdetail = itdetails.filter(id__in=rand_entitie)
    
    # eat_itdetails = InfoTravel.objects.filter(Q(city_id=city_id) & Q(asset__isnull=False) & Q(part='Eat'))
    # eat_itdetail = eat_itdetails.random(1)
    # print(eat_itdetail)

    eat_itdetail = itdetails.filter(part='Eat').last()
    drink_itdetail = itdetails.filter(part='Drink').last()
    fun_itdetail = itdetails.filter(part='Fun').last()
    see_itdetail = itdetails.filter(part='See').last()
    sleep_itdetail = itdetails.filter(part='Sleep').last()
    buy_itdetail = itdetails.filter(part='Buy').last()
    
    return render(request, 'client/citydetail.html', {'citydetails':citydetails, 'current_user': current_user, 'itdetails':itdetails, 'arcontents':arcontents,
            'eat_itdetail':eat_itdetail, 'drink_itdetail':drink_itdetail, 'fun_itdetail':fun_itdetail, 'see_itdetail':see_itdetail, 
            'sleep_itdetail':sleep_itdetail, 'buy_itdetail':buy_itdetail, 'topmenuoff':topmenuoff, 'travelcurators':travelcurators, 'travelplans':travelplans })

def tripguide(request, citydetails_id, partnum):
    citydetails = City.objects.get(id=citydetails_id)
    current_user = request.user
    topmenuoff = True
    itdetails = InfoTravel.objects.filter(Q(city_id=citydetails_id) & Q(asset__isnull=False))
    # print(city.name)
    eat_itdetails = itdetails.filter(part='Eat')
    drink_itdetails = itdetails.filter(part='Drink')
    fun_itdetails = itdetails.filter(part='Fun')
    see_itdetails = itdetails.filter(part='See')
    sleep_itdetails = itdetails.filter(part='Sleep')
    buy_itdetails = itdetails.filter(part='Buy')

    if partnum == 'Eat':
        selected_itdetails = eat_itdetails
    elif partnum =='Drink':
        selected_itdetails = drink_itdetails
    elif partnum == 'Fun':
        selected_itdetails = fun_itdetails
    elif partnum == 'See':
        selected_itdetails = see_itdetails
    elif partnum == 'Sleep':
        selected_itdetails = sleep_itdetails
    elif partnum == 'Buy':
        selected_itdetails = buy_itdetails
    elif partnum == 'All':
        selected_itdetails = itdetails

    return render(request, 'client/tripguide.html', {'citydetails':citydetails, 'current_user': current_user, 'citydetails_id':citydetails_id, 'partnum':partnum, 
                            'selected_itdetails':selected_itdetails, 'topmenuoff':topmenuoff })

def tripguidedetail(request, citydetails_id, partnum, tripguide_id):
    itdetails = InfoTravel.objects.filter(Q(city_id=citydetails_id) & Q(asset__isnull=False))
    itdetail = InfoTravel.objects.get(id=tripguide_id)
    # print(itdetail.like_infotravel.all())
    return render(request, 'client/tripguidedetail.html', {'citydetails_id':citydetails_id, 'itdetails':itdetails, 'partnum':partnum, 
                        'itdetail':itdetail,})

@login_required
def tripguide_like(request, citydetails_id, partnum, tripguide_id):
    post = get_object_or_404(InfoTravel, pk=tripguide_id)
    # 중간자 모델 Like 를 사용하며, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다..
    post_likeit, post_likeit_created = post.likeit_set.get_or_create(user=request.user)
    # print(post_likeit_created)
    
    if not post_likeit_created:
        post_likeit.delete()
        return redirect('/citymain/'+str(citydetails_id)+'/tripguidedetail/'+str(partnum)+'/'+str(tripguide_id))
    
    return redirect('/citymain/'+str(citydetails_id)+'/tripguidedetail/'+str(partnum)+'/'+str(tripguide_id))

def tripcurator(request, citydetails_id):
    citydetails = get_object_or_404(City, pk=citydetails_id)
    current_user = request.user
    topmenuoff = True
    travelcurators = TravelCurator.objects.filter(city_id=citydetails_id)
    
    return render(request, 'client/tripcurator.html', {'citydetails':citydetails, 'current_user': current_user,
                                    'travelcurators':travelcurators, 'topmenuoff':topmenuoff })

def tripcuratordetail(request, citydetails_id, tripcurator_id):
    citydetails = get_object_or_404(City, pk=citydetails_id)
    current_user = request.user
    travelcurators = TravelCurator.objects.filter(city_id=citydetails_id)
    travelcurator = TravelCurator.objects.get(id=tripcurator_id)

    # 제목으로 검색..
    searchwords=travelcurator.titleko.split(' ')
    searchlists = InfoTravel.objects.filter(Q(tagko__name__in=searchwords) & Q(asset__isnull=False)).distinct()
    # searchlist = ['문화', '연가'] # or 로 하나라도 포함된 걸 검색..
    # print(InfoTravel.objects.filter(tagko__name__in=searchlist).distinct()) # .distinct() -> 중복 제거..

    # 추천장소 리스트
    addedinfotravels = travelcurator.infotravel.all() 

    return render(request, 'client/tripcuratordetail.html', {'citydetails':citydetails, 'current_user': current_user,
                                'travelcurator':travelcurator, 'travelcurators':travelcurators , 'addedinfotravels':addedinfotravels,
                                'searchlists':searchlists })

@login_required
def tripcurator_like(request, citydetails_id, tripcurator_id):
    post = get_object_or_404(TravelCurator, pk=tripcurator_id)
    # 중간자 모델 Like 를 사용하며, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다..
    post_liketc, post_liketc_created = post.liketc_set.get_or_create(user=request.user)

    if not post_liketc_created:
        post_liketc.delete()
        return redirect('/citymain/'+str(citydetails_id)+'/tripcurator/'+str(tripcurator_id))
    
    return redirect('/citymain/'+str(citydetails_id)+'/tripcurator/'+str(tripcurator_id))


def tripcourse(request, citydetails_id):
    citydetails = get_object_or_404(City, pk=citydetails_id)
    current_user = request.user
    topmenuoff = True
    travelplans = TravelPlan.objects.filter(city_id=citydetails_id)
    
    return render(request, 'client/tripcourse.html', {'citydetails':citydetails, 'current_user': current_user,
                            'travelplans':travelplans, 'topmenuoff':topmenuoff })

def tripcoursedetail(request, citydetails_id, tripcourse_id):
    citydetails = get_object_or_404(City, pk=citydetails_id)
    current_user = request.user
    travelplans = TravelPlan.objects.filter(city_id=citydetails_id)
    travelplan = TravelPlan.objects.get(id=tripcourse_id)
    
    locations = []
    for poipoint in travelplan.poipoint_totals:
        point = []
        point.append(poipoint.pnameko)
        point.append(poipoint.point.x)
        point.append(poipoint.point.y)

        locations.append(point)

    pictures = []
    for poipoint in travelplan.poipoint_totals:
        picture = []
        picture.append(poipoint.picture1.name) # path 저장시 name 으로..
        picture.append(poipoint.picture2.name)
        picture.append(poipoint.picture3.name)
        picture.append(poipoint.picture4.name)
        # print(picture)
        pictures.append(picture)
    # print(pictures)

    return render(request, 'client/tripcoursedetail.html', {'citydetails':citydetails, 'current_user': current_user,
                                'travelplan':travelplan, 'travelplans':travelplans, 'locations':locations, 'pictures':pictures })

@login_required
def tripcourse_like(request, citydetails_id, tripcourse_id):
    post = get_object_or_404(TravelPlan, pk=tripcourse_id)
    # 중간자 모델 Like 를 사용하며, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다..
    post_liketp, post_liketp_created = post.liketp_set.get_or_create(user=request.user)

    if not post_liketp_created:
        post_liketp.delete()
        return redirect('/citymain/'+str(citydetails_id)+'/tripcourse/'+str(tripcourse_id))
    
    return redirect('/citymain/'+str(citydetails_id)+'/tripcourse/'+str(tripcourse_id))

def gotocity(request, citydetails_id):
    citydetails = get_object_or_404(City, pk=citydetails_id)
    current_user = request.user
    topmenuoff = True
    submenu = 1 # sub menu 진입여부
    # itdetails = InfoTravel.objects.filter(city_id=citydetails_id)

    if citydetails_id == 1: # if seoul..
        return render(request, 'client/gotocity_seoul.html', {'citydetails':citydetails, 'current_user': current_user, 'topmenuoff':topmenuoff, 'submenu':submenu })
    elif citydetails_id == 2: # if busan..
        return render(request, 'client/gotocity_busan.html', {'citydetails':citydetails, 'current_user': current_user, 'topmenuoff':topmenuoff, 'submenu':submenu })

def topbak(request, citydetails_id, partnum):
    citydetails = get_object_or_404(City, pk=citydetails_id)
    current_user = request.user
    topmenuoff = True
    submenu = 2 # sub menu 진입여부
    # itdetails = InfoTravel.objects.filter(city_id=citydetails_id)

    # 도시마다 must 구분..
    if citydetails_id == 1: # if seoul..
        itmusts = InfoTravel.objects.filter( Q(city_id=1) & Q(typeit=1) & Q(asset__isnull=False)) # tripguide 중 seoul 이고 must 이고 asset true 인것..
    elif citydetails_id == 2: # if busan..
        itmusts = InfoTravel.objects.filter( Q(city_id=2) & Q(typeit=1) & Q(asset__isnull=False))

    # print(itmusts)
    eat_itmusts = itmusts.filter(part='Eat')
    drink_itmusts = itmusts.filter(part='Drink')
    fun_itmusts = itmusts.filter(part='Fun')
    see_itmusts = itmusts.filter(part='See')
    sleep_itmusts = itmusts.filter(part='Sleep')
    buy_itmusts = itmusts.filter(part='Buy')

    if partnum == 'Eat':
        selected_itmusts = eat_itmusts
    elif partnum =='Drink':
        selected_itmusts = drink_itmusts
    elif partnum == 'Fun':
        selected_itmusts = fun_itmusts
    elif partnum == 'See':
        selected_itmusts = see_itmusts
    elif partnum == 'Sleep':
        selected_itmusts = sleep_itmusts
    elif partnum == 'Buy':
        selected_itmusts = buy_itmusts
    elif partnum == 'All':
        selected_itmusts = itmusts
    
    return render(request, 'client/topbak.html', {'citydetails':citydetails, 'current_user': current_user, 'selected_itmusts':selected_itmusts,
                                'itmusts':itmusts, 'partnum':partnum, 'topmenuoff':topmenuoff, 'submenu':submenu })

def searchlist(request, citydetails_id):
    citydetails = get_object_or_404(City, pk=citydetails_id)
    current_user = request.user
    topmenuoff = True
    itdetails = InfoTravel.objects.filter(Q(city_id=citydetails_id) & Q(asset__isnull=False))

    if request.method=='POST':
        srch = request.POST['srhwd']
        if srch:
            # 한단어만 넣어야 결과가 나옴..한 도시에서만 검색하기 위함..전체->InfoTravel.objects.filter로..
            # matchs = itdetails.filter(Q(tagko__name__icontains=srch) |
            #                                     Q(tageng__name__icontains=srch) |
            #                                     Q(tagven__name__icontains=srch)
            #                                     )

            # 여러 단어 넣으도 결과 나옴, 단 단어가 포함된 결과는 안나오고 딱! 일치한 것만..
            searchwords=srch.split(' ')
            matchs = itdetails.filter(Q(tagko__name__in=searchwords) |
                                                Q(tageng__name__in=searchwords) |
                                                Q(tagven__name__in=searchwords)
                                                ).distinct()

            print(matchs)
            if matchs:
                return render(request, 'client/searchlist.html', {'citydetails':citydetails, 
                                    'current_user':current_user, 'topmenuoff':topmenuoff, 'matchs':matchs })
            else:
                messages.error(request, 'no result found!')
        else:
            return HttpResponseRedirect('/citymain/'+citydetails_id+'/search/')

    return render(request, 'client/searchlist.html', {'citydetails':citydetails, 'current_user':current_user, 
                        'topmenuoff':topmenuoff })

def userlike(request):
    response_data = {}

    if request.method == 'GET':
        citydetails_id = request.GET['city_id']
        
        # infotravel likes..
        itcitylikes = Likeit.objects.filter(infotravel__city_id=citydetails_id) # 해당 도시의 likes
        userlikes = itcitylikes.filter(user=request.user)# 해당 도시의 likes 중 user의 likes
        # travelcurator likes..
        tccitylikes = Liketc.objects.filter(travelcurator__city_id=citydetails_id) 
        tcuserlikes = tccitylikes.filter(user=request.user)
        # travelplan likes..
        tpcitylikes = Liketp.objects.filter(travelplan__city_id=citydetails_id) 
        tpuserlikes = tpcitylikes.filter(user=request.user)

        # 방법 1..
        # userlikes_eat = userlikes.filter(infotravel__part='Eat')
        # serialized_eat = serializers.serialize('json', userlikes_eat)
        # response_data['Eat'] = userlikes_eat.count()
        # response_data['serialized_eat'] = serialized_eat
        
        # userlikes_drink = userlikes.filter(infotravel__part='Drink')
        # serialized_drink = serializers.serialize('json', userlikes_drink)
        # response_data['Drink'] = userlikes_drink.count()
        # response_data['serialized_drink'] = serialized_drink

        # userlikes_fun = userlikes.filter(infotravel__part='Fun')
        # serialized_fun = serializers.serialize('json', userlikes_fun)
        # response_data['Fun'] = userlikes_fun.count()
        # response_data['serialized_fun'] = serialized_fun

        # userlikes_see = userlikes.filter(infotravel__part='See')
        # serialized_see = serializers.serialize('json', userlikes_see)
        # response_data['See'] = userlikes_see.count()
        # response_data['serialized_see'] = serialized_see

        # userlikes_sleep = userlikes.filter(infotravel__part='Sleep')
        # serialized_sleep = serializers.serialize('json', userlikes_sleep)
        # response_data['Sleep'] = userlikes_sleep.count()
        # response_data['serialized_sleep'] = serialized_sleep

        # userlikes_buy = userlikes.filter(infotravel__part='Buy')
        # serialized_buy = serializers.serialize('json', userlikes_buy)
        # response_data['Buy'] = userlikes_buy.count()
        # response_data['serialized_buy'] = serialized_buy

        # 방법 2..
        # print(userlikes[0].infotravel_id)
        tmp = {}
        it_eat=[] 
        it_drink=[]
        it_fun=[]
        it_see=[] 
        it_sleep=[] 
        it_buy=[]
        tc_like=[]
        tp_like=[]
        it_all={}
        # infotravel like to array..
        for userlike in userlikes:
            if(userlike.infotravel.part == 'Eat'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven,
                        "part": userlike.infotravel.part
                }
                it_eat.append(tmp)
            elif(userlike.infotravel.part == 'Drink'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven,
                        "part": userlike.infotravel.part
                }
                it_drink.append(tmp)
            elif(userlike.infotravel.part == 'Fun'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven,
                        "part": userlike.infotravel.part
                }
                it_fun.append(tmp)
            elif(userlike.infotravel.part == 'See'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven,
                        "part": userlike.infotravel.part
                }
                it_see.append(tmp)
            elif(userlike.infotravel.part == 'Sleep'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven,
                        "part": userlike.infotravel.part
                }
                it_sleep.append(tmp)
            elif(userlike.infotravel.part == 'Buy'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven,
                        "part": userlike.infotravel.part
                }
                it_buy.append(tmp) 
        # travecurator like to array..
        for tcuserlike in tcuserlikes:
            tmp = {
                "id": tcuserlike.travelcurator_id,
                "titleko": tcuserlike.travelcurator.titleko,
                "titleeng": tcuserlike.travelcurator.titleeng,
                "titleven": tcuserlike.travelcurator.titleven,
                "itcount": tcuserlike.travelcurator.infotravel_count
            }
            tc_like.append(tmp)
        
        # travelplan like to array..
        for tpuserlike in tpuserlikes:
            tmp ={
                "id": tpuserlike.travelplan_id,
                "titleko": tpuserlike.travelplan.titleko,
                "titleeng": tpuserlike.travelplan.titleeng,
                "titleven": tpuserlike.travelplan.titleven,
                "course": tpuserlike.travelplan.course
            }
            tp_like.append(tmp)

        # like to json..
        it_all["Eat"] = it_eat
        it_all["Drink"] = it_drink
        it_all["Fun"] = it_fun
        it_all["See"] = it_see
        it_all["Sleep"] = it_sleep
        it_all["Buy"] = it_buy
        it_all["TClikes"] = tc_like
        it_all["TPlikes"] = tp_like

    # return JsonResponse(response_data)
    return JsonResponse(it_all)
    
def userlike_del(request):
    if request.method == 'GET':
        intype = request.GET['intype']
        if intype == 'tripguide':
            tripguide_id = request.GET['tripguide_id']
            post = get_object_or_404(InfoTravel, pk=tripguide_id)
            # 중간자 모델 Like 를 사용하며, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다..
            post_likeit, post_likeit_created = post.likeit_set.get_or_create(user=request.user)
    
            if not post_likeit_created:
                post_likeit.delete()
        if intype == 'tripcurator':
            tripcurator_id = request.GET['tripcurator_id']
            post = get_object_or_404(TravelCurator, pk=tripcurator_id)
            # 중간자 모델 Like 를 사용하며, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다..
            post_liketc, post_liketc_created = post.liketc_set.get_or_create(user=request.user)

            if not post_liketc_created:
                post_liketc.delete()
            # print(intype)
        if intype == 'tripcourse':
            tripcourse_id = request.GET['tripcourse_id']
            post = get_object_or_404(TravelPlan, pk=tripcourse_id)
            # 중간자 모델 Like 를 사용하며, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다..
            post_liketp, post_liketp_created = post.liketp_set.get_or_create(user=request.user)

            if not post_liketp_created:
                post_liketp.delete()
            # print(intype)

    # print(tripguide_id)

    return HttpResponse('success!')

# def tophund(request, citydetails_id, partnum):
#     citydetails = get_object_or_404(City, pk=citydetails_id)
#     current_user = request.user
#     # itdetails = InfoTravel.objects.filter(city_id=citydetails_id)
     
#     return render(request, 'client/topbak.html', {'citydetails':citydetails, 'current_user': current_user, 'partnum':partnum })


# @login_required
# def post_like(request, blog_id):
#     post = get_object_or_404(Blog, pk=blog_id)
#     # 중간자 모델 Like 를 사용하며, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다..
#     post_like, post_like_created = post.like_set.get_or_create(user=request.user)

#     if not post_like_created:
#         post_like.delete()
#         return redirect('/blog/'+str(post.id))
#     return redirect('/blog/'+str(post.id))



def cmain(request):
    pois = POIpoint.objects.all()  # Getting all the POI from database
    return render(request, 'client/cmain.html', { 'pois': pois })

def likePOI(request):
    if request.method == 'GET':
        poi_id = request.GET['poi_id']
        print(poi_id)
        num = int(poi_id)
        pois = POIpoint.objects.all()
        print(pois[num])

        # likedpoi = POIpoint.obejcts(pk=poi_id) #getting the liked pois
        # m = Like(post=likedpost) # Creating Like Object
        # m.save()  # saving it to store in database
        # return HttpResponse(pois[num]) # Sending an success response
        return render(request, 'client/cmain.html', { 'poisnum': pois[num] })
    else:
        return HttpResponse("Request method is not a GET")
