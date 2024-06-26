from django.shortcuts import render, redirect

from indolens_admin.admin_controllers import own_store_controller, \
    lab_technician_controller, lab_controller, \
    stores_inventory_controller, central_inventory_controller, customers_controller, area_head_controller, \
    orders_controller, store_expenses
from indolens_area_head.area_head_controller import area_head_auth_controller, stores_controller, \
    area_stores_inventory_controller, area_head_customers_controller, store_employee_controller, \
    area_head_store_orders_controller, area_head_dashboard_controller
from indolens_area_head.area_head_model.area_head_req_models import area_head_auth_model
from indolens_own_store.own_store_controller import store_inventory_controller


# =================================ADMIN START======================================
def index(request):
    return redirect('login_area_head')


# =================================ADMIN AUTH======================================

def login(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return redirect('dashboard_area_head')
    else:
        if request.method == 'POST':
            area_head_obj = area_head_auth_model.area_head_model_from_dict(request.POST)
            response, status_code = area_head_auth_controller.login(area_head_obj)
            if response['status']:
                if request.session.get('id') is not None:
                    request.session.clear()
                request.session.update({
                    'is_area_head_logged_in': True,
                    'id': response['area_head']['ah_area_head_id'],
                    'name': response['area_head']['ah_name'],
                    'email': response['area_head']['ah_email'],
                    'profile_pic': response['area_head']['ah_profile_pic'],
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
        return render(request, 'auth/reset_password.html',
                      {"code": code, "message": response['message'], "email": response['email']})


def getAreaHeadAssignedStores(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        assigned_store = area_head_auth_controller.get_area_head_assigned_store(request.session.get('id'))
        if assigned_store == 0:
            request.session.clear()
            return assigned_store
        else:
            return f"""({assigned_store})"""
    else:
        return redirect('login_area_head')


# =================================ADMIN DASH======================================

def dashboard(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        stats, stats_status_code = area_head_dashboard_controller.get_store_employee_stats(assigned_sores)
        orders_list, status_code = area_head_store_orders_controller.get_all_orders('All', 'All', assigned_sores)
        return render(request, 'dashboard.html', {"orders_list": orders_list['dash_orders_list'], "stats": stats})
    else:
        return redirect('login_area_head')


# =================================ADMIN STORE MANAGEMENT======================================

def manageOwnStores(request, status):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:

        response, status_code = stores_controller.get_area_head_own_stores(status, assigned_sores)
        return render(request, 'ownStore/manageOwnStores.html',
                      {"own_stores": response['own_stores'], "status": status})
    else:
        return redirect('login_area_head')


def viewOwnStore(request, ownStoreId):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = own_store_controller.get_own_store_by_id(ownStoreId)
        products_list, status_code = stores_inventory_controller.get_all_products_for_own_store(ownStoreId)
        store_stats, status_code = own_store_controller.get_own_storestore_stats(ownStoreId)
        revenue_generated, sale_status_code = orders_controller.get_store_sales(ownStoreId, 1)
        store_expense, store_exp_status_code = store_expenses.get_store_expense_amount(ownStoreId, 1)
        orders_list, status_code = area_head_store_orders_controller.get_all_store_orders(ownStoreId)
        return render(request, 'ownStore/ownStore.html',
                      {"store_data": response['own_stores'], "products_list": products_list['products_list'],
                       "total_employee_count": store_stats['total_employee_count'],
                       "total_customer_count": store_stats['total_customer_count'],
                       "orders_list": orders_list['orders_list'], "sales_data": orders_list['orders_list'],
                       "store_expense": store_expense['store_expense'], "revenue_generated": revenue_generated['sale'],
                       "net_income": int(revenue_generated['sale']) - store_expense['store_expense']})
    else:
        return redirect('login_area_head')


# =================================ADMIN STORE MANAGERS MANAGEMENT======================================

def manageEmployee(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = store_employee_controller.get_all_store_employee(assigned_sores)
        return render(request, 'storeEmployee/manageStoreEmployee.html',
                      {"store_employees": response['store_employees']})
    else:
        return redirect('login_area_head')


def viewEmployee(request, employeeId):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = store_employee_controller.get_store_employee_by_id(employeeId)
        return render(request, 'storeEmployee/viewStoreEmployee.html',
                      {"store_employee": response['store_employee']})
    else:
        return redirect('login_area_head')


def viewAreaHeadProfile(request, areaHeadId):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = area_head_controller.get_area_head_by_id(areaHeadId)
        return render(request, 'areaHead/viewAreaHeadProfile.html',
                      {"area_head": response['area_head']})
    else:
        return redirect('login_area_head')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageLabTechnician(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = lab_technician_controller.get_all_lab_technician()
        return render(request, 'labTechnician/manageLabTechnician.html',
                      {"lab_technician_list": response['lab_technician_list']})
    else:
        return redirect('login_area_head')


def viewLabTechnician(request, ltid):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = lab_technician_controller.get_lab_technician_by_id(ltid)
        return render(request, 'labTechnician/viewLabTechnician.html',
                      {"lab_technician": response['lab_technician']})
    else:
        return redirect('login_area_head')


# =================================ADMIN ORDERS MANAGEMENT======================================

def viewAllOrders(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        orders_list, status_code = area_head_store_orders_controller.get_all_orders('All', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_stores'))
        return render(request, 'orders/viewAllOrders.html', {"orders_list": orders_list['orders_list']})
    else:
        return redirect('login_area_head')


def viewdispatchedOrders(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        orders_list, status_code = area_head_store_orders_controller.get_all_orders('Dispatched', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_stores'))
        return render(request, 'orders/viewDispatchedOrders.html', {"orders_list": orders_list['orders_list']})
    else:
        return redirect('login_area_head')


def viewReceivedOrders(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewNewOrders.html')
    else:
        return redirect('login_area_head')


def viewProcessingOrders(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewProcessingOrders.html')
    else:
        return redirect('login_area_head')


def viewReadyOrders(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewReadyOrders.html')
    else:
        return redirect('login_area_head')


def viewDeliveredOrders(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewCompletedOrders.html')
    else:
        return redirect('login_area_head')


def viewCancelledOrders(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewCancelledOrders.html')
    else:
        return redirect('login_area_head')


def viewRefundedOrders(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewRefundedOrders.html')
    else:
        return redirect('login_area_head')


def viewOrderDetails(request, orderId):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        orders_list, status_code = area_head_store_orders_controller.get_order_details(orderId)
        return render(request, 'orders/viewOrderDetails.html', {"order_detail": orders_list['orders_details']})
    else:
        return redirect('login_area_head')


# =================================ADMIN CUSTOMERS MANAGEMENT======================================

def viewAllCustomers(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = area_head_customers_controller.get_all_area_stores_customers(assigned_sores)
        return render(request, 'customers/viewAllCustomers.html', {"customers_list": response['customers_list']})
    else:
        return redirect('login_area_head')


def viewCustomerDetails(request, customerId):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = area_head_customers_controller.get_customers_by_id(customerId)
        spending, status_code = customers_controller.get_customer_spend(customerId)
        orders_list, orders_status_code = orders_controller.get_all_customer_orders(customerId)

        membership = "Gold"
        if spending['total_spending'] > 5000 and spending['total_spending'] < 25000:
            membership = "Platinum"
        elif spending['total_spending'] > 25000:
            membership = "Luxury"
        return render(request, 'customers/viewCustomerDetails.html',
                      {"customer": response['customer'], "orders_list": orders_list['orders_list'],
                       "membership": membership})
    else:
        return redirect('login_area_head')


# =================================ADMIN LABS MANAGEMENT======================================

def manageLabs(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = lab_controller.get_all_labs()
        return render(request, 'labs/manageLabs.html', {"lab_list": response['lab_list']})
    else:
        return redirect('login_area_head')


def viewLab(request, labid):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = lab_controller.get_lab_by_id(labid)
        return render(request, 'labs/viewLab.html',
                      {"lab_data": response['lab_data']})
    else:
        return redirect('login_area_head')


def viewActiveJobs(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'labs/viewActiveJobs.html')
    else:
        return redirect('login_area_head')


def viewAllJobs(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'labs/viewAllJobs.html')
    else:
        return redirect('login_area_head')


def jobDetails(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'labs/jobDetails.html')
    else:
        return redirect('login_area_head')


def manageAuthenticityCard(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'labs/manageAuthenticityCard.html')
    else:
        return redirect('login_area_head')


# =================================ADMIN LABS MANAGEMENT======================================


def manageCentralInventoryProducts(request, status):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_central_inventory_products(status)
        return render(request, 'centralInventory/manageCentralInventoryProducts.html',
                      {"product_list": response['product_list'], "categories_List": response['categoriesList'],
                       "status": status})
    else:
        return redirect('login_area_head')


def manageCentralInventoryOutOfStock(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_out_of_stock_central_inventory_products(15)
        return render(request, 'centralInventory/manageCentralInventoryOutOfStock.html',
                      {"stocks_list": response['stocks_list'], "categories_list": response['categories_list']})
    else:
        return redirect('login_area_head')


def manageMoveStocks(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = own_store_controller.get_all_own_stores()
        return render(request, 'centralInventory/manageMoveStocks.html',
                      {"own_store_list": response['own_stores']})
    else:
        return redirect('login_area_head')


def manageMoveAStock(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'centralInventory/manageMoveAStock.html')
    else:
        return redirect('login_area_head')


# =================================ADMIN STORE MANAGEMENT======================================


def viewAllStockRequests(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'stockRequests/viewAllStockRequests.html')
    else:
        return redirect('login_area_head')


def viewPendingStockRequests(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'stockRequests/viewPendingStockRequests.html')
    else:
        return redirect('login_area_head')


def viewCompletedStockRequests(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'stockRequests/viewCompletedStockRequests.html')
    else:
        return redirect('login_area_head')


def viewRejectedStockRequests(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'stockRequests/viewrejectedStockRequests.html')
    else:
        return redirect('login_area_head')


def manageTask(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return redirect('dashboard_area_head')
    else:
        return redirect('login_area_head')


def manageCampaigns(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return redirect('dashboard_area_head')
    else:
        return redirect('login_area_head')
