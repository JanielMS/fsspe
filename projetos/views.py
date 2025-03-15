from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Projeto
from .forms import ProjetoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjetoListView(LoginRequiredMixin, ListView):
    model = Projeto
    template_name = "projetos/projeto_list.html"
    context_object_name = "projetos"
    paginate_by = 15
    ordering = ['nome'] 

class ProjetoDetailView(LoginRequiredMixin, DetailView):
    model = Projeto
    template_name = "projetos/projeto_detail.html"
    context_object_name = "projeto"

class ProjetoCreateView(LoginRequiredMixin, CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = "projetos/projeto_form.html"
    success_url = reverse_lazy("projetos:lista-projetos")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ProjetoUpdateView(LoginRequiredMixin, UpdateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = "projetos/projeto_form.html"
    success_url = reverse_lazy("projetos:lista-projetos")

class ProjetoDeleteView(LoginRequiredMixin, DeleteView):
    model = Projeto
    template_name = "projetos/projeto_confirm_delete.html"
    success_url = reverse_lazy("projetos:lista-projetos")
