from django.shortcuts import render
from catalog.models import Category, Product

def contacts(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'({email}):{message}')
    return render(request, 'catalog/contacts.html')

def about_me(request):
    return render(request, 'catalog/about_me.html')

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        overview = request.POST.get('overview')
        print(f'({name}):{overview}')

    return render(request, 'catalog/form.html')

def index_main(request):
    context = {
        'object_list': Category.objects.all()[:100],
        'title': 'Магазин'
    }
    return render(request, 'catalog/index_main.html', context)

def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории'
    }
    return render(request, 'catalog/categories.html', context)

def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{category_item.name}'
    }
    return render(request, 'catalog/products.html', context)


