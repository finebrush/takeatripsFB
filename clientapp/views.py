from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import random

from django.http import HttpResponse
from backendapp.travels.models import POIpoint, City, InfoTravel, Likeit, TravelCurator, Liketc, TCImage, TravelPlan, POIpoint
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

    if partnum == 1:
        selected_itdetails = eat_itdetails
    elif partnum ==2:
        selected_itdetails = drink_itdetails
    elif partnum == 3:
        selected_itdetails = fun_itdetails
    elif partnum == 4:
        selected_itdetails = see_itdetails
    elif partnum == 5:
        selected_itdetails = sleep_itdetails
    elif partnum == 6:
        selected_itdetails = buy_itdetails
    elif partnum == 0:
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
    itmusts = InfoTravel.objects.filter(typeit=1)
    # print(itmusts)
    eat_itmusts = itmusts.filter(part='Eat')
    drink_itmusts = itmusts.filter(part='Drink')
    fun_itmusts = itmusts.filter(part='Fun')
    see_itmusts = itmusts.filter(part='See')
    sleep_itmusts = itmusts.filter(part='Sleep')
    buy_itmusts = itmusts.filter(part='Buy')

    if partnum == 1:
        selected_itmusts = eat_itmusts
    elif partnum ==2:
        selected_itmusts = drink_itmusts
    elif partnum == 3:
        selected_itmusts = fun_itmusts
    elif partnum == 4:
        selected_itmusts = see_itmusts
    elif partnum == 5:
        selected_itmusts = sleep_itmusts
    elif partnum == 6:
        selected_itmusts = buy_itmusts
    elif partnum == 0:
        selected_itmusts = itmusts
    
    return render(request, 'client/topbak.html', {'citydetails':citydetails, 'current_user': current_user, 'selected_itmusts':selected_itmusts,
                                'itmusts':itmusts, 'partnum':partnum, 'topmenuoff':topmenuoff })
    
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
