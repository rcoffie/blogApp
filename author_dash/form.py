from  django.forms import ModelForm
from blog .models import  *

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ['title','body','category','blog_image']