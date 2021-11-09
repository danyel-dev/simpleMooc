from django.urls import path
from . import views


urlpatterns = [
    path('topicos/', views.forum.as_view(), name='forum'),
    path('topicos/tag/<slug:slug_tag>/', views.forum.as_view(), name='forum-tag'),
    path('topico/<slug:slug>/', views.detail_topic.as_view(), name='detail-topic'),
]
