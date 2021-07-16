from django.urls import path
from polls import views

urlpatterns=[
    path('',views.initial,name="initial"),
    path('home/',views.index,name="home"),
    path('play/<int:id>/',views.play,name="play")
]