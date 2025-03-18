from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
     class Meta:
        model = Projeto
        fields = [
            "nome", "nome_abreviado","data_inicio", "cliente", "nome_da_equipe",
            "status_projeto", "status_implantacao", "status_registro", "descricao", "equipe", "link_do_projeto", "imagem"
        ]

        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
        }


        