from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ConverterForm
from num2words import num2words

def home(request):    
    if request.method == 'POST':        
        form = ConverterForm(request.POST)
        
        if form.is_valid():
            number = form.cleaned_data['number']
            context = {'form': form, 'converted': converter(number)}
            return render(request, 'index.html', context)

    else:
        form = ConverterForm()
    return render(request, 'index.html', {'form': form})

def converter(number):
    return num2words(number, lang='pt_BR')
