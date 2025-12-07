from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'), #example route
    path('posts/', views.posts, name='posts'),
    path('posts/<int:id>/', views.post, name='post'),
]