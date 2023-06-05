from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('new', views.new, name='new'),
    path('msg', views.msg, name='msg'),
    path('logout', views.logout, name='logout'),

]
