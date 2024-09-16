from django.urls import path

from . import views

urlpatterns = [
    path('livros/', views.livro_list, name='livro_list'),
    path('livros/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/<int:pk>/editar/', views.livro_update, name='livro_update'),
    path('livros/<int:pk>/excluir/', views.livro_delete, name='livro_delete'),
]