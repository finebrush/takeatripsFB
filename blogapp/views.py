from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Blog
	
def home(request):
    blogs = Blog.objects
    current_user = request.user
    return render(request, 'client/blog/home.html', {'blogs': blogs, 'current_user': current_user})

def detail(request, blog_id): 
	details = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'client/blog/detail.html', {'details':details})

def new(request):
    if request.user.is_authenticated: 
        #로그인 한 상태라면 new포스트 html로 보내기.
        return render(request, 'client/blog/new.html')
    else:
        #회원정보가 존재하지 않는다면, 에러인자와 함께 home 템플릿으로 돌아가기.     
        blogs = Blog.objects
        return render(request, 'client/blog/home.html', {'blogs': blogs, 'error': 'You have to login to make newpost'})
    return render(request, 'client/blog/new.html')

def create(request):
    blog = Blog()
    blog.author = request.user
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) 

def delete(request, blog_id):
    destroy = get_object_or_404(Blog, pk=blog_id)
    destroy.delete()
    return redirect('blogapp:home')

def update(request, blog_id):
    updates= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'client/blog/update.html', {'updates': updates})

def edit(request, blog_id):
    edit = Blog.objects.get(pk=blog_id)
    edit.title = request.POST['title']
    edit.body = request.POST['body']
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('blogapp:home')

@login_required
def post_like(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    # 중간자 모델 Like 를 사용하며, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다..
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        return redirect('/blog/'+str(post.id))
    return redirect('/blog/'+str(post.id))