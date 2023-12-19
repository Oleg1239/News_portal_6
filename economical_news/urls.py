from django.urls import path
from .views import (
    home, author_list, post_list, category_list, post_category_list,
    comment_list, NewsListView, NewsDetailView, search_news, contact_view,
    RegisterView, BecomeAuthorView  # Добавьте BecomeAuthorView
)
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

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
    path('login/', LoginView.as_view(template_name='economical_news/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('become_author/', BecomeAuthorView.as_view(), name='become_author'),  # Новый путь для становления автором
    path('accounts/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # Другие URL-пути...
]
