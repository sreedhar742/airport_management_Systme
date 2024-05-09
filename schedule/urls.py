from django.urls import path
from . import views

urlpatterns = [
    path('', views.dosch, name='dosch'),
    path('new/', views.donew, name='donew'),
    path('createschedule/', views.docreateschedule, name='docreateschedule'),
    path('update/', views.doupdate, name='doupdate'),
    path('delete/', views.dodelete, name='dodelete'),
    path('change/', views.dochange, name='dochange'),
    path('remove/', views.doremove, name='doremove'),
    path('reschedule/', views.doreschedule, name='doreschedule'),
    path('choosecategory/', views.dochoosecategory, name='dochoosecategory'),
    path('searchid/', views.dosearchid, name='dosearchid'),
    path('searchcity/', views.dosearchcity, name='dosearchcity'),
    path('city/', views.docity, name='docity'),
    path('id/', views.doid, name='doid'),
]
