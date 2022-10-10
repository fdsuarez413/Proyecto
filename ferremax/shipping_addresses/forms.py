from django.forms import ModelForm
from .models import ShippingAddres

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddres
        fields = [
            'linea1', 'linea2', 'city', 'state', 'country', 'postal_code', 'reference'
        ]
        
        # labels= {
        #     'linea1': 'calle1',
        #     'linea2': 'calle1',
        #     'city': 'calle1',
        #     'state': 'calle1',
        #     'country': 'calle1',
        #     'postal_code':'Codigo postal',
        #     'reference':'Anotacion'
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['linea1'].widget.attrs.update({
            'class':'form-control'
        })
        
        self.fields['linea2'].widget.attrs.update({
            'class':'form-control'
        })
        
        self.fields['city'].widget.attrs.update({
            'class':'form-control',
            'readonly':''
        })
        
        self.fields['state'].widget.attrs.update({
            'class':'form-control'
        })
        
        self.fields['country'].widget.attrs.update({
            'class':'form-control',
            'readonly':''
        })
        
        self.fields['postal_code'].widget.attrs.update({
            'class':'form-control',
            'placeholder': '111011.',
        })
        
        self.fields['reference'].widget.attrs.update({
            'class':'form-control',
            'placeholder': 'EJ: Casa, Apat.'
        })