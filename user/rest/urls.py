from django.urls import path
from user.rest import views

urlpatterns = [
    path('signup', views.UserCreate.as_view())
]
