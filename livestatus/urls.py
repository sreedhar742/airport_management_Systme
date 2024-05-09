from django.urls import path
from . import views

urlpatterns = [
    path('', views.doinit, name='doinit'),
    path('lpassogood/', views.dolpassogood, name='dolpassogood'),
    path('lflight/', views.dolflight, name='dolflight'),
    path('livef/', views.dolivef, name='dolivef'),
    path('livepg/', views.dolivepg, name='dolivepg'),
]
