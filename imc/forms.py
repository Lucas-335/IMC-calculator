from django import forms
from django.core.exceptions import ValidationError
class ImcForm(forms.Form):
    weight = forms.CharField(
        label="Peso:", 
        widget=forms.TextInput(attrs={'class':'input-text'}), required=True)
    height = forms.CharField(
        label="Altura:", 
        widget=forms.TextInput(attrs={'class':'input-text'}), required=True)
    
    def transform_string(self, string):
        string = string.replace(' ','')
        if ',' in string:
            result = string.replace(',','.')
            return result
        return string
    
    def clean(self):
        data = self.cleaned_data
        # if not (
        #     'weight' in data.keys() or 
        #     'height' in data.keys()):
        #     self.add_error(None, ValidationError('Por favor, preencha todos os campos', code="invalid"))
        
        weight_ = self.transform_string(data['weight'])
        height_ = self.transform_string(data['height'])
        
        try:
            w_ = float(weight_)
            h_ = float(height_)
        except:
            self.add_error(
                None,
                ValidationError('Insira números válidos', code='invalid'),
            )
            data['weight'] = 0
            data['height'] = 0
            return data
        
        data['weight'] = w_
        data['height'] = h_
         