from django.urls import path
from .views import MenuItemView,SingleMenuItemView

urlpatterns = [
        path('menu-items/', MenuItemView.as_view({'get': 'list',
                                                  'post':'create'}
                                                 ),
             name='menu_items'),
        
        path('menu-items/<int:pk>', SingleMenuItemView.as_view({'get': 'retrieve',
                                                          'put':'update',
                                                          'patch':'partial_update',
                                                          'delete':'destroy'
                                                          }),
              name='menu_items'),


]