from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from datetime import datetime 
# Create your models here.


class Post(models.Model):
  Category=(
    ('Electronics','Electronics'),
    ('LifeStyle','LifeStyle'),
    ('Fashion','Fashion'),
    ('Technology','Technology')
  )
  Status=(
    ('Draft','Draft'),
    ('Published','Published')
  )


  title = models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  category = models.CharField(max_length=100,choices=Category,null=True)
  body = models.TextField()
  featured_post = models.BooleanField(default=False)
  # status = models.CharField(max_length=100,choices=Status)
  blog_image = models.ImageField(upload_to='photos/%Y/%m/%d')
  date_posted = models.DateField(default=datetime.now)



  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-date_posted']