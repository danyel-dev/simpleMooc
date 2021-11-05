from django.shortcuts import render
from django.views.generic import ListView

from .models import Topic


class forum(ListView):

    model = Topic
    paginate_by = 10
    template_name = 'forum/list_topics.html'
