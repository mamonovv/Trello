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
    path('main/new_board/', new_board, name='new_board'),
    path('main/board/<int:board_id>/', show_board, name='board'),
    
    path('main/board/<int:board_id>/addColumn', add_column, name='add_column'), #Изменил эти пути!!!!!!!!!!!
    path('main/board/<int:board_id>/deleteColumn/<int:column_id>', del_column, name='del_column'), # + etot

    path('main/board/<int:board_id>/addCard/<int:column_id>', add_card, name='add_card'),
    path('main/board/<int:board_id>/deleteCard/<int:card_id>', del_card, name='del_card'),
    
    path('main/board/<int:board_id>/moveCard', move_card, name='move_card'),
    path('main/board/<int:board_id>/editCard', edit_card, name='edit_card'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    