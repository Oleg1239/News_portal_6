# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('economical_news.urls')),  # Включите URL-адреса вашего приложения
]
