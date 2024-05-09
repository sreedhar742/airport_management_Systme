from django.urls import path
from . import views

urlpatterns = [
    path('', views.dohome, name='dohome'),
    path('login/', views.dologin, name='dologin'),
    path('doauth/', views.doauth, name='doauth'),
    path('logout/', views.dologout, name='dologout'),
]
