from django.shortcuts import render

from django.http import HttpResponse
from demo.cities.models import POIpoint

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
