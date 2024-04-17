from django import forms

class ImcForm(forms.Form):
    weight = forms.FloatField(
        label="Peso:", 
        widget=forms.TextInput(attrs={'class':'input-text'}))
    height = forms.FloatField(
        label="Altura:", 
        widget=forms.TextInput(attrs={'class':'input-text'}))