from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages

def blog_view(request,**kwargs):
  current_time=timezone.now()
  posts=Post.objects.filter(status=1,published_date__lte=current_time).order_by('-id')
  if kwargs.get('cat_name')!=None:
    posts=posts.filter(status=1,category__name=kwargs['cat_name'])
  if kwargs.get('author_username')!=None:
    posts=posts.filter(status=1,author__username=kwargs['author_username'])
  if kwargs.get('tag_name')!=None:
     posts=posts.filter(status=1,tags__name__in=[kwargs['tag_name']])
  posts=Paginator(posts,3)
  try:
    page_number=request.GET.get('page')
    posts=posts.get_page(page_number)
  except PageNotAnInteger:
    return render(request,'path-to-your-404-template.html')
  except EmptyPage:
    posts=posts.get_page(1)
    
  context={'posts':posts}
  return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      form.save()
      success_message = "you'r commet submited successfully"
      messages.add_message(request, messages.SUCCESS, success_message)
    else:
      error_message = "you'r comment didnt submited"
      messages.add_message(request, messages.ERROR, error_message)
  current_time=timezone.now()
  posts=Post.objects.filter(status=1,published_date__lte=current_time)
  post=get_object_or_404(posts, pk=pid)
  prev_post=Post.objects.filter(pk__lt=post.id,status=1,published_date__lte=current_time).order_by('-pk').first()
  next_post=Post.objects.filter(pk__gt=post.id,status=1,published_date__lte=current_time).order_by('pk').first()
  post.count_views+=1
  post.save()
  comments=Comment.objects.filter(post=post.id,approved=True)
  form=CommentForm()
  
  context={'post':post,'prev_post':prev_post,'next_post':next_post,'comments':comments,'form':form}
  return render(request,'blog/blog-single.html',context)

def blog_category(request,cat_name):
  posts=Post.objects.filter(status=1,category__name=cat_name)
  context={'posts':posts}
  return render(request,'blog/blog-home.html',context)

def blog_search(request):
  current_time=timezone.now()
  posts=Post.objects.filter(status=1,published_date__lte=current_time).order_by('-id')
  if request.method=='GET':
    if s:= request.GET.get('s'): # agar request.GET.get('s') ro rikhte toye s
      posts=posts.filter(content__contains=s)
  context={'posts':posts}
  return render(request,'blog/blog-home.html',context)