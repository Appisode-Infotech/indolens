from django.urls import path

from .views import *

urlpatterns = [
    # start
    path('', index, name='index'),
    # auth
    path('login/', login, name='login'),
    path('forgot_password/', forgotPassword, name='forgot_password'),
    path('reset_password/', resetPassword, name='reset_password'),
    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
    # own store management
    path('create_own_store/', createOwnStore, name='create_own_store'),
    path('manage_own_stores/', manageOwnStores, name='manage_own_stores'),
    path('manage_own_stores/view_own_store/?storeId=<int:sid>', viewOwnStore, name='view_own_store'),
    path('manage_own_stores/edit_own_store/?storeId=<int:sid>', editOwnStore, name='edit_own_store'),
    # franchise store management
    path('create_franchise_store/', createFranchiseStore, name='create_franchise_store'),
    path('manage_Franchise_stores/', manageFranchiseStores, name='manage_Franchise_stores'),
    path('manage_Franchise_stores/view_franchise_store/?storeId=<int:fid>', viewFranchiseStore, name='view_franchise_store'),
    path('manage_Franchise_stores/edit_franchise_store/?storeId=<int:fid>', editFranchiseStore, name='edit_franchise_store'),
    # inventory management
    path('manage_out_of_stock/', manageCentralInventoryOutOfStock, name='manage_out_of_stock'),
    path('manage_central_inventory_products/', manageCentralInventoryProducts,
         name='manage_central_inventory_products'),
    path('manage_central_inventory_products/add_products/', centralInventoryAddProducts, name='add_products'),
    path('manageMoveStocks/', manageMoveStocks, name='manageMoveStocks'),
    path('manageMoveStocks/move_a_stock/', manageMoveAStock, name='move_a_stock'),
    path('all_stock_requests/', viewAllStockRequests, name='all_stock_requests'),
    path('pending_stock_requests/', viewPendingStockRequests, name='pending_stock_requests'),
    path('completed_stock_requests/', viewCompletedStockRequests, name='completed_stock_requests'),
    path('rejected_stock_requests/', viewRejectedStockRequests, name='rejected_stock_requests'),
    # masters management
    path('manage_central_inventory_category/', manageMastersCategory, name='manage_central_inventory_category'),
    path('manage_central_inventory_category/add_product_category/', addProductCategory, name='add_product_category'),
    path('manage_central_inventory_brands/', manageMastersBrands, name='manage_central_inventory_brands'),
    path('manage_central_inventory_brands/add_product_brand/', addMastersBrands, name='add_product_brand'),
    path('manage_central_inventory_shapes/', manageMastersShapes, name='manage_central_inventory_shapes'),
    path('manage_central_inventory_shapes/add_frame_shape/', addMastersShapes, name='add_frame_shape'),
    path('manage_central_inventory_frame_types/', manageMastersFrameType, name='manage_central_inventory_frame_types'),
    path('manage_central_inventory_frame_types/add_frame_type/', addMastersFrameType, name='add_frame_type'),
    path('manage_central_inventory_color/', manageMastersColor, name='manage_central_inventory_color'),
    path('manage_central_inventory_color/add_master_color/', addMastersColor, name='add_master_color'),
    path('manage_central_inventory_materials/', manageMastersMaterials, name='manage_central_inventory_materials'),
    path('manage_central_inventory_materials/add_master_material/', addMastersMaterials, name='add_master_material'),
    path('manage_central_inventory_units/', manageMastersUnits, name='manage_central_inventory_units'),
    # customers
    path('view_customers/', viewAllCustomers, name='view_customers'),
    path('view_customers/customer_details/', viewCustomerDetails, name='customer_details'),
    # indolens staff
    # sub admins
    path('manage_sub_admins/', manageSubAdmins, name='manage_sub_admins'),
    path('manage_sub_admins/create_sub_admin/', createSubAdmin, name='create_sub_admin'),
    path('manage_sub_admins/edit_sub_admin/', editSubAdmin, name='edit_sub_admin'),
    path('manage_sub_admins/view_sub_admin/', viewSubAdmin, name='view_sub_admin'),
    # store managers
    path('manage_store_managers/', manageStoreManagers, name='manage_store_managers'),
    path('manage_store_managers/create_store_manager/', createStoreManager, name='create_store_manager'),
    path('manage_store_managers/edit_store_manager/', editStoreManager, name='edit_store_manager'),
    path('manage_store_managers/view_store_manager/?managerId=<int:mid>', viewStoreManager, name='view_store_manager'),
    # store franchise owners
    path('manage_franchise_owners/', manageFranchiseOwners, name='manage_franchise_owners'),
    path('manage_franchise_owners/create_franchise_owner/', createFranchiseOwners, name='create_franchise_owner'),
    path('manage_franchise_owners/edit_franchise_owner/', editFranchiseOwners, name='edit_franchise_owner'),
    path('manage_franchise_owners/view_franchise_owner/', viewFranchiseOwners, name='view_franchise_owner'),
    # area heads
    path('manage_area_head/', manageAreaHead, name='manage_area_head'),
    path('manage_area_head/create_area_head/', createAreaHead, name='create_area_head'),
    path('manage_area_head/edit_area_head/', editAreaHead, name='edit_area_head'),
    path('manage_area_head/view_area_head/', viewAreaHead, name='view_area_head'),
    # marketing head
    path('manage_marketing_head/', manageMarketingHead, name='manage_marketing_head'),
    path('manage_marketing_head/create_marketing_head/', createMarketingHead, name='create_marketing_head'),
    path('manage_marketing_head/edit_marketing_head/', editMarketingHead, name='edit_marketing_head'),
    path('manage_marketing_head/view_marketing_head/', viewMarketingHead, name='view_marketing_head'),
    # manage optimetry
    path('manage_optimetry/', manageOptimetry, name='manage_optimetry'),
    path('manage_optimetry/create_optimetry/', createOptimetry, name='create_optimetry'),
    path('manage_optimetry/edit_optimetry/', editOptimetry, name='edit_optimetry'),
    path('manage_optimetry/view_optimetry/', viewOptimetry, name='view_optimetry'),
    # manage sales executive
    path('manage_sales_executives/', manageSaleExecutives, name='manage_sales_executives'),
    path('manage_sales_executives/create_sales_executives/', createSaleExecutives, name='create_sales_executives'),
    path('manage_sales_executives/edit_sales_executives/', editSaleExecutives, name='edit_sales_executives'),
    path('manage_sales_executives/view_sales_executives/', viewSaleExecutives, name='view_sales_executives'),
    # manage accountant
    path('manage_accountant/', manageAccountant, name='manage_accountant'),
    path('manage_accountant/create_accountant/', createAccountant, name='create_accountant'),
    path('manage_accountant/edit_accountant/', editAccountant, name='edit_accountant'),
    path('manage_accountant/view_accountant/', viewAccountant, name='view_accountant'),
    # manage lab tech
    path('manage_lab_technician/', manageLabTechnician, name='manage_lab_technician'),
    path('manage_lab_technician/create_lab_technician/', createLabTechnician, name='create_lab_technician'),
    path('manage_lab_technician/edit_lab_technician/', editLabTechnician, name='edit_lab_technician'),
    path('manage_lab_technician/view_lab_technician/', viewLabTechnician, name='view_lab_technician'),
    # housekeeping
    path('manage_other_employees/', manageOtherEmployees, name='manage_other_employees'),
    path('manage_other_employees/create_other_employees/', createOtherEmployees, name='create_other_employees'),
    path('manage_other_employees/edit_other_employees/', editOtherEmployees, name='edit_other_employees'),
    path('manage_other_employees/view_other_employees/', viewOtherEmployees, name='view_other_employees'),
    # orders management
    path('all_orders/', viewAllOrders, name='all_orders'),
    path('pending_orders/', viewPendingOrders, name='pending_orders'),
    path('received_orders/', viewReceivedOrders, name='received_orders'),
    path('processing_orders/', viewProcessingOrders, name='processing_orders'),
    path('ready_orders/', viewReadyOrders, name='ready_orders'),
    path('delivered_orders/', viewDeliveredOrders, name='delivered_orders'),
    path('cancelled_orders/', viewCancelledOrders, name='cancelled_orders'),
    path('refunded_orders/', viewRefundedOrders, name='refunded_orders'),
    path('order_details/', viewOrderDetails, name='order_details'),
    # labs
    path('manage_labs/', manageLabs, name='manage_labs'),
    path('manage_labs/create_lab/', createLab, name='create_lab'),
    path('manage_labs/edit_lab/', editLab, name='edit_lab'),
    path('manage_labs/view_lab/', viewLab, name='view_lab'),
    path('manage_labs/view_active_jobs/', viewActiveJobs, name='view_active_jobs'),
    path('manage_labs/view_all_jobs/', viewAllJobs, name='view_all_jobs'),
    path('manage_labs/job_details/', jobDetails, name='job_details'),
    path('manage_authenticity_card/', manageAuthenticityCard, name='manage_authenticity_card'),
    path('manage_authenticity_card/create_authenticity_card/', createAuthenticityCard, name='create_authenticity_card'),
    # marketing
    path('manage_tasks/', viewOwnStore, name='manage_tasks'),
    path('manage_campaigns/', viewOwnStore, name='manage_campaigns'),
    path('view_product_details/', viewOwnStore, name='view_product_details'),
    path('all_notifications/', viewOwnStore, name='all_notifications'),
    path('manage_memberships/', viewOwnStore, name='manage_memberships'),
]
