from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .views import HomeView, UserDetailView

from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('user_detail/<int:pk>/', UserDetailView.as_view(), name="detail"),
    path('register/', views.register, name = 'register'),
    path('logout/', views.user_logout, name = 'logout'),
    path('login/', views.user_login, name = 'user_login'),
]


 