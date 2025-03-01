from django.shortcuts import render
from django.views.generic import TemplateView

class PaginaInicialView(TemplateView):
    template_name = 'pagina_inicial/index.html'

