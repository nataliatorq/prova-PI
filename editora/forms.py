# forms.py
from django import forms

from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'descricao', 'editora', 'categoria']
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control' }),
            'descricao' : forms.TextInput(attrs={'class': 'form-control' }),
            'editora' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria' : forms.Select(attrs={'class': 'form-control' }),
        }
