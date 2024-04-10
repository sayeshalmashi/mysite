from django import template
from blog.models import Post
register =template.Library()
@register.simple_tag(name='post')
def function():
  posts=Post.objects.filter(status=1).count()
  return posts

@register.filter
def snippet(value,arg=20):
  return value[:arg] + '...'