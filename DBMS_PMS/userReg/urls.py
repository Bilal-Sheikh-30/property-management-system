
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('home/', views.home,name='home'),
    path('logined/', views.logined,name='logined'),
]