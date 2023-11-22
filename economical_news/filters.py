import django_filters
from .models import News

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    # Добавьте другие поля фильтра здесь

    class Meta:
        model = News
        fields = ['title', 'author', 'date']
