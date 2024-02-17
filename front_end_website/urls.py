from django.urls import path

from . import views
from .views import customerOrderTracking, viewProductDetsils

urlpatterns = [
    path('', views.index, name='entry'),
    path('customer_order_tracking/orderId=<str:orderId>', customerOrderTracking, name='customer_order_tracking'),
    path('view_product_detail/productId=<str:productId>', viewProductDetsils, name='view_product_detail'),
]
