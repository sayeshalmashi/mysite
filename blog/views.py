from django.shortcuts import render,get_object_or_404

from blog.models import Post
from django.utils import timezone

def blog_view(request,**kwargs):
  current_time=timezone.now()
  posts=Post.objects.filter(status=1,published_date__lte=current_time).order_by('-id')
  if kwargs.get('cat_name')!=None:
    posts=Post.objects.filter(status=1,category__name=kwargs['cat_name'])
  if kwargs.get('author_username')!=None:
    posts=Post.objects.filter(status=1,author__username=kwargs['author_username'])
  context={'posts':posts}
  return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
  current_time=timezone.now()
  posts=Post.objects.filter(status=1,published_date__lte=current_time)
  post=get_object_or_404(posts, pk=pid)
  prev_post=Post.objects.filter(pk__lt=post.id,status=1,published_date__lte=current_time).order_by('-pk').first()
  next_post=Post.objects.filter(pk__gt=post.id,status=1,published_date__lte=current_time).order_by('pk').first()
  post.count_views+=1
  post.save()
  context={'post':post,'prev_post':prev_post,'next_post':next_post}
  return render(request,'blog/blog-single.html',context)

def blog_category(request,cat_name):
  posts=Post.objects.filter(status=1,category__name=cat_name)
  context={'posts':posts}
  return render(request,'blog/blog-home.html',context)
