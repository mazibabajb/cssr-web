from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name ='tutor-home'),
    path('register/', views.register, name ='register'),
    path('profile/', views.profile, name ='profile'),
    path('find/', views.find, name ='find'),
]
