from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import Topic
from .forms import ReplyForm


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


# class detail_topic(DetailView):

#     model = Topic
#     template_name = 'forum/detail_topic.html'

#     def get_context_data(self, **kwargs):
#         context = super(detail_topic, self).get_context_data(**kwargs)
#         context['tags'] = Topic.tags.all()
#         return context


def detail_topic(request, slug_topic):
    topic = get_object_or_404(Topic, slug=slug_topic)
    tags = Topic.tags.all()

    if topic.author != request.user:
        topic.views = topic.views + 1
        topic.save()

    form = ReplyForm(request.POST or None)

    if request.method == 'POST':
        if request.user.is_authenticated:
            if form.is_valid():
                reply = form.save(commit=False)
                reply.topic = topic
                reply.author = request.user
                reply.save()

                form = ReplyForm()
                messages.success(request, 'Comentário enviado com sucesso!')
                
                return redirect('detail-topic', slug_topic)
        else:
            return redirect('login')
        
    return render(request, 'forum/detail_topic.html', {'topic': topic, 'tags': tags, 'form': form})
