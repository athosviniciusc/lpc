from django.urls import path
from .views import *

urlpatterns = [
    path('orcamentos/', orcamentos_lista, name='orcamentos-lista'),
    path('orcamentos/estatisticas/', orcamentos_estatisticas, name='orcamentos-estatisticas'),
    path('clientes/<codigo>', informacoes_cliente, name='informacoes_cliente'),
    path('clientes/estatisticas/', estatisticas_cliente, name='estatisticas_cliente')
]
