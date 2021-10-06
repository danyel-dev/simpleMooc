from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('detail/<slug:slug>/', views.course_detail, name='course-detail'),
]
