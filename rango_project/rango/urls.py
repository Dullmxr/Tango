from django.urls import path # type: ignore
from rango import views 

urlpatterns = [
    path('', views.index, name='index'),  
]
