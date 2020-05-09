from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.posts, name='posts'), 
    path('create/', views.post_create, name="create"),
    path('<int:post_id>/', views.post_detail, name='detail'),
    path('update/<int:post_id>/', views.post_update, name="update"),
    path('delete/<int:post_id>/', views.post_delete, name="delete"),
]