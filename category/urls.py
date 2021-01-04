from django.urls import path,include
from . import views 

urlpatterns = [
 path('electronics',views.Electronics,name='electronics'),
 path('lifestyle',views.LifeStyle,name='lifestyle'),
 path('fashion',views.Fashion,name='fashion'),
 path('technology',views.Technology,name='technology')
]
