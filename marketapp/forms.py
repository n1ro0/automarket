from django import forms
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'


class OwnerForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'


class CarAdForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'


class OfferForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'