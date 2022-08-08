
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),

]
