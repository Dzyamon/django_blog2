from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class Blog2ListView(ListView):
    model = Post
    template_name = 'home.html'


class Blog2DetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'