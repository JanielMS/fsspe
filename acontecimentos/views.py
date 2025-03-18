from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Acontecimento
from .forms import AcontecimentoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class AcontecimentoListView(LoginRequiredMixin, ListView):
    model = Acontecimento
    template_name = 'acontecimentos/acontecimento_list.html'
    context_object_name = 'acontecimentos'
    paginate_by = 15
    ordering = ['-data']

class AcontecimentoDetailView(LoginRequiredMixin, DetailView):
    model = Acontecimento
    template_name = 'acontecimentos/acontecimento_detail.html'
    context_object_name = 'acontecimento'

class AcontecimentoCreateView(LoginRequiredMixin, CreateView):
    model = Acontecimento
    form_class = AcontecimentoForm
    template_name = 'acontecimentos/acontecimento_form.html'
    success_url = reverse_lazy('acontecimentos:lista-acontecimentos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class AcontecimentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Acontecimento
    form_class = AcontecimentoForm
    template_name = 'acontecimentos/acontecimento_form.html'
    success_url = reverse_lazy('acontecimentos:lista-acontecimentos')

class AcontecimentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Acontecimento
    template_name = 'acontecimentos/acontecimento_confirm_delete.html'
    success_url = reverse_lazy('acontecimentos:lista-acontecimentos')


