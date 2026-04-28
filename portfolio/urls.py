from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
]