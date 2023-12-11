from django.urls import path

from .views import *
from django.conf.urls.static import static
from django.urls import path, include
from django.urls import re_path


from indolens import settings

urlpatterns = [
    # start
    path('', home, name='index'),
    # auth
    path('login/', login, name='login'),
    path('admin_logout/', adminLogout, name='admin_logout'),
    path('forgot_password/', forgotPassword, name='forgot_password'),
    path('reset_password/code=<str:code>', resetPassword, name='reset_password'),
    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
    # own store management
    path('create_own_store/', createOwnStore, name='create_own_store'),
    path('manage_own_stores/status=<str:status>', manageOwnStores, name='manage_own_stores'),
    path('manage_own_stores/view_own_store/storeId=<int:ownStoreId>', viewOwnStore, name='view_own_store'),
    path('manage_own_stores/edit_own_store/storeId=<int:ownStoreId>', editOwnStore, name='edit_own_store'),
    path('manage_own_stores/enable_disable_own_store/storeId=<int:ownStoreId>/status=<int:status>/route=<str:route>',
         enableDisableOwnStore,
         name='enable_disable_own_store'),
    # franchise store management
    path('create_franchise_store/', createFranchiseStore, name='create_franchise_store'),
    path('manage_Franchise_stores/status=<str:status>', manageFranchiseStores, name='manage_Franchise_stores'),
    path('manage_Franchise_stores/view_franchise_store/storeId=<int:franchiseStoreId>', viewFranchiseStore,
         name='view_franchise_store'),
    path('manage_Franchise_stores/edit_franchise_store/storeId=<int:franchiseStoreId>', editFranchiseStore,
         name='edit_franchise_store'),
    path(
        'manage_Franchise_stores/enable_disable_franchise_store/storeId=<int:franchiseStoreId>/status=<int:status>/route=<str:route>',
        enableDisableFranchiseStore, name='enable_disable_franchise_store'),
    # inventory management
    path('manage_out_of_stock/', manageCentralInventoryOutOfStock, name='manage_out_of_stock'),
    path('manage_central_inventory_products/status=<str:status>', manageCentralInventoryProducts,
         name='manage_central_inventory_products'),
    path('manage_central_inventory_products/add_products/', centralInventoryAddProducts, name='add_products'),
    path('manage_central_inventory_products/update_product/productId=<str:productId>', centralInventoryUpdateProduct,
         name='update_product'),
    path('manage_central_inventory_products/update_product_images/productId=<str:productId>', centralInventoryUpdateProductImages,
         name='update_product_images'),
    path(
        'manage_central_inventory_products/<str:filter>/enable_disable_product/productId=<str:productId>/status=<str:status>',
        centralInventoryUpdateProductStatus, name='enable_disable_product'),
    path('manageMoveStocks/', manageMoveStocks, name='manageMoveStocks'),
    path('manageMoveStocks/move_a_stock/', manageMoveAStock, name='move_a_stock'),
    path('manageMoveStocks/restock_products/status=<str:status>', restockProduct, name='restock_products'),
    path('manageMoveStocks/restockProductOutOfStock', restockProductOutOfStock, name='restockProductOutOfStock'),
    path('all_stock_requests/', viewAllStockRequests, name='all_stock_requests'),
    path('pending_stock_requests/', viewPendingStockRequests, name='pending_stock_requests'),
    path('completed_stock_requests/', viewCompletedStockRequests, name='completed_stock_requests'),
    path('rejected_stock_requests/', viewRejectedStockRequests, name='rejected_stock_requests'),
    path('change_stock_request_status/route=<str:route>/requestId=<int:requestId>/status=<int:status>',
         changeStockRequestStatus, name='change_stock_request_status'),
    # masters management
    path('manage_central_inventory_category/', manageMastersCategory, name='manage_central_inventory_category'),
    path('manage_central_inventory_category/add_product_category/', addProductCategory, name='add_product_category'),
    path('manage_central_inventory_category/edit_product_category/categoryId=<int:categoryId>', editProductCategory, name='edit_product_category'),
    path(
        'manage_central_inventory_category/enable_disable_product_category/categoryId=<int:categoryId>/status=<int:status>',
        enableDisableProductCategory, name='enable_disable_product_category'),
    path('manage_central_inventory_brands/', manageMastersBrands, name='manage_central_inventory_brands'),
    path('manage_central_inventory_brands/add_product_brand/', addMastersBrands, name='add_product_brand'),
    path('manage_central_inventory_brands/edit_product_brand/brandId=<int:brandId>', editMastersBrands, name='edit_product_brand'),
    path('manage_central_inventory_brands/enable_disable_product_brand/brandId=<int:brandId>/status=<int:status>',
         enableDisableMastersBrands, name='enable_disable_product_brand'),
    path('manage_central_inventory_shapes/', manageMastersShapes, name='manage_central_inventory_shapes'),
    path('manage_central_inventory_shapes/add_frame_shape/', addMastersShapes, name='add_frame_shape'),
    path('manage_central_inventory_shapes/edit_frame_shape/shapeId=<int:shapeId>', editMastersShapes, name='edit_frame_shape'),
    path('manage_central_inventory_shapes/enable_disable_frame_shape/shapeId=<int:shapeId>/status=<int:status>',
         enableDisableMastersShapes, name='enable_disable_frame_shape'),
    path('manage_central_inventory_frame_types/', manageMastersFrameType, name='manage_central_inventory_frame_types'),
    path('manage_central_inventory_frame_types/add_frame_type/', addMastersFrameType, name='add_frame_type'),
    path('manage_central_inventory_frame_types/edit_frame_type/frameId=<int:frameId>', editMastersFrameType, name='edit_frame_type'),
    path('manage_central_inventory_frame_types/enable_disable_frame_type/frameId=<int:frametypeId>/status=<int:status>',
         enableDisableMastersFrameType, name='enable_disable_frame_type'),
    path('manage_central_inventory_color/', manageMastersColor, name='manage_central_inventory_color'),
    path('manage_central_inventory_color/add_master_color/', addMastersColor, name='add_master_color'),
    path('manage_central_inventory_color/edit_master_color/colorId=<int:colorId>', editMastersColor, name='edit_master_color'),
    path('manage_central_inventory_color/enable_disable_master_color/colorId=<int:colorId>/status=<int:status>',
         enableDisableMastersColor, name='enable_disable_master_color'),
    path('manage_central_inventory_materials/', manageMastersMaterials, name='manage_central_inventory_materials'),
    path('manage_central_inventory_materials/add_master_material/', addMastersMaterials, name='add_master_material'),
    path('manage_central_inventory_materials/edit_master_material/materialId=<int:materialId>', editMastersMaterials, name='edit_master_material'),
    path(
        'manage_central_inventory_materials/enable_disable_master_material/materialId=<int:materialId>/status=<int:status>',
        enableDisableMastersMaterials, name='enable_disable_master_material'),
    path('manage_central_inventory_units/', manageMastersUnits, name='manage_central_inventory_units'),
    path('manage_central_inventory_units/add_Master_units', addMastersUnits, name='add_Master_units'),
    path('manage_central_inventory_units/edit_master_units/unitsId=<int:unitId>', editMastersUnits, name='edit_master_units'),
    path('manage_central_inventory_units/enable_disable_master_units/unitsId=<int:unitId>/status=<int:status>',
         enableDisableMastersUnits, name='enable_disable_master_units'),
    # customers
    path('view_customers/', viewAllCustomers, name='view_customers'),
    path('view_customers/customer_details/customerId=<int:customerId>', viewCustomerDetails, name='customer_details'),
    # indolens staff
    # sub admins
    path('manage_sub_admins/status=<str:status>', manageSubAdmins, name='manage_sub_admins'),
    path('manage_sub_admins/create_sub_admin/', createSubAdmin, name='create_sub_admin'),
    path('manage_sub_admins/edit_sub_admin/subAdminId=<int:subAdminId>', editSubAdmin, name='edit_sub_admin'),
    path('manage_sub_admins/update_sub_admin_documents/subAdminId=<int:subAdminId>', updateSubAdminDocuments,
         name='update_sub_admin_documents'),
    path('manage_sub_admins/view_sub_admin/subAdminId=<int:subAdminId>', viewSubAdmin, name='view_sub_admin'),
    path('manage_sub_admins/enable_disable_sub_admin/route<str:route>/subAdminId=<int:subAdminId>/status=<int:status>',
         enableDisableSubAdmin, name='enable_disable_sub_admin'),

    # store managers
    path('manage_store_managers/status=<str:status>', manageStoreManagers, name='manage_store_managers'),
    path('manage_store_managers/create_store_manager/', createStoreManager, name='create_store_manager'),
    path('manage_store_managers/edit_store_manager/managerId=<int:storeManagerId>', editStoreManager,
         name='edit_store_manager'),
    path('manage_store_managers/update_store_manager_documents/managerId=<int:storeManagerId>',
         updateStoreManagerDocuments, name='update_store_manager_documents'),
    path('manage_store_managers/view_store_manager/managerId=<int:storeManagerId>', viewStoreManager,
         name='view_store_manager'),
    path(
        'manage_store_managers/enable_disable_store_manager/route=<str:route>/managerId=<int:storeManagerId>/status=<int:status>',
        enableDisableStoreManager, name='enable_disable_store_manager'),

    # store franchise owners
    path('manage_franchise_owners/status=<str:status>', manageFranchiseOwners, name='manage_franchise_owners'),
    path('manage_franchise_owners/create_franchise_owner/', createFranchiseOwners, name='create_franchise_owner'),
    path('manage_franchise_owners/edit_franchise_owner/franchiseOwnerId=<int:franchiseOwnersId>', editFranchiseOwners,
         name='edit_franchise_owner'),
    path('manage_franchise_owners/update_franchise_owner_documents/franchiseOwnerId=<int:franchiseOwnersId>',
         updateFranchiseOwnersDocuments, name='update_franchise_owner_documents'),
    path('manage_franchise_owners/view_franchise_owner/franchiseOwnerId=<int:franchiseOwnersId>', viewFranchiseOwners,
         name='view_franchise_owner'),
    path(
        'manage_franchise_owners/enable_disable_franchise_owner/route=<str:route>/franchiseOwnerId=<int:franchiseOwnersId>/status=<int:status>',
        enableDisableFranchiseOwner, name='enable_disable_franchise_owner'),

    # area heads
    path('manage_area_head/status=<str:status>', manageAreaHead, name='manage_area_head'),
    path('manage_area_head/create_area_head/', createAreaHead, name='create_area_head'),
    path('manage_area_head/edit_area_head/areaHeadId=<int:areaHeadId>', editAreaHead, name='edit_area_head'),
    path('manage_area_head/update_area_head_documents/areaHeadId=<int:areaHeadId>', UpdateAreaHeadDocuments,
         name='update_area_head_documents'),
    path('manage_area_head/view_area_head/areaHeadId=<int:areaHeadId>', viewAreaHead, name='view_area_head'),
    path('manage_area_head/enable_disable_area_head/route<str:route>/areaHeadId=<int:areaHeadId>/status=<int:status>',
         enableDisableAreaHead,
         name='enable_disable_area_head'),
    # marketing head
    path('manage_marketing_head/status=<str:status>', manageMarketingHead, name='manage_marketing_head'),
    path('manage_marketing_head/create_marketing_head/', createMarketingHead, name='create_marketing_head'),
    path('manage_marketing_head/edit_marketing_head/marketingHeadId=<int:marketingHeadId>', editMarketingHead,
         name='edit_marketing_head'),
    path('manage_marketing_head/update_marketing_head_documents/marketingHeadId=<int:marketingHeadId>',
         updateMarketingHeadDocuments, name='update_marketing_head_documents'),
    path('manage_marketing_head/view_marketing_head/marketingHeadId=<int:marketingHeadId>', viewMarketingHead,
         name='view_marketing_head'),
    path(
        'manage_marketing_head/enable_disable_marketing_head/route=<str:route>/marketingHeadId=<int:marketingHeadId>/status=<int:status>',
        enableDisableMarketingHead, name='enable_disable_marketing_head'),

    # manage optimetry
    path('manage_store_optimetry/status=<str:status>', manageOptimetry, name='manage_store_optimetry'),
    path('manage_store_optimetry/create_optimetry/', createOptimetry, name='create_optimetry'),
    path('manage_store_optimetry/edit_optimetry/optimetryId=<int:ownOptimetryId>', editOptimetry,
         name='edit_optimetry'),
    path('manage_store_optimetry/update_optimetry_documents/optimetryId=<int:ownOptimetryId>', updateOptimetryDocuments,
         name='update_optimetry_documents'),
    path('manage_store_optimetry/view_optimetry/optimetryId=<int:ownOptimetryId>', viewOptimetry,
         name='view_optimetry'),
    path(
        'manage_store_optimetry/enable_disable_optimetry/route<str:route>/optimetryId=<int:ownOptimetryId>/status=<int:status>',
        enableDisableOptimetry, name='enable_disable_optimetry'),

    # manage franchise optimetry
    path('manage_franchise_optimetry/status=<str:status>', manageFranchiseOptimetry, name='manage_franchise_optimetry'),
    path('manage_franchise_optimetry/create_franchise_optimetry/', createFranchiseOptimetry,
         name='create_franchise_optimetry'),
    path('manage_franchise_optimetry/edit_franchise_optimetry/optimetryId=<int:franchiseOptimetryId>',
         editFranchiseOptimetry, name='edit_franchise_optimetry'),
    path('manage_franchise_optimetry/update_franchise_optimetry_documents/optimetryId=<int:franchiseOptimetryId>',
         updateFranchiseOptimetryDocuments, name='update_franchise_optimetry_documents'),
    path('manage_franchise_optimetry/view_franchise_optimetry/optimetryId=<int:franchiseOptimetryId>',
         viewFranchiseOptimetry, name='view_franchise_optimetry'),
    path(
        'manage_franchise_optimetry/enable_disable_franchise_optimetry/route=<str:route>/optimetryId=<int:franchiseOptimetryId>/status=<int:status>',
        enableDisableFranchiseOptimetry, name='enable_disable_franchise_optimetry'),

    # manage sales executive
    path('manage_store_sales_executives/status=<str:status>', manageSaleExecutives,
         name='manage_store_sales_executives'),
    path('manage_store_sales_executives/create_sales_executives/', createSaleExecutives,
         name='create_sales_executives'),
    path('manage_store_sales_executives/edit_sales_executives/salesExecutiveId=<int:ownSaleExecutivesId>',
         editSaleExecutives, name='edit_sales_executives'),
    path('manage_store_sales_executives/update_sales_executives_documents/salesExecutiveId=<int:ownSaleExecutivesId>',
         updateSaleExecutivesDocuments, name='update_sales_executives_documents'),
    path(
        'manage_store_sales_executives/enable_disable_sales_executive/route=<str:route>/saleExecutivesId=<int:ownSaleExecutivesId>/status=<int:status>',
        enableDisableSaleExecutives, name='enable_disable_sales_executive'),
    path('manage_store_sales_executives/view_sales_executives/salesExecutiveId=<int:ownSaleExecutivesId>',
         viewSaleExecutives,
         name='view_sales_executives'),

    # manage franchise sales executive
    path('manage_franchise_sales_executives/status=<str:status>', manageFranchiseSaleExecutives,
         name='manage_franchise_sales_executives'),
    path('manage_franchise_sales_executives/create_sales_executives/', createFranchiseSaleExecutives,
         name='create_franchise_sales_executives'),
    path('manage_franchise_sales_executives/edit_sales_executives/salesExecutiveId=<int:franchiseSaleExecutivesId>',
         editFranchiseSaleExecutives, name='edit_franchise_sales_executives'),
    path(
        'manage_franchise_sales_executives/update_franchise_sales_executives_documents/salesExecutiveId=<int:franchiseSaleExecutivesId>',
        updateFranchiseSaleExecutivesDocuments, name='update_franchise_sales_executives_documents'),
    path(
        'manage_franchise_sales_executives/enable_disable_sales_executive/route=<str:route>/saleExecutivesId=<int:franchiseSaleExecutivesId>/status=<int:status>',
        enableDisableFranchiseSaleExecutives, name='enable_disable_franchise_sales_executive'),
    path('manage_franchise_sales_executives/view_sales_executives/salesExecutiveId=<int:franchiseSaleExecutivesId>',
         viewFranchiseSaleExecutives,
         name='view_franchise_sales_executives'),
    # manage accountant
    path('manage_accountant/status=<str:status>', manageAccountant, name='manage_accountant'),
    path('manage_accountant/create_accountant/', createAccountant, name='create_accountant'),
    path('manage_accountant/edit_accountant/accountantId=<int:accountantId>', editAccountant, name='edit_accountant'),
    path('manage_accountant/update_accountant_documents/accountantId=<int:accountantId>', updateAccountantDocuments,
         name='update_accountant_documents'),
    path('manage_accountant/view_accountant/accountantId=<int:accountantId>', viewAccountant, name='view_accountant'),
    path('manage_accountant/enable_disable_accountant/route=<str:route>/accountantId=<int:accountantId>/status=<int:status>',
         enableDisableAccountant, name='enable_disable_accountant'),
    # manage lab tech
    path('manage_lab_technician/status=<str:status>', manageLabTechnician, name='manage_lab_technician'),
    path('manage_lab_technician/create_lab_technician/', createLabTechnician, name='create_lab_technician'),
    path('manage_lab_technician/edit_lab_technician/labTechnicianId=<int:labTechnicianId>', editLabTechnician,
         name='edit_lab_technician'),
    path('manage_lab_technician/update_lab_technician_documents/labTechnicianId=<int:labTechnicianId>',
         updateLabTechnicianDocuments, name='update_lab_technician_documents'),
    path('manage_lab_technician/view_lab_technician/labTechnicianId=<int:labTechnicianId>', viewLabTechnician,
         name='view_lab_technician'),
    path(
        'manage_lab_technician/enable_disable_lab_technician/route=<str:route>/labTechnicianId=<int:labTechnicianId>/status=<int:status>',
        enableDisableLabTechnician, name='enable_disable_lab_technician'),

    # Own store other employees
    path('manage_store_other_employees/status=<str:status>', manageOtherEmployees, name='manage_store_other_employees'),
    path('manage_store_other_employees/create_other_employees/', createOtherEmployees, name='create_other_employees'),
    path('manage_store_other_employees/edit_other_employees/ownEmployeeId=<int:ownEmployeeId>', editOtherEmployees,
         name='edit_other_employees'),
    path('manage_store_other_employees/update_other_employees_documents/ownEmployeeId=<int:ownEmployeeId>',
         updateOtherEmployeesDocuments, name='update_other_employees_documents'),
    path('manage_store_other_employees/view_other_employees/ownEmployeeId=<int:ownEmployeeId>', viewOtherEmployees,
         name='view_other_employees'),
    path(
        'manage_store_other_employees/enable_disable_other_employees/route=<str:route>/ownEmployeeId=<int:ownEmployeeId>/status=<int:status>',
        enableDisableOtherEmployees, name='enable_disable_other_employees'),

    # Franchise other employees
    path('manage_franchise_other_employees/status=<str:status>', manageFranchiseOtherEmployees,
         name='manage_franchise_other_employees'),
    path('manage_franchise_other_employees/create_other_employees/', createFranchiseOtherEmployees,
         name='create_franchise_other_employees'),
    path('manage_franchise_other_employees/edit_other_employees/otherEmpId=<int:franchiseEmployeeId>',
         editFranchiseOtherEmployees,
         name='edit_franchise_other_employees'),
    path('manage_franchise_other_employees/update_franchise_other_employees_documents/otherEmpId=<int:franchiseEmployeeId>',
         updateFranchiseOtherEmployeesDocuments, name='update_franchise_other_employees_documents'),
    path('manage_franchise_other_employees/view_other_employees/otherEmpId=<int:franchiseEmployeeId>',
         viewFranchiseOtherEmployees,
         name='view_franchise_other_employees'),
    path(
        'manage_franchise_other_employees/enable_disable_other_employees/route=<str:route>/otherEmpId=<int:franchiseEmployeeId>/status=<int:status>',
        enableDisableFranchiseOtherEmployees, name='enable_disable_franchise_other_employees'),
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
    path('manage_labs/edit_lab/labId=<int:labId>', editLab, name='edit_lab'),
    path('manage_labs/view_lab/labId=<int:labId>', viewLab, name='view_lab'),
    path('manage_labs/enable_disable_lab/labId=<int:labId>/status=<int:status>', enableDisableLab,
         name='enable_disable_lab'),
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

    # assign/un assign Own Store manager
    path('assign_manager_own_store/route<str:route>', assignManagerOwnStore, name='assign_manager_own_store'),
    path('un_assign_manager_own_store/route<str:route>/empId=<int:empId>/storeId=<int:storeId>',
         unAssignManagerOwnStore,
         name='un_assign_manager_own_store'),

    # assign/un assign Own Store optimetry
    path('assign_optimetry_own_store/route<str:route>', assignOptimetryOwnStore, name='assign_optimetry_own_store'),
    path('un_assign_optimetry_own_store/route<str:route>/empId=<int:empId>/storeId=<int:storeId>',
         unAssignOptimetryOwnStore,
         name='un_assign_optimetry_own_store'),

    # assign/un assign Own store Sales Executive
    path('assign_sales_executive_own_store/route=<str:route>', assignSalesExecutiveOwnStore,
         name='assign_sales_executive_own_store'),
    path(
        'un_assign_sales_executive_own_store/route=<str:route>/salesExecutiveId=<int:salesExecutiveId>/storeId=<int:storeId>',
        unAssignSalesExecutiveOwnStore,
        name='un_assign_sales_executive_own_store'),

    # assign/un assign Own store Housekeeping
    path('assign_other_employee_own_store/route=<str:route>', assignOtherEmployeeOwnStore,
         name='assign_other_employee_own_store'),
    path(
        'un_assign_other_employee_own_store/route=<str:route>/otherEmployeeId=<int:otherEmployeeId>/storeId=<int:storeId>',
        unAssignOtherEmployeeOwnStore,
        name='un_assign_other_employee_own_store'),

    # assign/un assign Franchise store Owner
    path('assign_franchise_store_owner/route=<str:route>', assignFranchiseStoreOwner,
         name='assign_franchise_store_owner'),
    path(
        'un_assign_franchise_store_owner/route=<str:route>/FranchiseOwnerId=<int:FranchiseOwnerId>/storeId=<int:storeId>',
        unAssignFranchiseStoreOwner,
        name='un_assign_franchise_store_owner'),

    # assign/un assign Franchise store Optimetry
    path('assign_franchise_store_optimetry/route=<str:route>', assignFranchiseStoreOptimetry,
         name='assign_franchise_store_optimetry'),
    path(
        'un_assign_franchise_store_optimetry/route=<str:route>/FranchiseOptimetryId=<int:FranchiseOptimetryId>/storeId=<int:storeId>',
        unAssignFranchiseStoreOptimetry,
        name='un_assign_franchise_store_optimetry'),

    # assign/un assign Franchise store Sales Executive
    path('assign_franchise_store_sales_executive/route=<str:route>', assignFranchiseStoreSalesExecutive,
         name='assign_franchise_store_sales_executive'),
    path(
        'un_assign_franchise_store_sales_executive/route=<str:route>/FranchiseSalesExecutiveId=<int:FranchiseSalesExecutiveId>/storeId=<int:storeId>',
        unAssignFranchiseStoreSalesExecutive,
        name='un_assign_franchise_store_sales_executive'),

    # assign/un assign Franchise store Housekeeping
    path('assign_franchise_store_other_employee/route=<str:route>', assignFranchiseStoreOtherEmployee,
         name='assign_franchise_store_other_employee'),
    path(
        'un_assign_franchise_store_other_employee/route=<str:route>/FranchiseOtherEmployeeId=<int:FranchiseOtherEmployeeId>/storeId=<int:storeId>',
        unAssignFranchiseStoreOtherEmployee,
        name='un_assign_franchise_store_other_employee'),

    # assign/un area head
    path('assign_area_head_own_store/', assignAreaHeadOwnStore, name='assign_area_head_own_store'),
    path('un_assign_area_head_own_store/?empId=<int:empId>/?storeId=<int:storeId>', unAssignAreaHeadOwnStore,
         name='un_assign_area_head_own_store'),


    # assign/un assign Lab Technician
    path('assign_lab_technician/route=<str:route>', assignLabTechnician,
         name='assign_lab_technician'),
    path(
        'un_assign_lab_technician/route=<str:route>/LabTechnicianId=<int:LabTechnicianId>/labId=<int:labId>',
        unAssignLabTechnician,
        name='un_assign_lab_technician'),


    # Delete Documents
    path(
            'manage_sub_admins/delete_sub_admin_document/subAdminId=<int:subAdminId>/documentURL=<str:documentURL>/document_Type=<str:document_Type>',
            deleteSubAdminDocuments, name='delete_sub_admin_document'),
    path(
            'manage_area_head/delete_area_head_document/areaHeadId=<int:areaHeadId>/documentURL=<str:documentURL>/document_Type=<str:document_Type>',
            deleteAreaHeadDocuments, name='delete_area_head_document'),
    path(
            'manage_marketing_head/delete_marketing_head_document/marketingHeadId=<int:marketingHeadId>/documentURL=<str:documentURL>/document_Type=<str:document_Type>',
            deleteMarketingHeadDocuments, name='delete_marketing_head_document'),
    path(
            'manage_accountant/delete_accountant_document/accountantId=<int:accountantId>/documentURL=<str:documentURL>/document_Type=<str:document_Type>',
            deleteAccountantDocuments, name='delete_accountant_document'),
    path(
            'manage_lab_technician/delete_lab_tech_document/labTechnicianId=<int:labTechnicianId>/documentURL=<str:documentURL>/document_Type=<str:document_Type>',
            deleteLabTechnicianDocuments, name='delete_lab_tech_document'),
    re_path(
        r'^manage_own_store_employee/delete_own_store_employee_document/employeeId=(?P<employeeId>[0-9]+)/documentURL=(?P<documentURL>.+?)/document_Type=(?P<document_Type>[^/]+)$',
        deleteOwnStoreEmployeeDocuments,
        name='delete_own_store_employee_document'
    ),
    re_path(
        r'^manage_franchise_store_employee/delete_franchise_store_employee_document/employeeId=(?P<employeeId>[0-9]+)/documentURL=(?P<documentURL>.+?)/document_Type=(?P<document_Type>[^/]+)$',
        deleteFranchiseStoreEmployeeDocuments,
        name='delete_franchise_store_employee_document'
    ),

    path(
            'manage_central_inventory_products/delete_product_image/productId=<int:productId>/imageURL=<str:imageURL>',
            deleteProductImage, name='delete_product_image'),
    re_path(
            r'^manage_central_inventory_products/delete_product_image/productId=(?P<productId>[0-9]+)/imageURL=(?P<imageURL>.+)$',
            deleteProductImage,
            name='delete_product_image'
        ),

    #Update Image

    path('manage_central_inventory_products/add_product_image/productId=<int:productId>',
            addProductImage, name='add_product_image'),
    path('manage_own_store_employee/add_own_store_employee_image/employeeId=<int:employeeId>',
            addOwnStoreEmployeeImage, name='add_own_store_employee_image'),
    path('manage_franchise_store_employee/add_franchise_store_employee_image/employeeId=<int:employeeId>',
            addFranchiseStoreEmployeeImage, name='add_franchise_store_employee_image'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
