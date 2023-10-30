from economical_news import views
from django.contrib import admin
from economical_news.views import contact_view
from economical_news.views import NewsListView, NewsDetailView
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.author_list, name='author_list'),
    path('posts/', views.post_list, name='post_list'),
    path('categories/', views.category_list, name='category_list'),
    path('post_categories/', views.post_category_list, name='post_category_list'),
    path('comments/', views.comment_list, name='comment_list'),
    # path('news/', include('economical_news.urls')),
    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_details'),
    path('economical_news/', include('economical_news.urls')),  # включение URLs из вашего приложения
    # другие пути...
]



