from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name'].lower()
        for word in self.forbidden:
            if word in cleaned_data:
                raise forms.ValidationError('Ай-яй-яй, такое продавать нельзя')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description'].lower()
        for word in self.forbidden:
            if word in cleaned_data:
                raise forms.ValidationError('Ай-яй-яй, такое продавать нельзя')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'