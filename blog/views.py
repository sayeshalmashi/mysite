from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request):
  return render(request,'blog/blog-home.html')

def blog_single(request):
  # post= get_object_or_404(Post,pk=pid)
  # context={'post':post}
  return render(request,'blog/blog-single.html')

# def test_views(request):
#   current_time= timezone.now()
#   filtered_post= Post.objects.filter(published_date__lte=current_time)
#   for post in filtered_post:
#     post.count_views+=1
#     post.save()
#   context={'published':filtered_post}
#   return render(request,'test.html',context)