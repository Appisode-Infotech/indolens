from django.urls import path

from .views import *

urlpatterns = [
    # start
    path('', index, name='franchise_store_index'),
    # auth
    path('login/', login, name='franchise_store_login'),
    path('franchise_store_forgot_password/', forgotPassword, name='franchise_store_forgot_password'),
    path('franchise_store_reset_password/code=<str:code>', resetPassword, name='franchise_store_reset_password'),
    path('franchise_owner_logout/', franchiseOwnerLogout, name='franchise_owner_logout'),
    # Dashboard
    path('franchise_store_dashboard/', dashboard, name='franchise_store_dashboard'),
    # Manage customers
    path('view_franchise_store_customers/', viewAllCustomersFranchise, name='view_franchise_store_customers'),
    path('view_franchise_store_customers/view_franchise_store_customer_details/customerId=<int:customerId>', viewCustomerDetailsFranchise,
         name='view_franchise_store_customer_details'),
    # Manage ownEmployee
    path('view_franchise_store_employee/', viewAllEmployeFranchise, name='view_franchise_store_employee'),
    path('view_franchise_store_employee/view_franchise_store_employee_details/employeeId=<int:employeeId>', viewEmployeeDetailsFranchise,
         name='view_franchise_store_employee_details'),

    # orders management
    path('all_franchise_store_orders/', allFranchiseOrders, name='all_franchise_store_orders'),
    path('dispatched_franchise_store_orders/', dispatchedFranchiseOrders, name='dispatched_franchise_store_orders'),
    path('new_franchise_store_orders/', newFranchiseOrders, name='new_franchise_store_orders'),
    path('processing_franchise_store_orders/', processingFranchiseOrders, name='processing_franchise_store_orders'),
    path('ready_franchise_store_orders/', readyFranchiseOrders, name='ready_franchise_store_orders'),
    path('delivered_franchise_store_orders/', deliveredFranchiseOrders, name='delivered_franchise_store_orders'),
    path('cancelled_franchise_store_orders/', cancelledFranchiseOrders, name='cancelled_franchise_store_orders'),
    path('refunded_franchise_store_orders/', refundedFranchiseOrders, name='refunded_franchise_store_orders'),
    path('order_details_franchise_store/orderId=<str:orderId>', orderDetailsFranchise, name='order_details_franchise_store'),
    path('order_details_franchise_store/franchise_order_status_change/orderId=<str:orderId>/status=<str:status>',
         franchiseOrderStatusChange, name='franchise_order_status_change'),
    path('order_details_franchise_store/franchise_payment_status_change/orderId=<str:orderId>/status=<str:status>',
         franchisePaymentStatusChange, name='franchise_payment_status_change'),

    # inventory items
    path('manage_franchise_store_inventory_products/', franchiseInventoryProducts,
         name='manage_franchise_store_inventory_products'),
    path('manage_franchise_store_out_of_stock/', inventoryOutOfStockFranchise,
         name='manage_franchise_store_out_of_stock'),

    # stock request management
    path('create_request_franchise_store/', createStockRequestFranchise, name='create_request_franchise_store'),
    path('all_stock_franchise_store_requests/', viewAllStockRequestsFranchise,
         name='all_stock_franchise_store_requests'),
    path('pending_franchise_store_stock_requests/', viewPendingStockRequestsFranchise,
         name='pending_franchise_store_stock_requests'),
    path('completed_franchise_store_stock_requests/', viewCompletedStockRequestsFranchise,
         name='completed_franchise_store_stock_requests'),
    path('rejected_franchise_store_stock_requests/', viewRejectedStockRequestsFranchise,
         name='rejected_franchise_store_stock_requests'),
    # Make sale
    path('franchise_store_make_sale/', makeSaleFranchiseStore, name='franchise_store_make_sale'),
    path('all_expenses_franchise_store/', allExpenseFranchise, name='all_expenses_franchise_store'),
]
