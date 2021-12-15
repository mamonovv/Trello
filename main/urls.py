from Trell import settings
from django.urls import path, include
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name = 'home'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('logout/', logout_user , name = 'logout'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('main/', main_page, name = 'main'),
    path('main/<int:user_id>/', main_user, name='user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    