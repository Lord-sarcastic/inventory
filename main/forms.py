from django import forms

from main.models import Item


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
