from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

def contacts(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'({email}):{message}')
    return render(request, 'catalog/contacts.html')

def about_me(request):
    return render(request, 'catalog/about_me.html')
