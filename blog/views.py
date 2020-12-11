from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse
# Create your views here.


def Home(request):
  featured_post = Post.objects.all().filter(featured_post=True)[:1]
  posts_list = Post.objects.all()
  paginator = Paginator(posts_list,6)
  query = request.GET.get('q')
  if query:
    posts_list=Post.objects.all().filter(
      Q(title__icontains=query)|
      Q(body__icontains=query)
    
    )
  page_number = request.GET.get('page')
  posts = paginator.get_page(page_number)
  context = {'posts':posts,'featured_post':featured_post}
  return render(request,'blog/index.html',context)




def PostDetail(request, id):
  post = Post.objects.get(id=id)
  comments = Comment.objects.filter(post=post)
  if request.method== 'POST':
    name = request.POST['name']
    content = request.POST['content']
    comment = Comment.objects.create(name=name,content=content , post=post)
    comment.save()
    return HttpResponseRedirect(reverse('detail', args=[post.id]))
    

  context = {'post':post,'comments':comments}

  return render(request,'blog/detail.html',context)