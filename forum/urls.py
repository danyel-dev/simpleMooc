from django.urls import path
from . import views


urlpatterns = [
    path('topicos/', views.forum.as_view(), name='forum'),
]
