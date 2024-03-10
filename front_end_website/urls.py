from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='entry'),
    path('customer_order_tracking/orderId=<str:orderId>', customerOrderTracking, name='customer_order_tracking'),
    path('customer_order_invoice/orderId=<str:orderId>', customerorderInvoice, name='customer_order_invoice'),
    path('view_product_detail/productId=<str:productId>', viewProductDetails, name='view_product_detail'),
    # apis
    path('get_franchise_vs_ownStore_sale/', get_franchise_vs_ownStore_sale_analytics, name='get_franchise_vs_ownStore_sale'),
    path('get_customer_analytics/', get_customer_analytics, name='get_customer_analytics'),
    path('get_order_analytics/', get_order_analytics, name='get_order_analytics'),
    path('get_store_sale_analytics/', get_store_sale_analytics, name='get_store_sale_analytics'),
    path('get_store_customer_analytics/', get_store_customer_analytics, name='get_store_customer_analytics'),
    path('get_store_order_analytics/', get_store_order_analytics, name='get_store_order_analytics'),

    path('customer_eye_test/testId=<int:testId>', customerEyeTestPrint, name='customer_eye_test_print'),

]
