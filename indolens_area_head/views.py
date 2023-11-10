from django.shortcuts import render, redirect

from indolens_admin.admin_controllers import own_store_controller, franchise_store_controller, store_manager_controller, \
    franchise_manager_controller, marketing_head_controller, sales_executives_controller, \
    accountant_controller, lab_technician_controller, other_employee_controller, lab_controller, \
    stores_inventory_controller, central_inventory_controller
from indolens_area_head.area_head_controller import area_head_auth_controller, stores_controller, \
    area_stores_inventory_controller, area_head_customers_controller
from indolens_area_head.area_head_model.area_head_req_models import area_head_auth_model
from indolens_own_store.own_store_controller import store_inventory_controller


# =================================ADMIN START======================================
def index(request):
    return redirect('login_area_head')


# =================================ADMIN AUTH======================================

def login(request):
    if request.method == 'POST':
        area_head_obj = area_head_auth_model.area_head_model_from_dict(request.POST)
        response, status_code = area_head_auth_controller.login(area_head_obj)
        if response['status']:
            request.session.clear()
            for data in response['area_head']:
                request.session.update({
                    'is_area_head_logged_in': True,
                    'id': data['area_head_id'],
                    'assigned_stores': data['assigned_stores'],
                    'name': data['name'],
                    'email': data['email'],
                    'profile_pic': data['profile_pic'],
                })
            return redirect('dashboard_area_head')
        else:
            return render(request, 'auth/sign_in.html', {"message": response['message']})
    else:
        return render(request, 'auth/sign_in.html')


def areaHeadLogout(request):
    request.session.clear()
    return redirect(login)


def forgotPassword(request):
    if request.method == 'POST':
        response, status_code = area_head_auth_controller.forgot_password(request.POST['email'])
        return render(request, 'auth/forgot_password.html',
                      {"message": response['message'], "status": response['status']})
    else:
        return render(request, 'auth/forgot_password.html', {"status": False})


def resetPassword(request, code):
    if request.method == 'POST':
        response, status_code = area_head_auth_controller.update_area_head_password(request.POST['password'],
                                                                            request.POST['email'])
        return render(request, 'auth/reset_password.html',
                      {"code": code, "message": response['message']})
    else:
        response, status_code = area_head_auth_controller.check_link_validity(code)
        print(response)
        return render(request, 'auth/reset_password.html',
                      {"code": code, "message": response['message'], "email": response['email']})


# =================================ADMIN DASH======================================

def dashboard(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'dashboard.html')
    else:
        return redirect('login_area_head')

# =================================ADMIN STORE MANAGEMENT======================================

def manageOwnStores(request, status):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = stores_controller.get_area_head_own_stores(status,
                                                                           request.session.get('assigned_stores'))
        return render(request, 'ownStore/manageOwnStores.html',
                      {"own_stores": response['own_stores'], "status": status})
    else:
        return redirect('login_area_head')


def viewOwnStore(request, ownStoreId):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = own_store_controller.get_own_store_by_id(ownStoreId)
        products_list, status_code = stores_inventory_controller.get_all_products_for_own_store(ownStoreId)
        store_stats, status_code = own_store_controller.get_own_storestore_stats(ownStoreId)
        return render(request, 'ownStore/ownStore.html',
                      {"store_data": response['own_stores'], "products_list": products_list['products_list'],
                       "total_employee_count": store_stats['total_employee_count'],
                       "total_customer_count": store_stats['total_customer_count']})
    else:
        return redirect('login_area_head')


def viewFranchiseStore(request, fid):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = franchise_store_controller.get_franchise_store_by_id(fid)
        return render(request, 'franchiseStores/franchiseStore.html',
                      {"franchise_store": response['franchise_store']})
    else:
        return redirect('login_area_head')

def manageFranchiseStores(request, status):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = stores_controller.get_area_head_franchise_stores(status)
        return render(request, 'franchiseStores/manageFranchiseStores.html',
                      {"franchise_store_list": response['franchise_store'], "status": status})
    else:
        return redirect('login_area_head')


# =================================ADMIN STORE MANAGERS MANAGEMENT======================================

def manageStoreManagers(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = store_manager_controller.get_all_store_manager()
        return render(request, 'storeManagers/manageStoreManagers.html',
                      {"store_managers": response['store_managers']})
    else:
        return redirect('login_area_head')

def viewStoreManager(request, mid):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = store_manager_controller.get_store_manager_by_id(mid)
        return render(request, 'storeManagers/viewStoreManager.html',
                      {"store_manager": response['store_manager']})
    else:
        return redirect('login_area_head')

# =================================ADMIN FRANCHISE OWNERS MANAGEMENT======================================

def manageFranchiseOwners(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = franchise_manager_controller.get_all_franchise_owner()
        return render(request, 'franchiseOwners/manageFranchiseOwners.html',
                      {"franchise_owners": response['franchise_owners']})
    else:
        return redirect('login_area_head')

def viewFranchiseOwners(request, foid):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = franchise_manager_controller.get_franchise_owner_by_id(foid)
        return render(request, 'franchiseOwners/viewFranchiseOwner.html',
                      {"franchise_owner": response['franchise_owner']})
    else:
        return redirect('login_area_head')

# =================================ADMIN MARKETING HEADS MANAGEMENT======================================

def manageMarketingHead(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = marketing_head_controller.get_all_marketing_head()
        return render(request, 'marketingHeads/manageMarketingHead.html',
                      {"marketing_heads_list": response['marketing_heads_list']})
    else:
        return redirect('login_area_head')

def viewMarketingHead(request, mhid):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = marketing_head_controller.get_marketing_head_by_id(mhid)
        print(response)
        return render(request, 'marketingHeads/viewMarketingHead.html',
                      {"marketing_head": response['marketing_head']})
    else:
        return redirect('login_area_head')

# =================================ADMIN OPTIMETRY MANAGEMENT======================================


def manageOptimetry(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'optimetry/manageOptimetry.html')
    else:
        return redirect('login_area_head')

def viewOptimetry(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'optimetry/viewOptimetry.html')

    else:
        return redirect('login_area_head')
# =================================ADMIN OPTIMETRY MANAGEMENT======================================


def manageSaleExecutives(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = sales_executives_controller.get_all_sales_executive()
        print(response)
        return render(request, 'salesExecutive/manageSaleExecutives.html',
                      {"sales_executive_list": response['sales_executive_list']})
    else:
        return redirect('login_area_head')


def viewSaleExecutives(request, seid):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = sales_executives_controller.get_sales_executive_by_id(seid)
        print(response)
        return render(request, 'salesExecutive/viewSaleExecutives.html',
                      {"sales_executive": response['sales_executive']})
    else:
        return redirect('login_area_head')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageAccountant(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = accountant_controller.get_all_accountant()
        return render(request, 'accountant/manageAccountant.html',
                      {"accountant_list": response['accountant_list']})
    else:
        return redirect('login_area_head')


def viewAccountant(request, aid):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = accountant_controller.get_accountant_by_id(aid)
        return render(request, 'accountant/viewAccountant.html',
                      {"accountant": response['accountant']})
    else:
        return redirect('login_area_head')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageLabTechnician(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = lab_technician_controller.get_all_lab_technician()
        return render(request, 'labTechnician/manageLabTechnician.html',
                      {"lab_technician_list": response['lab_technician_list']})
    else:
        return redirect('login_area_head')


def viewLabTechnician(request, ltid):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = lab_technician_controller.get_lab_technician_by_id(ltid)
        return render(request, 'labTechnician/viewLabTechnician.html',
                      {"lab_technician": response['lab_technician']})
    else:
        return redirect('login_area_head')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageOtherEmployees(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = other_employee_controller.get_all_other_emp()
        print(response)
        return render(request, 'otherEmployees/manageOtherEmployees.html',
                      {"other_employee_list": response['other_emp_list']})
    else:
        return redirect('login_area_head')


def viewOtherEmployees(request, empid):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = other_employee_controller.get_other_emp_by_id(empid)
        return render(request, 'otherEmployees/viewOtherEmployees.html',
                      {"other_employee": response['other_employee']})
    else:
        return redirect('login_area_head')

# =================================ADMIN ORDERS MANAGEMENT======================================

def viewAllOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewAllOrders.html')
    else:
        return redirect('login_area_head')

def viewPendingOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewPendingOrders.html')
    else:
        return redirect('login_area_head')


def viewReceivedOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewReceivedOrders.html')
    else:
        return redirect('login_area_head')


def viewProcessingOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewProcessingOrders.html')
    else:
        return redirect('login_area_head')

def viewReadyOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewReadyOrders.html')
    else:
        return redirect('login_area_head')

def viewDeliveredOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewDeliveredOrders.html')
    else:
        return redirect('login_area_head')

def viewCancelledOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewCancelledOrders.html')
    else:
        return redirect('login_area_head')

def viewRefundedOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewRefundedOrders.html')
    else:
        return redirect('login_area_head')

def viewOrderDetails(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewOrderDetails.html')
    else:
        return redirect('login_area_head')


# =================================ADMIN CUSTOMERS MANAGEMENT======================================

def viewAllCustomers(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = area_head_customers_controller.get_all_area_stores_customers(request.session.get('assigned_stores'))
        return render(request, 'customers/viewAllCustomers.html',{"customers_list": response['customers_list']})
    else:
        return redirect('login_area_head')


def viewCustomerDetails(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'customers/viewCustomerDetails.html')
    else:
        return redirect('login_area_head')


# =================================ADMIN LABS MANAGEMENT======================================

def manageLabs(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = lab_controller.get_all_labs()
        return render(request, 'labs/manageLabs.html', {"lab_list": response['lab_list']})
    else:
        return redirect('login_area_head')


def viewLab(request, labid):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = lab_controller.get_lab_by_id(labid)
        return render(request, 'labs/viewLab.html',
                      {"lab_data": response['lab_data']})
    else:
        return redirect('login_area_head')


def viewActiveJobs(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'labs/viewActiveJobs.html')
    else:
        return redirect('login_area_head')


def viewAllJobs(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'labs/viewAllJobs.html')
    else:
        return redirect('login_area_head')


def jobDetails(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'labs/jobDetails.html')
    else:
        return redirect('login_area_head')


def manageAuthenticityCard(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'labs/manageAuthenticityCard.html')
    else:
        return redirect('login_area_head')


# =================================ADMIN LABS MANAGEMENT======================================


def manageCentralInventoryProducts(request, status):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_central_inventory_products(status)
        return render(request, 'centralInventory/manageCentralInventoryProducts.html',
                      {"product_list": response['product_list'], "categories_List": response['categoriesList'],
                       "status": status})
    else:
        return redirect('login_area_head')


def manageCentralInventoryOutOfStock(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_out_of_stock_central_inventory_products(15)
        return render(request, 'centralInventory/manageCentralInventoryOutOfStock.html',
                      {"stocks_list": response['stocks_list'], "categories_list": response['categories_list']})
    else:
        return redirect('login_area_head')


def manageMoveStocks(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = own_store_controller.get_all_own_stores()
        return render(request, 'centralInventory/manageMoveStocks.html',
                      {"own_store_list": response['own_stores']})
    else:
        return redirect('login_area_head')


def manageMoveAStock(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'centralInventory/manageMoveAStock.html')
    else:
        return redirect('login_area_head')


# =================================ADMIN STORE MANAGEMENT======================================


def viewAllStockRequests(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'stockRequests/viewAllStockRequests.html')
    else:
        return redirect('login_area_head')


def viewPendingStockRequests(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'stockRequests/viewPendingStockRequests.html')
    else:
        return redirect('login_area_head')


def viewCompletedStockRequests(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'stockRequests/viewCompletedStockRequests.html')
    else:
        return redirect('login_area_head')


def viewRejectedStockRequests(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'stockRequests/viewrejectedStockRequests.html')
    else:
        return redirect('login_area_head')
