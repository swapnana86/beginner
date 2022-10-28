from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'post_home.html'
    context_object_name = 'all_posts_list'  # new
