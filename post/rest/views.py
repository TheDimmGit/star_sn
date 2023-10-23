from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from post.models import Post
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
