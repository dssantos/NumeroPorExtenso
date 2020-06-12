from django import forms

class ConverterForm(forms.Form):
    number = forms.DecimalField(
        decimal_places=2, 
        label=False, 
        max_value=10**18-1)
