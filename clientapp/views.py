from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import *
from django.core import serializers
import random
from django.utils import translation

from django.http import HttpResponse
from backendapp.travels.models import POIpoint, City, InfoTravel, Likeit, TravelCurator, Liketc, TCImage, TravelPlan, Liketp, POIpoint
from backendapp.arcontent.models import ARTrip

def chome(request):
    citys = City.objects.filter().order_by('id') # 순차적으로 불러오기..
    current_user = request.user
    topmenuoff = False # 상단 메뉴가 display none..
    
    return render(request, 'client/cindex.html', {'citys': citys , 'current_user': current_user, 'topmenuoff':topmenuoff})

def citymain(request, city_id):
    citydetails = get_object_or_404(City, pk=city_id)
    current_user = request.user
    topmenuoff = True
    itdetails = InfoTravel.objects.filter(city_id=city_id)
    artrips = ARTrip.objects.filter(share=True)
    arcontents = artrips.random(8)

    # InfoTravel 에서 part 별 랜덤한 하나의 DB를 전달..
    eat_itdetail = itdetails.filter(part='Eat').first()
    drink_itdetail = itdetails.filter(part='Drink').first()
    fun_itdetail = itdetails.filter(part='Fun').first()
    see_itdetail = itdetails.filter(part='See').first()
    sleep_itdetail = itdetails.filter(part='Sleep').first()
    buy_itdetail = itdetails.filter(part='Buy').first()
    
    return render(request, 'client/citydetail.html', {'citydetails':citydetails, 'current_user': current_user, 'itdetails':itdetails, 'arcontents':arcontents,
            'eat_itdetail':eat_itdetail, 'drink_itdetail':drink_itdetail, 'fun_itdetail':fun_itdetail, 'see_itdetail':see_itdetail, 
            'sleep_itdetail':sleep_itdetail, 'buy_itdetail':buy_itdetail, 'topmenuoff':topmenuoff })

def tripguide(request, citydetails_id, partnum):
    citydetails = City.objects.get(id=citydetails_id)
    current_user = request.user
    topmenuoff = True
    itdetails = InfoTravel.objects.filter(city_id=citydetails_id)
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
    itdetails = InfoTravel.objects.filter(city_id=citydetails_id)
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
    searchlists = InfoTravel.objects.filter(tagko__name__in=searchwords).distinct()
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
    # itdetails = InfoTravel.objects.filter(city_id=citydetails_id)

    if citydetails_id == 1:
        return render(request, 'client/gotocity_seoul.html', {'citydetails':citydetails, 'current_user': current_user, 'topmenuoff':topmenuoff })
    elif citydetails_id == 2:
        return render(request, 'client/gotocity_busan.html', {'citydetails':citydetails, 'current_user': current_user, 'topmenuoff':topmenuoff })

def topbak(request, citydetails_id, partnum):
    citydetails = get_object_or_404(City, pk=citydetails_id)
    current_user = request.user
    topmenuoff = True
    # itdetails = InfoTravel.objects.filter(city_id=citydetails_id)
    itmusts = InfoTravel.objects.filter(typeit=1) # tripguide 중 must 인것..
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
                                'itmusts':itmusts, 'partnum':partnum, 'topmenuoff':topmenuoff })

def searchlist(request, citydetails_id):
    citydetails = get_object_or_404(City, pk=citydetails_id)
    current_user = request.user
    topmenuoff = True
    itdetails = InfoTravel.objects.filter(city_id=citydetails_id)

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
                        "companyven": userlike.infotravel.companyven
                }
                it_eat.append(tmp)
            elif(userlike.infotravel.part == 'Drink'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven
                }
                it_drink.append(tmp)
            elif(userlike.infotravel.part == 'Fun'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven
                }
                it_fun.append(tmp)
            elif(userlike.infotravel.part == 'See'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven
                }
                it_see.append(tmp)
            elif(userlike.infotravel.part == 'Sleep'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven
                }
                it_sleep.append(tmp)
            elif(userlike.infotravel.part == 'Buy'):
                tmp = { 
                        "id": userlike.infotravel_id,
                        "companyko": userlike.infotravel.companyko,
                        "companyeng": userlike.infotravel.companyeng,
                        "companyven": userlike.infotravel.companyven
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
