from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ConversorForm

def home(request):    
    if request.method == 'POST':        
        form = ConversorForm(request.POST)
        
        if form.is_valid():
            numero = form.cleaned_data['numero']
            print(numero)
            return render(request, 'index.html', {'form': form, 'extenso': conversor(numero)})

    else:
        form = ConversorForm()
    return render(request, 'index.html', {'form': form, 'extenso': ''})

def conversor(numero):
    switcher = {
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        10: "dez",
        11: "onze",
        12: "doze"
    }
    return switcher.get(numero, "Número inválido")