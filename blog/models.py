from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from taggit.managers import TaggableManager
# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=255)
  def __str__(self):
    return self.name

class Post(models.Model):
  title=models.CharField(max_length=255)
  content=models.TextField()
  author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
  # tags=TaggableManager()
  category=models.ManyToManyField(Category)
  count_views=models.IntegerField(default=0)
  status=models.BooleanField(default=False)
  login_require=models.BooleanField(default=False)
  published_date=models.DateTimeField(null=True)
  creat_date=models.DateField(auto_now_add=True)
  update_date=models.DateField(auto_now=True)
  
  class Meta:
    ordering=['-creat_date']
    #verbose_name='پست'
  
  def __str__(self):
    return "{}-{}".format(self.title,self.id)
  def get_absolute_url(self):
    return reverse('blog:single',kwargs={'pid':self.id})
  
class Comment(models.Model):
  post=models.ForeignKey(Post,on_delete=models.CASCADE)
  name=models.CharField(max_length=255)
  email=models.EmailField()
  subject=models.CharField(max_length=255)
  message=models.TextField()
  approved=models.BooleanField(default=False)
  created_date=models.DateTimeField(auto_now_add=True)
  updated_date=models.DateTimeField(auto_now=True)
  class Meta:
    ordering=['-created_date']
    
  def __str__(self):
     return self.name
  