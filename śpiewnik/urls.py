from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('songbook.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login')

]