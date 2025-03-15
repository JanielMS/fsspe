from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
     class Meta:
        model = Projeto
        fields = [
            "nome", "nome_abreviado","data_inicio", "cliente",
            "status_projeto", "status_implantacao", "status_registro", "descricao", "equipe","nome_da_equipe", "imagem"
        ]
        