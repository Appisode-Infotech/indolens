from django.urls import path

from . import views
from .views import customerOrderTracking, get_franchise_vs_ownStore_sale

urlpatterns = [
    path('', views.index, name='entry'),
    path('customer_order_tracking/orderId=<str:orderId>', customerOrderTracking, name='customer_order_tracking'),
    # apis
    path('get_franchise_vs_ownStore_sale/', get_franchise_vs_ownStore_sale, name='get_franchise_vs_ownStore_sale'),

]
