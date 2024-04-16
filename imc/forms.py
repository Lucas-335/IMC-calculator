from django import forms

class ImcForm(forms.Form):
    weight = forms.FloatField(label="Peso:")
    height = forms.FloatField(label="Altura:")