from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from .models import Author, Category, Post, PostCategory, Comment, News
from .filters import NewsFilter
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import Category
from .models import PostCategory
from .models import Comment

# Оставшиеся функции представлений не изменены...
def home(request):
    return render(request, 'economical_news/base.html')

# ...

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
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

class NewsDetailView(DetailView):
    model = News
    template_name = 'economical_news/news_detail.html'
    context_object_name = 'news_item'

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'economical_news/registration/registration.html'

def contact_view(request):
    return render(request, 'economical_news/contact.html')

def search_news(request):
    news_filter = NewsFilter(request.GET, queryset=News.objects.all())
    return render(request, 'economical_news/search_results.html', {'filter': news_filter})

# Новая функция представления для добавления пользователя в группу authors
class BecomeAuthorView(View):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='authors')
        if not request.user.groups.filter(name='authors').exists():
            request.user.groups.add(group)
            messages.success(request, "Вы теперь автор!")
        else:
            messages.info(request, "Вы уже являетесь автором.")
        return redirect('home')
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'news/author_list.html', {'authors': authors})

def post_list(request):
    posts = Post.objects.all()  # Получаем все объекты Post из базы данных
    return render(request, 'economical_news/post_list.html', {'posts': posts})

def category_list(request):
    categories = Category.objects.all()  # Получаем все объекты Category из базы данных
    return render(request, 'economical_news/category_list.html', {'categories': categories})

def post_category_list(request):
    post_categories = PostCategory.objects.all()  # Получаем все категории постов
    return render(request, 'economical_news/post_category_list.html', {'post_categories': post_categories})

def comment_list(request):
    comments = Comment.objects.all()  # Получаем все комментарии
    return render(request, 'economical_news/comment_list.html', {'comments': comments})
