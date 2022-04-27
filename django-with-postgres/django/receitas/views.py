from django.shortcuts import get_object_or_404, render
from .models import Receitas

def index(request):
    #receitas = Receitas.objects.all()
    receitas = Receitas.objects.order_by('-date_receita').filter(publicada=True)


    dados = {
        'receitas' : receitas
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)

    receita_exibir = {
        'receita': receita
    }

    return render(request, 'receita.html', receita_exibir )


def buscar(request):
    lista_receitas = Receitas.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas' : lista_receitas
    }

    return render(request, 'buscar.html', dados)

