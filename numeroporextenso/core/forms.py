from django import forms

class ConversorForm(forms.Form):
    numero = forms.DecimalField(decimal_places=2, label=False)