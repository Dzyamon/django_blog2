from django.urls import path
from .views import Blog2ListView, Blog2DetailView, Blog2CreateView, Blog2UpdateView, Blog2DeleteView


urlpatterns = [
    path('post/new/', Blog2CreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', Blog2DetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', Blog2UpdateView.as_view(), name='post_edit'),
    path("post/<int:pk>/delete/", Blog2DeleteView.as_view(), name='post_delete'),
    path('', Blog2ListView.as_view(), name='home'),
]