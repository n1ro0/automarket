from django import forms
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'



class OwnerForm(forms.ModelForm):
    class Meta:
        model = models.Owner
        fields = '__all__'


class CarAdForm(forms.ModelForm):
    class Meta:
        model = models.CarAd
        fields = '__all__'


class OfferForm(forms.ModelForm):
    class Meta:
        model = models.Offer
        fields = '__all__'