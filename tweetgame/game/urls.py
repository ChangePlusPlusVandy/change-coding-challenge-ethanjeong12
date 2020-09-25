from django.urls import path
from game import views

urlpatterns = [
    path('/display', views.index),
    path('/end', views.result)
    #path('/new', views.post, name='post') 
]
