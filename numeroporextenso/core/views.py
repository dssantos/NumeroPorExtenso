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
    if numero <= 99:
        return ate_99(numero)
    if numero <= 999:
        return ate_999(numero)

def ate_99(dezena):
    if dezena <= 19:
        return unidades(dezena)
    if dezena <= 99:
        if dezena%10 == 0:
            return dezenas(str(dezena)[0])
        else:
            return dezenas(str(dezena)[0]) + ' e ' + unidades(str(dezena)[1])

def ate_999(centena):
    if centena%100 == 0:
        return centenas(str(centena)[0])
    else:
        return centenas(str(centena)[0]) + ' e ' + ate_99(centena%100)

def unidades(n):
    switcher = {
        0: 'zero',
        1: 'um',
        2: 'dois',
        3: 'três',
        4: 'quatro',
        5: 'cinco',
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove',
        10: 'dez',
        11: 'onze',
        12: 'doze',
        13: 'treze',
        14: 'quatorze',
        15: 'quinze',
        16: 'dezesseis',
        17: 'dezessete',
        18: 'dezoito',
        19: 'dezenove'
    }
    return switcher.get(int(n), "Número inválido")

def dezenas(n):
    switcher = {
        2: 'vinte',
        3: 'trinta',
        4: 'quarenta',
        5: 'cinquenta',
        6: 'sessenta',
        7: 'setenta',
        8: 'oitenta',
        9: 'noventa'
    }
    return switcher.get(int(n), "Número inválido")

def centenas(n):
    switcher = {
        1: 'cento',
        2: 'duzentos',
        3: 'trezentos',
        4: 'quatrocentos',
        5: 'quinhentos',
        6: 'seiscentos',
        7: 'setecentos',
        8: 'oitocentos',
        9: 'novecentos'
    }
    return switcher.get(int(n), "Número inválido")
