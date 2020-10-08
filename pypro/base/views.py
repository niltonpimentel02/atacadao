from django.shortcuts import render


def home(request):
    produtos = [
        {'descricao': 'Banana prata', 'cor': 'Amarelo', 'peso': '1kg'},
        {'descricao': 'Maçã', 'cor': 'Vermelho', 'peso': '500g'},
        {'descricao': 'Laranja', 'cor': 'Laranja', 'peso': '2kg'},
        {'descricao': 'Melancia', 'cor': 'Verde', 'peso': '4kg'},
    ]
    return render(request, 'base/home.html', context={'produtos': produtos})
