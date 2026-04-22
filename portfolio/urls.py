from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    
    path('projeto/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projeto/edita/<int:projeto_id>/', views.edita_projeto_view, name='edita_projeto'),
    path('projeto/apaga/<int:projeto_id>/', views.apaga_projeto_view, name='apaga_projeto'),
    
    path('sobre/', views.sobre_view, name='sobre'),
]