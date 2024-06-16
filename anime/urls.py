from django.urls import path
from . import views
from .views import delete_movie

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('product/<int:pk>/add-comment/', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('delete_movie/<int:movie_id>/', delete_movie, name='delete_movie'),

    # Other URL patterns...
]
