from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ConversorForm
from num2words import num2words

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
    return num2words(numero, lang='pt_BR')
