from django.contrib import admin
from blog.models import Post, Category
# # Register your models here.

class PostAdmin(admin.ModelAdmin):
  date_hierarchy='creat_date'
  empty_value_display='-empty-'
  list_display=('title','author','count_views','status','published_date','creat_date')
  list_filter=('status','author',) #topple akharesh ,
  ordering=['-creat_date']
  search_fields=['title','content']
  # in taghirat va filter ha faghat zaman namyesg anjam mishavad va dar database in filter ha anjam nmishe age mikhy in filtera dar database anjam beshe dar class meta dakhel model ina ro benevis.

admin.site.register(Category)
admin.site.register(Post,PostAdmin)