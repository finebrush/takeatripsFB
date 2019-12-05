from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     nickname = models.TextField(max_length=10)

#     like_posts = models.ManyToManyField('Post', blank=True, related_name='like_users')

#     def __str__(self):
#         return self.nickname

# class Post(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     title = models.CharField(max_length=30)
#     content = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)

#     like_count = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         return self.title

# class Blog(models.Model):
#     objects = models.Manager()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     pub_date = models.DateTimeField('date published')
#     body = models.TextField()
#     like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_user_set', through='Like')

#     @property
#     # get method 표현..
#     def like_count(self):
#         return self.like_user_set.count()

#     def __str__(self):
#         return self.title

# class Like(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         unique_together = (('user', 'blog'),)

