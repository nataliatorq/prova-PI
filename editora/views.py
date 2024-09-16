from django.shortcuts import get_object_or_404, redirect, render

from .forms import LivroForm
from .models import Livro


def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'livro_list.html', {'livros': livros})

def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livro_detail.html', {'livro': livro})

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('livro_list')
    else:
        form = LivroForm()
    return render(request, 'livro_form.html', {'form': form})

def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save()
            return redirect('livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livro_form.html', {'form': form})

def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    livro.delete()
    return redirect('livro_list')
