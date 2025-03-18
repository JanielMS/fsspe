from django import forms
from .models import Acontecimento

class AcontecimentoForm(forms.ModelForm):
    class Meta:
        model = Acontecimento
        fields = ['titulo', 'data', 'descricao', 'imagem']

        widgets = {
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
