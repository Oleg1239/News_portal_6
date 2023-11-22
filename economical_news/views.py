from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Category, Post, PostCategory, Comment, News
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.db.models import Q
from django_filters.views import FilterView
from .filters import NewsFilter

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
    template_name = 'news/news_list.html'  # Обновленный путь к шаблону
    context_object_name = 'news_items'
    ordering = ['-date']
    paginate_by = 10
    filterset_class = NewsFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )
        return queryset

def contact_view(request):
    return render(request, 'economical_news/contact.html')

class NewsDetailView(DetailView):
    model = News
    template_name = 'economical_news/news_detail.html'  # Обновленный путь к шаблону
    context_object_name = 'news_item'

# Функция поиска новостей
def search_news(request):
    news_filter = NewsFilter(request.GET, queryset=News.objects.all())
    return render(request, 'economical_news/search_results.html', {'filter': news_filter})
