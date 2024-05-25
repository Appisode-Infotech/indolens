from django.urls import path

from .views import *
from indolens import settings
from django.conf.urls.static import static

urlpatterns = [
    # start
    path('', index, name='own_store_index'),
    # auth
    path('own_store_login/', login, name='own_store_login'),
    path('forgot_password/', forgotPassword, name='own_store_forgot_password'),
    path('reset_password/code=<str:code>', resetPassword, name='own_store_reset_password'),
    path('store_employee_logout/', storeEmployeeLogout, name='store_employee_logout'),
    # Dashboard
    path('own_store_dashboard/', dashboard, name='own_store_dashboard'),
    # manage store Employee
    path('manage_store_employees/', manageStoreEmployees, name='manage_store_employees'),
    path('manage_store_employees/view_employee/employeeId=<int:employeeId>', viewEmployees, name='view_employee'),

    path('manage_store_employees/view_franchise_employee/employeeId=<int:employeeId>', viewFranchiseEmployees, name='view_franchise_employee'),
    # Manage customers
    path('view_store_customers/', viewStoreCustomers, name='view_store_customers'),
    path('view_store_customers/view_store_customer_details/customerId=<int:customerId>', viewStoreCustomerDetails,
         name='view_store_customer_details'),

    # orders management
    path('all_store_orders/', allStoreOrders, name='all_store_orders'),
    path('dispatched_store_orders/', dispatchedStoreOrders, name='dispatched_store_orders'),
    path('new_store_orders/', newStoreOrders, name='new_store_orders'),
    path('processing_store_orders/', processingStoreOrders, name='processing_store_orders'),
    path('ready_lab_orders/', readylabOrders, name='ready_lab_orders'),
    path('completed_store_orders/', completedStoreOrders, name='completed_store_orders'),
    path('delivered_to_store_orders/', DeliveredStoreOrders, name='delivered_to_store_orders'),
    path('cancelled_store_orders/', cancelledStoreOrders, name='cancelled_store_orders'),
    path('refunded_store_orders/', refundedStoreOrders, name='refunded_store_orders'),
    path('order_details_store/orderId=<str:orderId>', orderDetails, name='order_details_store'),
    path('order_invoice_store/orderId=<str:orderId>', orderInvoice, name='order_invoice_store'),
    path('order_details_store/order_status_change/orderId=<str:orderId>/status=<str:status>', orderStatusChange,
         name='order_status_change'),
    path('order_details_store/order_payment_status_change/', orderPaymentStatusChange,
         name='order_payment_status_change'),

    # inventory items
    path('manage_store_inventory_products/', storeInventoryProducts, name='manage_store_inventory_products'),
    path('view_store_inventory_products/productId=<int:productId>', viewStoreInventoryProducts, name='view_store_inventory_products'),
    path('view_central_inventory_products/productId=<int:productId>', viewCentralInventoryProducts, name='view_central_inventory_products'),
    path('manage_store_out_of_stock/', inventoryOutOfStock, name='manage_store_out_of_stock'),
    # stock request management
    path('create_request_store/', createStockRequestStore, name='create_request_store'),
    path('all_stock_store_requests/', viewAllStockRequestsStore, name='all_stock_store_requests'),
    path('pending_store_stock_requests/', viewPendingStockRequestsStore, name='pending_store_stock_requests'),
    path('completed_store_stock_requests/', viewCompletedStockRequestsStore, name='completed_store_stock_requests'),
    path('rejected_store_stock_requests/', viewRejectedStockRequestsStore, name='rejected_store_stock_requests'),
    path('request_delivery_status_change/requestId=<int:requestId>/status=<int:status>', stockRequestDeliveryStatusChange, name='request_delivery_status_change'),
    # Make sale
    path('own_store_make_sale/', makeSaleOwnStore, name='own_store_make_sale'),
    path('all_expenses_store/', allExpenseStore, name='all_expenses_store'),

    path('own_store_eye_test/', ownStoreEyeTest, name='own_store_eye_test'),
    path('get_eye_test/', getOwnStoreEyeTest, name='get_eye_test'),
    path('get_eye_test_by_id/testId=<int:testId>', getOwnStoreEyeTestById, name='get_eye_test_by_id'),
    path('print_eye_test/testId=<int:testId>', ownStoreEyeTestPrint, name='own_store_eye_test_print'),

    path('own_store_contact_lens_power_card/saleId=<str:saleId>', ownStoreContactLensPowerCard,
             name='own_store_contact_lens_power_card'),
    path('own_store_lens_power_card/saleId=<str:saleId>', ownStoreLensPowerCard,
             name='own_store_lens_power_card'),
    path('own_store_job_item_details/saleId=<str:saleId>', viewJobItemDetails,
             name='own_store_job_item_details'),
    path('own_store_job_authenticity_card/saleId=<str:saleId>/frame=<str:frame>', viewJobAuthenticityCard,
             name='own_store_job_authenticity_card'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

