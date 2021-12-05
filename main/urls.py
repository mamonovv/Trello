from Trell import settings
from django.urls import path, include
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name = 'home'),
    path('login/', login, name = 'login'),
    #path('register/', RegisterUser.as_view(), name = 'register'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    