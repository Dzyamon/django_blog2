from django.urls import path
from .views import Blog2ListView, Blog2DetailView


urlpatterns = [
    path('post/<int:pk>/', Blog2DetailView.as_view(), name='post_detail'),
    path('', Blog2ListView.as_view(), name='home'),
]