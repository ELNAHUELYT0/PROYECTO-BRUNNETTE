from django.urls import path
from MiPrimerApp import views

urlpatterns = [
    path('', views.AppIndex, name='app_index'),
    path('ValidarLogin', views.ValidarLogin, name='validar-login'),
]
