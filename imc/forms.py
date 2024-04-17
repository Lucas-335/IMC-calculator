from django import forms

class ImcForm(forms.Form):
    weight = forms.CharField(
        label="Peso:", 
        widget=forms.TextInput(attrs={'class':'input-text'}))
    height = forms.CharField(
        label="Altura:", 
        widget=forms.TextInput(attrs={'class':'input-text'}))