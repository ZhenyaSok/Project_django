from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView


class IndexView(TemplateView):
    template_name = 'catalog/index_main.html'
    extra_context = {
        'title': 'Категории'

    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()[:100]

        return context_data

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'{category_item.name}'

        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:categories')

    def get_success_url(self):
        return reverse('catalog:category_products', args=[self.object.category.pk])

# class ProductCreateView(CreateView):
#     model = Product
#     fields = ('name', 'category',)
#     success_url = reverse_lazy('catalog:categories')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return  context_data
    
    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('catalog:product_update', args=[self.kwargs.get('pk')])



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:categories')

def contacts(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'({email}):{message}')
    return render(request, 'catalog/contacts.html')

def about_me(request):
    return render(request, 'catalog/about_me.html')

def product_form(request):
    if request.method == 'POST':

        return render(request, 'catalog/product_form.html')
