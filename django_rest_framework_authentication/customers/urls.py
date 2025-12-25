from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet
from django.urls import path,include

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customers')

urlpatterns = [
  path('',include(router.urls)),
  path('auth/',include('rest_framework.urls',namespace='rest_framework'))
  #🔹 Why is this REQUIRED for Session Authentication?

    # Session Authentication depends on:

    # Django login system

    # Browser sessions

    # Cookies

    # This line connects DRF to Django’s authentication system.

    # Without it:

    # No login button

    # No logout button

    # Session auth won’t work properly in browser
      
         
          
]