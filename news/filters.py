import django_filters
from .models import Post
from django.forms import DateInput

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    author__user__username = django_filters.CharFilter(lookup_expr='icontains', label='Author')
    created_at = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}), label='Published After')

    class Meta:
        model = Post
        fields = ['title', 'author__user__username', 'created_at']
