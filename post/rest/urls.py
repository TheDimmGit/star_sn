from django.urls import path
from rest_framework import routers

from .views import AnalyticsView, PostView

post_router = routers.SimpleRouter()
post_router.register(r'posts', PostView)
post_router.register(r'like', PostView)

urlpatterns = [
    path('analytics/', AnalyticsView.as_view()),
]

urlpatterns += post_router.urls
