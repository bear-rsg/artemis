from django.views.generic import (ListView, DetailView)
from . import models


class BlogListView(ListView):
    """
    Class-based view to show the blog list template
    """

    template_name = 'blog/list.html'
    queryset = models.Blog.objects.all()


class BlogDetailView(DetailView):
    """
    Class-based view to show the blog detail template
    """

    template_name = 'blog/detail.html'
    queryset = models.Blog.objects.all()
