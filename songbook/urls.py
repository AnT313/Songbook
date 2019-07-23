from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
]