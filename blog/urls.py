from django.urls import path,include
from . import views 

urlpatterns = [
  path('',views.Home,name='home'),
  path('<int:id>/',views.PostDetail,name='detail')
]
