from django import views
 
from django.urls import path
from Home import views
urlpatterns = [ 
    path('',views.index,name='Home'),
    path('logout',views.logoutUser,name='logout'),
    path('login',views.loginUser,name='login')
]
