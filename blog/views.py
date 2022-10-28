from django.shortcuts import render
from django.views.generic import ListView
from .models import Post_blog
# Create your views here.


class BlogListView(ListView):
    model = Post_blog
    template_name = 'home_blog.html'
