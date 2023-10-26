from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from post.rest.views import GenericViewSet
from user.models import User
from user.rest.serializers import UserRequestSerializer, UserResponseSerializer


class UserCreate(GenericViewSet):
    request_serializer_class = UserRequestSerializer
    response_serializer_class = UserResponseSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )

    @action(methods=['get'], url_path='detail', detail=True)
    def user_detail(self, request, *args, **kwargs):
        serializer = self.get_response_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)
