from django.urls import path
from catalog.views import index, contacts, about_me

urlpatterns = [
    path('', index),
    path('contacts/templates/contacts.html', contacts),
    path('catalog/templates/catalog/about_me.html', about_me)
]
