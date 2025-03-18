from django.urls import path
from .views import *

app_name = 'acontecimentos'

urlpatterns = [
    path('', AcontecimentoListView.as_view(), name='lista-acontecimentos'),
    path('criar/', AcontecimentoCreateView.as_view(), name='criar-acontecimento'),
    path('visualizar/<int:pk>', AcontecimentoDetailView.as_view(), name='ver-acontecimento'),
    path('editar/<int:pk>', AcontecimentoUpdateView.as_view(), name='editar-acontecimento'),
    path('excluir/<int:pk>', AcontecimentoDeleteView.as_view(), name='excluir-acontecimento')
]
