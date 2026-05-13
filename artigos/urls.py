from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_artigos_view, name='lista'),
    path('<int:artigo_id>/', views.detalhe_artigo_view, name='detalhe'),
    path('<int:artigo_id>/like/', views.like_artigo_view, name='like'),
    path('<int:artigo_id>/comentar/', views.comentar_view, name='comentar'),
]