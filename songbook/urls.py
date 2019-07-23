from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('song/new/', views.song_new, name='song_new'),
    path('song/<int:pk>/edit/', views.song_edit, name='song_edit'),
    path('drafts/', views.song_draft_list, name='song_draft_list'),
    path('song/<pk>/publish/', views.song_publish, name='song_publish'),
    path('song/<pk>/remove/', views.song_remove, name='song_remove'),
]