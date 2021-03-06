from django.urls import path

from . import views


urlpatterns = [
    path('dashboard/', views.dashboard,  name='dashboard'),
    path('register/', views.register,  name='register'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('edit_password/', views.edit_password,  name='edit_password'),
    path('course-adverts/<slug:slug>/', views.course_adverts,  name='course-adverts'),
    path('<slug:slug>/anuncios/<int:id_advert>/', views.detail_advert,  name='detail-advert'),
    path('<slug:slug>/aulas/', views.lessons,  name='lessons'),
    path('<slug:slug>/aula/<int:id_lesson>/', views.detail_lesson,  name='detail-lesson'),
    path('<slug:slug>/material/<int:id_material>/', views.material,  name='material'),
]
