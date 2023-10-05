from django.shortcuts import render
from .models import Author, Category, Post, PostCategory, Comment
from django.shortcuts import render

def home(request):
    # Ваш код для главной страницы здесь
    return render(request, 'economical_news/base.html')
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'news/author_list.html', {'authors': authors})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'news/post_list.html', {'posts': posts})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'news/category_list.html', {'categories': categories})

def post_category_list(request):
    post_categories = PostCategory.objects.all()
    return render(request, 'news/post_category_list.html', {'post_categories': post_categories})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'news/comment_list.html', {'comments': comments})
