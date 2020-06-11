from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('register/', views.register),
    path('login/', views.login),
    path('post_register/', views.post_register),
    path('post_login/', views.post_login),
    path('user/<int:id>/', views.user),
    path('champions/', views.champions_page),
    path('logout/', views.logout),
    path('champions/<str:id>/', views.champ_info),
    path('champions/<str:id>/add/', views.add),
    path('user/<int:user_id>/remove/<str:champ_id>/', views.remove),
]
