from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Customer
from .serializers import CustomerSerializer

from rest_framework.authentication import BasicAuthentication,SessionAuthentication

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # authentication_classes=[BasicAuthentication]
    
    authentication_classes=[SessionAuthentication]
    
    # permission_classes=[IsAdminUser]#only those users whose is_staff is true in adminpanel will be able to use this view
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[DjangoModelPermissions]
    
    