from django.urls import path
from . import views

app_name = 'users'


urlpatterns = [
    path('account/', views.account_view, name='account'),
    path('profile/', views.profile, name='profile'),

    # other url patterns...
]
