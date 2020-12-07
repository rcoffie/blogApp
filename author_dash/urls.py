from django.urls import path,include
from . import views 

urlpatterns = [
 path('',views.Home,name='author_dash'),
 path('create/',views.BlogPost,name='create'),
 path('update/<str:id>/',views.EditPost,name='update'),
 path('delete/<int:id>/',views.DeletePost,name='delete'),
]
