from django.urls import path
from .views import *
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
        
        
        path('groups/manager/users/',ManagerViewSet.as_view({'get': 'list',
                                                  'post':'create',
                                                  'delete':'destroy'}
                                                 ),name="manager"),
        
        
        path('groups/delivery-crew/users/',DeliveryCrewViewSet.as_view({'get': 'list',
                                                  'post':'create',
                                                  'delete':'destroy'}
                                                 ),name="manager"),
        
        
        path('cart/menu-items/',CartViewSet.as_view({'get': 'list',
                                                  'post':'create',
                                                  'delete':'destroy'}
                                                 ),name="cart"),
        
        path('orders/',OrderViewSet.as_view({'get': 'list',
                                                  'post':'create',
                                                  'delete':'destroy'
                                                }
                                                 ),name="order"),
        
        path('orders/<int:orderId>',OrderManagementViewSet.as_view({'get': 'retrieve',
                                                  'put':'update',
                                                  'delete':'destroy'
                                                }
                                                 ),name="order"),
        
]
