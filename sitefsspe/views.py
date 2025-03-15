from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(LoginRequiredMixin, TemplateView):
    template_name  = 'home.html'

def custom_403(request, exception):
    """
    View para exibir a página de acesso negado (403).
    """
    return render(request, "core/403.html", status=403)