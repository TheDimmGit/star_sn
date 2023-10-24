from rest_framework import routers

from user.rest.views import UserCreate

user_router = routers.SimpleRouter()
user_router.register(r'users', UserCreate)

urlpatterns = user_router.urls
