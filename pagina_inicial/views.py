from django.shortcuts import render
from django.views.generic import TemplateView
from projetos.models import Projeto


class PaginaInicialView(TemplateView):
    template_name = 'pagina_inicial/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Buscando os projetos que estão com status finalizado
        projetos_finalizados = Projeto.objects.filter(status_projeto='finalizado')[:10]
        context['projetos_finalizados'] = projetos_finalizados
        return context

class SoftwaresView(TemplateView):
    template_name = 'pagina_inicial/pages/softwares.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projetos_finalizados = Projeto.objects.filter(status_projeto='finalizado')
        context['projetos_finalizados'] = projetos_finalizados
        projetos_finalizados = Projeto.objects.filter(status_projeto='nao_finalizado')
        context['projetos_nao_finalizados'] = projetos_finalizados
        projetos_finalizados = Projeto.objects.filter(status_projeto='em_andamento')
        context['projetos_em_andamento'] = projetos_finalizados
        return context
