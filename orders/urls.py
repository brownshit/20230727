from django.urls import path
from . import views
#phone number create , list
# from .views import PhoneNumberCreateView, PhoneNumberListView, call_external_api

urlpatterns = [
    # #gpt-1
    # path('api/save_phone_number/', views.save_phone_number, name='save_phone_number'),
    # path('api/get_order_details/<int:order_id>/', views.get_order_details, name='get_order_details'),
    #gpt-2


    path('api/menu/', views.menu_list, name='menu_list'),
    path('api/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('api/remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('api/checkout/', views.checkout, name='checkout'),
    #git
    path('api/orders/', views.submit_order, name='submit_order'),
    
    # path('', views.index, name="index"),
    #phone number create , list
    # path('create/', PhoneNumberCreateView.as_view(), name='phone_create'),
    # path('list/', PhoneNumberListView.as_view(), name='phone_list'),
    # path('call_external_api/', call_external_api, name = 'call_external_api'),
]
#pip install django, djangorestframework, requests, Pillow