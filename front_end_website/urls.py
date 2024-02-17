from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='entry'),
    path('customer_order_tracking/orderId=<str:orderId>', customerOrderTracking, name='customer_order_tracking'),
    path('view_product_detail/productId=<str:productId>', viewProductDetsils, name='view_product_detail'),
    # apis
    path('get_franchise_vs_ownStore_sale/', get_franchise_vs_ownStore_sale, name='get_franchise_vs_ownStore_sale'),

]
