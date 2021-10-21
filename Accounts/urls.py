from django.urls import path

from . import views


urlpatterns = [
    path('', views.dashboard,  name='dashboard'),
    path('register/', views.register,  name='register'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('edit_password/', views.edit_password,  name='edit_password'),
    path('course-adverts/<slug:slug>/', views.course_adverts,  name='course-adverts')
]
