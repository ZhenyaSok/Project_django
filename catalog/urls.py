from catalog.apps import CatalogConfig
from catalog.views import IndexView, ProductListView, about_me, contacts, CategoryListView, ProductUpdateView, \
    ProductCreateView, ProductDeleteView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index_main'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<int:pk>/', ProductListView.as_view(), name='category_products'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    # path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', contacts, name='info'),
    path('about_me/', about_me, name='about_me'),
    # path('product_form/', product_form, name='product_form'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

