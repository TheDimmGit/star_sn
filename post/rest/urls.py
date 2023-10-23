from django.contrib import admin
from django.urls import path, include
from .views import PostView
from rest_framework import routers

post_router = routers.SimpleRouter()
post_router.register(r'posts', PostView)
post_router.register(r'like', PostView)

urlpatterns = post_router.urls
