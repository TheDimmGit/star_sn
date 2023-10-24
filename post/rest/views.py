from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Like, Post
from post.rest.filters import PostFilter
from post.rest.serializers import PostSerializer


class GenericViewSet(viewsets.ModelViewSet):
    """
    Overrides rest_framework.viewsets.GenericViewSet
    to support different classes for serialization and deserialization.
    """
    permission_classes = (IsAuthenticated,)
    request_serializer_class = None
    response_serializer_class = None

    def get_request_serializer_class(self):
        if self.request_serializer_class:
            return self.request_serializer_class
        return self.response_serializer_class

    def get_response_serializer_class(self):
        return self.response_serializer_class

    def get_request_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        that should be used for validating and
        deserializing input
        """

        serializer_class = self.get_request_serializer_class()
        assert serializer_class is not None, (
            "'%s' should either include a `request_serializer_class`"
            " attribute, or override the `get_request_serializer_class()`"
            " method."
            % self.__class__.__name__
        )
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_response_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        that should be used for serializing output
        """

        serializer_class = self.get_response_serializer_class()
        assert serializer_class is not None, (
            "'%s' should either include a `response_serializer_class`"
            " attribute, or override the `get_response_serializer_class()`"
            " method."
            % self.__class__.__name__
        )
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        return self.get_request_serializer(*args, **kwargs)


class PostView(GenericViewSet):
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = PostFilter
    request_serializer_class = PostSerializer
    response_serializer_class = PostSerializer
    queryset = Post.objects.all()
    ordering = '-id'

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['author'] = request.user.id
        request_serializer = self.get_request_serializer(data=data)
        request_serializer.is_valid(raise_exception=True)
        instance = request_serializer.save()
        response_serializer = self.get_response_serializer(instance)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], url_path='like', detail=True)
    def like_post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user.id
        like = Like.objects.filter(post=post, author=user)
        if like.exists():
            like.first().delete()
        else:
            Like.objects.create(post=post, author_id=user)

        return Response(status=status.HTTP_200_OK)


class AnalyticsView(APIView):

    def get(self, request):
        # Такое лучше сделать через django-filter (как для постов),
        # но в данном случае фильровать кверисет лайков будет странно,
        # потому что мы не возвращаем инстансы лайков.

        try:
            date_from = request.GET.get('date_from', datetime.now() - timedelta(days=7))
            date_to = request.GET.get('date_to', datetime.now())

            likes = Like.objects.filter(date__range=[date_from, date_to]).count()
            posts = Post.objects.filter(date__range=[date_from, date_to]).count()
            result = {
                'total_likes': likes,
                'total_posts': posts
            }
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'error_message': 'Invalid date'}, status=status.HTTP_400_BAD_REQUEST)
