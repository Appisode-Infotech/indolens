from django.urls import path
from .views import *

urlpatterns = [
    # start
    path('', index, name='own_store_index'),
    # auth
    path('login/', login, name='own_store_login'),
    path('forgot_password/', forgotPassword, name='own_store_forgot_password'),
    path('reset_password/', resetPassword, name='own_store_reset_password'),
    # Dashboard
    path('own_store_dashboard/', dashboard, name='own_store_dashboard'),
    path('dashboard/', dashboard, name='manage_store_employees'),
    # manage store Employee
    path('manage_store_employees/', dashboard, name='manage_store_employees'),
    # Manage customers
    path('view_store_customers/', dashboard, name='view_store_customers'),
    # orders management
    path('all_store_orders/', dashboard, name='all_store_orders'),
    path('pending_store_orders/', dashboard, name='pending_store_orders'),
    path('received_store_orders/', dashboard, name='received_store_orders'),
    path('processing_store_orders/', dashboard, name='processing_store_orders'),
    path('ready_store_orders/', dashboard, name='ready_store_orders'),
    path('delivered_store_orders/', dashboard, name='delivered_store_orders'),
    path('cancelled_store_orders/', dashboard, name='cancelled_store_orders'),
    path('refunded_store_orders/', dashboard, name='refunded_store_orders'),
    path('order_store_details/', dashboard, name='order_store_details'),


    path('manage_store_out_of_stock/', dashboard, name='manage_store_out_of_stock'),
    path('move_stocks_store/', dashboard, name='move_stocks_store'),
    path('manage_store_inventory_products/', dashboard,name='manage_store_inventory_products'),
    path('all_stock_store_requests/', dashboard,name='all_stock_store_requests'),
    path('pending_store_stock_requests/', dashboard,name='pending_store_stock_requests'),
    path('completed_store_stock_requests/', dashboard,name='completed_store_stock_requests'),
    path('rejected_store_stock_requests/', dashboard,name='rejected_store_stock_requests'),
]
