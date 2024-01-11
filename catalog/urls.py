from catalog.views import contacts, index, about_me
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index),
    path('contacts/', contacts, name='info'),
    path('about_me/', about_me,),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

