from django.urls import path
from . import views

urlpatterns = [
    path('', views.connexion, name='connexion'),
    path('acces/', views.acces, name='acces'),
    path('modifiermembre/<int:pk>/', views.modifiermembre, name='modifiermembre'),
    path('creermembre/', views.creermembre, name='creermembre'),
    path('listemedia/', views.listemedia, name='listemedia'),
    path('ajoutmedia/', views.ajoutmedia, name='ajoutmedia'),
    path('listemembre/', views.listemembre, name='listemembre'),
    path('listemembre/supprimermembre/<int:pk>/', views.supprimermembre, name='supprimermembre'),
    path('empruntmedia/', views.empruntmedia, name="empruntmedia"),
    path('modifiermembre/<int:pk>/', views.modifiermembre, name='modifiermembre'),
    path('acces/creermembre/', views.creermembre, name='creermembre'),
    path('acces/listemedia/', views.listemedia, name='listemedia'),
    path('acces/ajoutmedia/', views.ajoutmedia, name='ajoutmedia'),
    path('acces/listemembre/', views.listemembre, name='listemembre'),
    path('listemembre/supprimermembre/<int:pk>/', views.supprimermembre, name='supprimermembre'),
    path('acces/empruntmedia/', views.empruntmedia, name="empruntmedia"),
]