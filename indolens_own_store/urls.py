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
    path('manage_store_employees/', manageStoreEmployees, name='manage_store_employees'),
    path('manage_store_employees/view_employee/', viewEmployees, name='view_employee'),
    # Manage customers
    path('view_store_customers/', viewStoreCustomers, name='view_store_customers'),
    path('view_store_customers/view_store_customer_details/', viewStoreCustomerDetails, name='view_store_customer_details'),
    # orders management
    path('all_store_orders/', allStoreOrders, name='all_store_orders'),
    path('pending_store_orders/', pendingStoreOrders, name='pending_store_orders'),
    path('received_store_orders/', receivedStoreOrders, name='received_store_orders'),
    path('processing_store_orders/', processingStoreOrders, name='processing_store_orders'),
    path('ready_store_orders/', readyStoreOrders, name='ready_store_orders'),
    path('delivered_store_orders/', deliveredStoreOrders, name='delivered_store_orders'),
    path('cancelled_store_orders/', cancelledStoreOrders, name='cancelled_store_orders'),
    path('refunded_store_orders/', refundedStoreOrders, name='refunded_store_orders'),
    path('order_details_store/', orderDetails, name='order_details_store'),
    # inventory items
    path('manage_store_inventory_products/', storeInventoryProducts, name='manage_store_inventory_products'),
    path('manage_store_out_of_stock/', inventoryOutOfStock, name='manage_store_out_of_stock'),
    path('move_stocks_store/', moveStocksStore, name='move_stocks_store'),
    # stock request management
    path('create_request_store/', createStockRequestStore, name='create_request_store'),
    path('all_stock_store_requests/', viewAllStockRequestsStore, name='all_stock_store_requests'),
    path('pending_store_stock_requests/', viewPendingStockRequestsStore, name='pending_store_stock_requests'),
    path('completed_store_stock_requests/', viewCompletedStockRequestsStore, name='completed_store_stock_requests'),
    path('rejected_store_stock_requests/', viewRejectedStockRequestsStore, name='rejected_store_stock_requests'),
    # Make sale
    path('own_store_make_sale/', makeSaleOwnStore, name='own_store_make_sale'),
    path('all_expenses_store/', allExpenseStore, name='all_expenses_store'),
    path('all_expenses_store/add_expense_store/', dashboard, name='add_expense_store'),
]
