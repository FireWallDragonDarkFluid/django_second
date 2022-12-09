from django.urls import path 

from . import views 

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('forest', views.forest, name='forest'),
    path('lassocv', views.lassocv, name='lassocv'), 
    path('about', views.about, name='about'), 
    path('search', views.search, name='search')
]