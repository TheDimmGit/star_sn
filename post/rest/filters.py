from datetime import datetime

import django_filters

from post.models import Post


class PostFilter(django_filters.FilterSet):
    date_from = django_filters.CharFilter(help_text='YYYY-MM-DD', method='filter_date_from')
    date_to = django_filters.CharFilter(help_text='YYYY-MM-DD', method='filter_date_to')

    def filter_date_from(self, queryset, name, value):
        try:
            value = datetime.strptime(value, '%Y-%m-%d')
            return queryset.filter(date__gte=value)
        except ValueError:
            return queryset.none()

    def filter_date_to(self, queryset, name, value):
        try:
            value = datetime.strptime(value, '%Y-%m-%d')
            return queryset.filter(date__lte=value)
        except ValueError:
            return queryset.none()

    class Meta:
        model = Post
        fields = ['date_from', 'date_to']
