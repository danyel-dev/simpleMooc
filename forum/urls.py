from django.urls import path
from . import views


urlpatterns = [
    path('topics/', views.forum.as_view(), name='forum'),
]
