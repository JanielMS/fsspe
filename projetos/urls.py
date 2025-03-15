from django.urls import path
from .views import *

app_name = 'projetos'

urlpatterns = [
    path('', ProjetoListView.as_view(), name='lista-projetos'),
    path('criar/', ProjetoCreateView.as_view(), name='criar-projeto'),
    path('editar/<int:pk>/', ProjetoUpdateView.as_view(), name='editar-projeto'),
    path('excluir/<int:pk>/', ProjetoDeleteView.as_view(), name='excluir-projeto'),
    path('visualizar/<int:pk>/', ProjetoDetailView.as_view(), name='ver-projeto'),
]
