from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import random

from django.http import HttpResponse
from backendapp.travels.models import POIpoint, City, InfoTravel, TravelCurator, TravelPlan
from backendapp.arcontent.models import ARTrip

def chome(request):
    citys = City.objects.filter().order_by('id') # 순차적으로 불러오기..
    current_user = request.user
    return render(request, 'client/cindex.html', {'citys': citys ,'current_user': current_user})

def citymain(request, city_id):
    citydetails = get_object_or_404(City, pk=city_id)
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
    
    return render(request, 'client/citydetail.html', {'citydetails':citydetails, 'itdetails':itdetails, 'arcontents':arcontents,
            'eat_itdetail':eat_itdetail, 'drink_itdetail':drink_itdetail, 'fun_itdetail':fun_itdetail, 'see_itdetail':see_itdetail, 
            'sleep_itdetail':sleep_itdetail, 'buy_itdetail':buy_itdetail })

def tripguide(request, citydetails_id, partnum):
    itdetails = InfoTravel.objects.filter(city_id=citydetails_id)
    city = City.objects.get(id=citydetails_id)
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

    return render(request, 'client/tripguide.html', {'city':city, 'citydetails_id':citydetails_id, 'partnum':partnum, 
                            'selected_itdetails':selected_itdetails})

def tripguidedetail(request, citydetails_id, partnum, tripguide_id):
    itdetails = InfoTravel.objects.filter(city_id=citydetails_id)
    itdetail = InfoTravel.objects.get(id=tripguide_id)
    # print(itdetail.itlocation[0])
    return render(request, 'client/tripguidedetail.html', {'citydetails_id':citydetails_id, 'itdetails':itdetails, 'partnum':partnum, 
                        'itdetail':itdetail})
 


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
