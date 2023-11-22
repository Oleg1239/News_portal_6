# economical_news/urls.py
from django.urls import path
from .views import home, author_list, post_list, category_list, post_category_list, comment_list, NewsListView, NewsDetailView, search_news, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('authors/', author_list, name='author_list'),
    path('posts/', post_list, name='post_list'),
    path('categories/', category_list, name='category_list'),
    path('post_categories/', post_category_list, name='post_category_list'),
    path('comments/', comment_list, name='comment_list'),
    path('contact/', contact_view, name='contact'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/search/', search_news, name='search_news'),
    # Другие маршруты внутри приложения...
]
