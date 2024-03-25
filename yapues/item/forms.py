from django import forms 

from .models import Item

INPUT_CLASS = 'w-full py-3 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('categoria', 'nombre', 'descripcion', 'precio', 'imagen')

        widgets =  {
            'categoria': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'nombre': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'descripcion': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            'precio': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'imagen': forms.FileInput(attrs={
                'class': INPUT_CLASS
            }),
        }

class EdiItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('nombre', 'descripcion', 'precio', 'imagen', 'vendido')

        widgets =  {
            'nombre': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'descripcion': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            'precio': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'imagen': forms.FileInput(attrs={
                'class': INPUT_CLASS
            }),
        }