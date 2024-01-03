from catalog.views import contacts, index, about_me
from django.urls import path


urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('about_me/', about_me),
]

