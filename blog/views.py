from django.shortcuts import render
from .models import *

# Create your views here.


def Home(request):
  featured_post = Post.objects.all().filter(featured_post=True)[:1]
  posts = Post.objects.all()
  context = {'posts':posts,'featured_post':featured_post}
  return render(request,'blog/index.html',context)



def PostDetail(request, id):
  post = Post.objects.get(id=id)
  context = {'post':post}

  return render(request,'blog/detail.html',context)
