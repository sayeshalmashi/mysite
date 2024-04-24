from django import template
from blog.models import Post,Category,Comment
from django.utils import timezone
register =template.Library()
@register.simple_tag(name='post')
def function():
  posts=Post.objects.filter(status=1).count()
  return posts

@register.simple_tag(name='comments_count')
def function(pid):
  return Comment.objects.filter(post=pid,approved=True).count()

@register.filter
def snippet(value,arg=20):
  return value[:arg] + '...'

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
  current_time=timezone.now()
  posts=Post.objects.filter(status=1,published_date__lte=current_time).order_by('-published_date')[:arg]
  return {'posts':posts}

@register.inclusion_tag('blog/blog-post-category.html')
def postcategory():
  current_time=timezone.now()
  posts=Post.objects.filter(status=1,published_date__lte=current_time)
  categories=Category.objects.all()
  cat_dict={}
  for name in categories:
    cat_dict[name]=posts.filter(category=name).count()
  return {'categories':cat_dict}