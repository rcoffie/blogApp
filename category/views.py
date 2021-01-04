from django.shortcuts import render,redirect
from blog.models import *

# Create your views here.


def Electronics(request):
  posts = Post.objects.filter(category='Electronics')
  context = {'posts':posts}

  return render(request,'category/electronic.html',context)



def LifeStyle(request):
  posts = Post.objects.filter(category='LifeStyle')
  context = {'posts':posts}

  return render(request,'category/lifestyle.html',context)



def Fashion(request):
  posts = Post.objects.filter(category='Fashion')
  context = {'posts':posts}

  return render(request,'category/fashion.html',context)




def Technology(request):
  posts = Post.objects.filter(category='Technology')
  context = {'posts':posts}

  return render(request,'category/technology.html',context)







