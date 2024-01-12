from catalog.views import index_main  #, about_me, contacts
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index_main),
    # path('contacts/', contacts, name='info'),
    # path('about_me/', about_me,),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

