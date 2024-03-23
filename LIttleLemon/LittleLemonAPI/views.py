from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManagerOrReadOnly
from rest_framework import status, viewsets


@permission_classes([IsAuthenticated,IsManagerOrReadOnly])
class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
@permission_classes([IsAuthenticated,IsManagerOrReadOnly])
class SingleMenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
