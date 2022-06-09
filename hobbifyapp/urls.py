from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('add_hobby', views.add_hobby, name='add_hobby'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('likes', views.likes, name='likes'),
    path('like/<int:user_id>', views.like, name='like'),
]
