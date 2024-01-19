from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from catalog.models import Category, Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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

def index_main(request):
    context = {
        'object_list': Category.objects.all()[:100],
        'title': 'Магазин'
    }
    return render(request, 'catalog/index_main.html', context)

# class UbaListView(ListView):
#     model =

# def categories(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Категории'
#     }
#     return render(request, 'catalog/category_list.html', context)

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }

# def category_products(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=pk),
#         'title': f'{category_item.name}'
#     }
#     return render(request, 'catalog/product_list.html', context)

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
    fields = ('name', 'category',)
    success_url = reverse_lazy('catalog:categories')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'category',)

    def get_success_url(self):
        return reverse('catalog:category_products', args=[self.object.category.pk])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category_products')




