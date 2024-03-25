from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import MenuItem,Cart
from .serializers import MenuItemSerializer, UserSerializer, CartSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from rest_framework import status, viewsets
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from decimal import Decimal



@permission_classes([IsAuthenticated,IsManagerOrReadOnly])
class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
@permission_classes([IsAuthenticated,IsManagerOrReadOnly])
class SingleMenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class ManagerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsManager]
    
    
    def list(self, request):
        manager_group = Group.objects.get(name='Manager')
        manager_users = manager_group.user_set.all()
        serializer = UserSerializer(manager_users, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        managers = Group.objects.get(name="Manager")
        managers.user_set.add(user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        managers = Group.objects.get(name="Manager")
        managers.user_set.remove(user)

        return Response({"message":"delete successful! "}, status=status.HTTP_204_NO_CONTENT)
        

class DeliveryCrewViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsManager]
    
    
    def list(self, request):
        delivery_crew_group = Group.objects.get(name='Delivery Crew')
        delivery_crew_users = delivery_crew_group.user_set.all()
        serializer = UserSerializer(delivery_crew_users, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        delivery_crew = Group.objects.get(name="Delivery Crew")
        delivery_crew.user_set.add(user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        delivery_crew = Group.objects.get(name="Delivery Crew")
        delivery_crew.user_set.remove(user)

        return Response({"message":"delete successful! "}, status=status.HTTP_204_NO_CONTENT)


class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        carts = Cart.objects.filter(user=request.user) 
        serializer = CartSerializer(carts, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        menuitem = get_object_or_404(MenuItem, title=request.data["title"])
        quantity = request.data['quantity']
        unit_price = menuitem.price
        price = Decimal(quantity) *unit_price


        cart_item = Cart.objects.create(
                user=request.user,
                menuitem=menuitem,
                quantity=quantity,
                unit_price=unit_price,
                price=price
            )

        serializer = CartSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request):
        carts = Cart.objects.filter(user=request.user)
        if not carts.exists():
            raise PermissionDenied("Your cart is already empty.")

        carts.delete()
        return Response({"message":"Your cart has been emptied."}, status=status.HTTP_204_NO_CONTENT)
  
             
    