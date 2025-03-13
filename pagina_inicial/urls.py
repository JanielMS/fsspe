from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaInicialView.as_view(), name='pagina-inicial'),
    path('processos/ciclodevida/', TemplateView.as_view(template_name='pagina_inicial/pages/ciclodevida.html'), name='ciclo-de-vida'),
     path('processos/', TemplateView.as_view(template_name='pagina_inicial/pages/processos.html'), name='processos'),
     path('processos/templates', TemplateView.as_view(template_name='pagina_inicial/pages/templates.html'), name='templates'),
     path('processos/ferramentas', TemplateView.as_view(template_name='pagina_inicial/pages/ferramentas.html'), name='ferramentas'),
]