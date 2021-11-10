from django.urls import path
from . import views


urlpatterns = [
    path('topicos/', views.forum.as_view(), name='forum'),
    path('topicos/tag/<slug:slug_tag>/', views.forum.as_view(), name='forum-tag'),
    path('topico/<slug:slug_topic>/', views.detail_topic, name='detail-topic'),
]
