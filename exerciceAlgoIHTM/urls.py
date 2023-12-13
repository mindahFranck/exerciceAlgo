from django.contrib import admin
from django.urls import path

import allexercice.views as views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('algorithme', views.algorithme1, name='algorithme'),
    path('algorithme1', views.algorithme2, name='algorithme1'),
    path('algorithme2', views.algorithme3, name='algorithme2'),
    path('calculfacteur', views.add, name='calculfacteur'),
    path('admin/', admin.site.urls),
]
