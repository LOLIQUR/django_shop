from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта',
    'биржа', 'дешево', 'бесплатно',
    'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-select'})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise forms.ValidationError(f'Название содержит запрещённое слово: "{word}"')
        return name

    def clean_description(self):
        desc = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word.lower() in desc.lower():
                raise forms.ValidationError(f'Описание содержит запрещённое слово: "{word}"')
        return desc

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной')
        return price
