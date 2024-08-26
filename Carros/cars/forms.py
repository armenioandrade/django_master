from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    '''
    #Tentativa de validar se o campo não estiver preenchido, não funcionou
    def clean_value_str(self):
        value = self.cleaned_data.get('value')
        if value == '':
            self.add_error('value', 'Valor não pode estar em branco')
        else:
                ...
        return value
    '''
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value == 0:
            self.add_error('value', 'Valor não pode ser zero')
        elif value < 0:
            self.add_error('value', 'Valor não pode ser menor que zero')
        else:
            return value
        return value
    