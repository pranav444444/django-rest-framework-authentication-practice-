from rest_framework.routers import DefaultRouter
# from .views import CustomerViewSet
from .views import CustomerListView,CustomerCreateView,CustomerDestroyView,CustomerRetrieveView,CustomerUpdateView

from django.urls import path,include



# router = DefaultRouter()
# router.register('customers', CustomerViewSet, basename='customers')

# urlpatterns = [
#   path('',include(router.urls)),
#   path('auth/',include('rest_framework.urls',namespace='rest_framework'))
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
      
         
          
# ]

urlpatterns = [
    # Create & List
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer-create'),

    # Retrieve / Update / Delete (by ID)
    path('customers/<int:pk>/', CustomerRetrieveView.as_view(), name='customer-retrieve'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', CustomerDestroyView.as_view(), name='customer-delete'),

    # Session authentication (login/logout for browser)
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]