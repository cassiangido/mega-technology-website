from django.urls import path
from . import views


urlpatterns = [
    path('base/', views.base, name='base'),
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('careers/', views.careers, name='careers'),

]
