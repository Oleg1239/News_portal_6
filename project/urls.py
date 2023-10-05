from django.urls import path
from economical_news import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.author_list, name='author_list'),
    path('posts/', views.post_list, name='post_list'),
    path('categories/', views.category_list, name='category_list'),
    path('post_categories/', views.post_category_list, name='post_category_list'),
    path('comments/', views.comment_list, name='comment_list'),
    path('admin/', admin.site.urls),
]


