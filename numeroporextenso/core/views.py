from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ConverterForm
from num2words import num2words

def home(request):
    """Renders the home page"""
    if request.method == 'POST':        
        form = ConverterForm(request.POST)
        
        if form.is_valid():
            number = form.cleaned_data['number']
            context = {
                'form': form, 
                'cardinal': convert(number), 
                'currency': convert(number, 'currency')}
            return render(request, 'index.html', context)

    else:
        form = ConverterForm()
    return render(request, 'index.html', {'form': form})

def convert(number, format='cardinal'):
    """Convert number to text in specific formats"""
    return num2words(number, lang='pt_BR', to=format)
