from django import forms
from AppRodriguez.models import Mayorista, Minorista, Stock

class MayoristaForm(forms.ModelForm):
    class Meta:
        model = Mayorista
        fields = '__all__'

class MinoristaForm(forms.ModelForm):
    class Meta:
        model = Minorista
        fields = '__all__'

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
