from django.urls import path
from new1 import views
from .views import UserList, DetailUser

urlpatterns = [
    path('users', UserList.as_view(), name='users'),
    path('users/<int:pk>/', DetailUser.as_view(), name='singleuser'),
]
