from django.shortcuts import render, get_object_or_404
from django.views import generic

from . import forms
from . import models


#Book model------------------------------------------------------
class CarAdListView(generic.ListView):
    template_name = 'carads.html'
    model = models.CarAd
    context_object_name = 'carads'


class CarAdDetailView(generic.DetailView):
    template_name = 'carad.html'
    model = models.CarAd
    context_object_name = 'carad'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CarAdDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['book'] = models.Book.objects.filter(id = self.kwargs['pk']).first()
        context['offers'] = models.Offers.objects.filter(carad_id = self.kwargs['pk'])
        return context


class CarAdCreateView(generic.CreateView):
    template_name = 'carad_create.html'
    form_class = forms.CarAdForm
    success_url = '/carads/'

    def get_success_url(self):
        return self.success_url


class CarAdUpdateView(generic.UpdateView):
    template_name = 'carad_create.html'
    model = models.CarAd
    form_class = forms.CarAdForm
    success_url = '/carads/'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return self.success_url


class CarAdDeleteView(generic.DeleteView):
    template_name = 'delete_conformation.html'
    success_message = "Deleted Successfully"
    model = models.CarAd
    success_url = '/CarAds/'


#Category model------------------------------------------------------
class CategoryListView(generic.ListView):
    template_name = 'categories.html'
    model = models.Category
    context_object_name = 'categories'


class CategoryDetailView(generic.ListView):
    template_name = 'category.html'
    model = models.Category
    # context_object_name = 'category'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(models.Category.objects.prefetch_related('carads'),
                                                id=self.kwargs['pk'])
        return context


class CategoryCreateView(generic.CreateView):
    template_name = 'create_category.html'
    form_class = forms.CategoryForm
    success_url = "/categories/"


class CategoryUpdateView(generic.UpdateView):
    template_name = 'create_category.html'
    model = models.Category
    form_class = forms.CategoryForm
    success_url = "/categories/"


class CategoryDeleteView(generic.DeleteView):
    template_name = 'delete_conformation.html'
    success_message = "Deleted Successfully"
    model = models.Category
    success_url = '/categories/'



#Author model------------------------------------------------------
class OwnerListView(generic.ListView):
    template_name = 'owners.html'
    model = models.Owner
    context_object_name = 'owners'


class OwnerUpdateView(generic.UpdateView):
    template_name = 'base_create.html'
    model = models.Owner
    form_class = forms.OwnerForm
    success_url = '/owners/'


#Comment model-------------------------------------------------------------
class OfferCreateView(generic.CreateView):
    template_name = 'base_create.html'
    form_class = forms.OfferForm
    success_url = "/"


def index(request):
    return render(request, "index.html")