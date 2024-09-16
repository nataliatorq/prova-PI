from django.forms import ModelForm
from django import forms
from .models import Aluno

class AlunoForm(ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
      
        widgets = {
            'nome_aluno' : forms.TextInput(attrs={'class': 'form-control' }),
        }
