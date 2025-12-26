from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Customer
from .serializers import CustomerSerializer

from rest_framework.authentication import BasicAuthentication,SessionAuthentication

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions

# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

from rest_framework.throttling import ScopedRateThrottle

from customers.throttling import JackRateThrottle

# class CustomerViewSet(ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     # authentication_classes=[BasicAuthentication]
    
#     authentication_classes=[SessionAuthentication]
    
#     # permission_classes=[IsAdminUser]#only those users whose is_staff is true in adminpanel will be able to use this view
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     # permission_classes=[AllowAny]
#     # permission_classes=[IsAuthenticatedOrReadOnly]
#     # permission_classes=[DjangoModelPermissions]
    
#     # throttle_classes=[AnonRateThrottle,UserRateThrottle]
    
#     throttle_classes=[AnonRateThrottle,JackRateThrottle]
    
 
class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly] 
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'
   
class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'
    

class CustomerRetrieveView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'


class CustomerUpdateView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'
    
class CustomerDestroyView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'

