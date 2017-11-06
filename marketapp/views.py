from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

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
    success_url = '/carads/'


#Category model------------------------------------------------------
class CategoryListView(generic.ListView):
    template_name = 'categories.html'
    model = models.Category
    context_object_name = 'categories'


class CategoryDetailView(generic.DetailView):
    template_name = 'category.html'
    model = models.Category

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
class OwnerListView(LoginRequiredMixin, generic.ListView):
    template_name = 'owners.html'
    model = models.Owner
    context_object_name = 'owners'


class OwnerDetailView(generic.DetailView):
    template_name = 'owner.html'
    model = models.Owner


class OwnerCreateView(generic.CreateView):
    template_name = 'owner_create.html'
    form_class = forms.OwnerForm
    success_url = '/owners/'



class OwnerUpdateView(generic.UpdateView):
    template_name = 'owner_create.html'
    model = models.Owner
    form_class = forms.OwnerForm
    success_url = '/owners/'



class OwnerDeleteView(generic.DeleteView):
    template_name = 'delete_conformation.html'
    model = models.Owner
    success_url = '/owners/'


#Comment model-------------------------------------------------------------
class OfferCreateView(generic.CreateView):
    template_name = 'base_create.html'
    form_class = forms.OfferForm
    success_url = "/"

class IndexView(generic.TemplateView):
    template_name = "index.html"

def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return render(request, "index.html")


class IndexView1(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, template_name="index.html")


    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     #context['book'] = models.Book.objects.filter(id = self.kwargs['pk']).first()
    #     context['carads_count'] = models.CarAd.objects.count()
    #     context['owners_count'] = models.Owner.objects.count()
    #     context['categories_count'] = models.Category.objects.count()
    #     return context