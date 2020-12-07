from django.shortcuts import render,redirect,get_object_or_404
from . import views 
from .form import *
from blog.models import *

# Create your views here.

def Home(request):
  posts = Post.objects.all().filter(author=request.user)
  
  if request.method == 'POST':
    form = PostForm(request.POST,request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('author_dash')
  form = PostForm()
  context = {'form':form,'posts':posts}
  return render(request,'author/index.html',context)



def BlogPost(request):
  form = PostForm()

  context = {'form':form}

  return render(request,'author/create.html',context)



def EditPost(request, id):
  posts = Post.objects.all().filter(author=request.user)
  post = get_object_or_404(Post, id=id)
  updateForm = PostForm(request.POST or None, instance=post)
  if updateForm.is_valid():
    updateForm.save()
    return redirect('author_dash')
  
  context = {'updateForm':updateForm,'posts':posts}

  return render(request,'author/update.html',context)


def DeletePost(request, id):
  post = Post.objects.get(id=id)
  post.delete()
  return redirect('author_dash')