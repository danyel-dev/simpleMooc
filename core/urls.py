from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('course-detail/<slug:slug>/', views.detail_course, name='detail-course'),
]
