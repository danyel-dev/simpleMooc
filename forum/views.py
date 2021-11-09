from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Topic


class forum(ListView):

    model = Topic
    paginate_by = 1
    template_name = 'forum/list_topics.html'

    def get_queryset(self):
        queryset = Topic.objects.all()

        if 'order' in self.request.GET:
            order = '-' + self.request.GET.get('order')
            queryset = queryset.order_by(order)

        slug_tag = self.kwargs.get('slug_tag', '')

        if slug_tag:
            queryset = queryset.filter(tags__slug__icontains=slug_tag)

        return queryset


    def get_context_data(self, **kwargs):
        context = super(forum, self).get_context_data(**kwargs)
        context['tags'] = Topic.tags.all()
        return context


class detail_topic(DetailView):

    model = Topic
    template_name = 'forum/detail_topic.html'

    def get_context_data(self, **kwargs):
        context = super(detail_topic, self).get_context_data(**kwargs)
        context['tags'] = Topic.tags.all()
        return context
    