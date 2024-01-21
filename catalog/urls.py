from catalog.apps import CatalogConfig
from catalog.views import index_main, categories, category_products, about_me, contacts, form
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('', index_main, name='index_main'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/products/', category_products, name='category_products'),
    path('contacts/', contacts, name='info'),
    path('about_me/', about_me, name='about_me'),
    path('form/', form, name='form'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

