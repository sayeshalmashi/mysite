from django.contrib import admin
from blog.models import Post, Category,Comment
from django_summernote.admin import SummernoteModelAdmin
# # Register your models here.

class PostAdmin(SummernoteModelAdmin):
  date_hierarchy='creat_date'
  empty_value_display='-empty-'
  list_display=('title','author','count_views','status','published_date','creat_date','login_require')
  list_filter=('status','author',) #topple akharesh ,
  ordering=['-creat_date']
  search_fields=['title','content']
  # in taghirat va filter ha faghat zaman namyesh anjam mishavad va dar database in filter ha anjam nmishe age mikhy in filtera dar database anjam beshe dar class meta dakhel model ina ro benevis.
  summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
  date_hierarchy='created_date'
  empty_value_display='-empty-'
  list_display=('name','post','approved','created_date')
  list_filter=('post','approved',) #topple akharesh ,
  ordering=['-created_date']
  search_fields=['name','post']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)