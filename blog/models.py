from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
  title=models.CharField(max_length=255)
  content=models.TextField()
  author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  #image
  # tag
  # category
  count_views=models.IntegerField(default=0)
  status=models.BooleanField(default=False)
  published_date=models.DateField(null=True)
  creat_date=models.DateField(auto_now_add=True)
  update_date=models.DateField(auto_now=True)
  
  class Meta:
    ordering=['-creat_date']
    #verbose_name='پست'
  
  def __str__(self):
    return "{}-{}".format(self.title,self.id)