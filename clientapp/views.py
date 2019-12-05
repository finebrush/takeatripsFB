from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from backendapp.travels.models import POIpoint
# from .models import Blog


# def home(request):
#     blogs = Blog.objects
#     current_user = request.user
#     return render(request, 'home.html', {'blogs':blogs, 'current_user': current_user})

# def detail(request, blog_id):
#     details = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'detail.html', {'details':details})

# def new(request):

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
