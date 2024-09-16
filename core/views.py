from django.shortcuts import get_object_or_404, redirect, render

from .form import AlunoForm
from .models import Aluno


# Create your views here.
def index(request):
    return render(request, 'core/index.html')

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm()
    return render(request, 'core/form.html', {'form': form})

def lista(request):
    alunos = Aluno.objects.all()
    return render(request, 'core/lista.html', {'alunos': alunos})


def detalhe(request,id):
    aluno = get_object_or_404(Aluno, id=id)
    return render(request, 'core/detalhe.html', {'aluno': aluno})

def update(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'core/form.html', {'form': form})

def delete(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista')

