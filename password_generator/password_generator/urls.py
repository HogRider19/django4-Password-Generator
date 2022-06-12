from django.contrib import admin
from django.urls import path, include
from generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('password/', views.password, name = 'password'),
    path('information/', views.information, name = 'information')
]
