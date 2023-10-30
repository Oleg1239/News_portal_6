from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Category, Post, PostCategory, Comment, News
from django.views.generic.detail import DetailView

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

# Class-based view for News model
class NewsListView(ListView):
    model = News
    template_name = 'flatpages/default.html'  # путь к шаблону default.html
    context_object_name = 'news_items'  # имя переменной в контексте
    ordering = ['-date']  # сортировка новостей по дате

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_items'] = News.objects.all().order_by('-date')
        return context

def contact_view(request):
    return render(request, 'economical_news/contact.html')

class NewsDetailView(DetailView):
    model = News
    template_name = 'flatpages/default.html'
    context_object_name = 'news_item'



