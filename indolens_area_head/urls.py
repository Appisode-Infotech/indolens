from django.urls import path

from .views import *

urlpatterns = [
    # start
    path('', index, name='index_area_head'),
    # auth
    path('login/', login, name='login_area_head'),
    path('logout_area_head/', areaHeadLogout, name='logout_area_head'),
    path('forgot_password/', forgotPassword, name='forgot_password_area_head'),
    path('reset_password/code=<str:code>', resetPassword, name='reset_password_area_head'),
    # Dashboard
    path('dashboard/', dashboard, name='dashboard_area_head'),
    # own store management
    path('manage_own_stores/status=<str:status>', manageOwnStores, name='manage_own_stores_area_head'),
    path('manage_own_stores/view_own_store/ownStoreId=<int:ownStoreId>', viewOwnStore, name='view_own_store_area_head'),
    # franchise store management
    path('manage_Franchise_stores/status=<str:status>', manageFranchiseStores, name='manage_Franchise_stores_area_head'),
    path('manage_Franchise_stores/view_franchise_store/?storeId=<int:fid>', viewFranchiseStore,
         name='view_franchise_store_area_head'),
    # inventory management
    path('manage_out_of_stock/', manageCentralInventoryOutOfStock, name='manage_out_of_stock_area_head'),
    path('manage_central_inventory_products/status=<str:status>', manageCentralInventoryProducts,
         name='manage_central_inventory_products_area_head'),
    path('manageMoveStocks/', manageMoveStocks, name='manageMoveStocks_area_head'),
    path('manageMoveStocks/move_a_stock/', manageMoveAStock, name='move_a_stock_area_head'),
    path('all_stock_requests/', viewAllStockRequests, name='all_stock_requests_area_head'),
    path('pending_stock_requests/', viewPendingStockRequests, name='pending_stock_requests_area_head'),
    path('completed_stock_requests/', viewCompletedStockRequests, name='completed_stock_requests_area_head'),
    path('rejected_stock_requests/', viewRejectedStockRequests, name='rejected_stock_requests_area_head'),
    # customers
    path('view_customers/', viewAllCustomers, name='view_customers_area_head'),
    path('view_customers/customer_details/', viewCustomerDetails, name='customer_details_area_head'),
    # store managers
    path('manage_store_managers/', manageStoreManagers, name='manage_store_managers_area_head'),
    path('manage_store_managers/view_store_manager/?managerId=<int:mid>', viewStoreManager,
         name='view_store_manager_area_head'),
    # store franchise owners
    path('manage_franchise_owners/', manageFranchiseOwners, name='manage_franchise_owners_area_head'),
    path('manage_franchise_owners/view_franchise_owner/?franchiseOwnerId=<int:foid>', viewFranchiseOwners,
         name='view_franchise_owner_area_head'),
    # marketing head
    path('manage_marketing_head/', manageMarketingHead, name='manage_marketing_head_area_head'),
    path('manage_marketing_head/view_marketing_head/?marketingHeadId=<int:mhid>', viewMarketingHead,
         name='view_marketing_head_area_head'),
    # manage optimetry
    path('manage_optimetry/', manageOptimetry, name='manage_optimetry_area_head'),
    path('manage_optimetry/view_optimetry/', viewOptimetry, name='view_optimetry_area_head'),
    # manage sales executive
    path('manage_sales_executives/', manageSaleExecutives, name='manage_sales_executives_area_head'),
    path('manage_sales_executives/view_sales_executives/?salesExecutiveId=<int:seid>', viewSaleExecutives,
         name='view_sales_executives_area_head'),
    # manage accountant
    path('manage_accountant/', manageAccountant, name='manage_accountant_area_head'),
    path('manage_accountant/view_accountant/?accountantId=<int:aid>', viewAccountant, name='view_accountant_area_head'),
    # manage lab tech
    path('manage_lab_technician/', manageLabTechnician, name='manage_lab_technician_area_head'),
    path('manage_lab_technician/view_lab_technician/?labTechnicianId=<int:ltid>', viewLabTechnician,
         name='view_lab_technician_area_head'),
    # housekeeping
    path('manage_other_employees/', manageOtherEmployees, name='manage_other_employees_area_head'),
    path('manage_other_employees/view_other_employees/empId=<int:empid>', viewOtherEmployees,
         name='view_other_employees_area_head'),
    # orders management
    path('all_orders/', viewAllOrders, name='all_orders_area_head'),
    path('pending_orders/', viewPendingOrders, name='pending_orders_area_head'),
    path('received_orders/', viewReceivedOrders, name='received_orders_area_head'),
    path('processing_orders/', viewProcessingOrders, name='processing_orders_area_head'),
    path('ready_orders/', viewReadyOrders, name='ready_orders_area_head'),
    path('delivered_orders/', viewDeliveredOrders, name='delivered_orders_area_head'),
    path('cancelled_orders/', viewCancelledOrders, name='cancelled_orders_area_head'),
    path('refunded_orders/', viewRefundedOrders, name='refunded_orders_area_head'),
    path('order_details/', viewOrderDetails, name='order_details_area_head'),
    # labs
    path('manage_labs/', manageLabs, name='manage_labs_area_head'),
    path('manage_labs/view_lab/?labId=<int:labid>', viewLab, name='view_lab_area_head'),
    path('manage_labs/view_active_jobs/', viewActiveJobs, name='view_active_jobs_area_head'),
    path('manage_labs/view_all_jobs/', viewAllJobs, name='view_all_jobs_area_head'),
    path('manage_labs/job_details/', jobDetails, name='job_details_area_head'),
    path('manage_authenticity_card/', manageAuthenticityCard, name='manage_authenticity_card_area_head'),
    # marketing
    path('manage_tasks/', viewOwnStore, name='manage_tasks_area_head'),
    path('manage_campaigns/', viewOwnStore, name='manage_campaigns_area_head'),
    path('view_product_details/', viewOwnStore, name='view_product_details_area_head'),
    path('all_notifications/', viewOwnStore, name='all_notifications_area_head'),
    path('manage_memberships/', viewOwnStore, name='manage_memberships_area_head'),
]
