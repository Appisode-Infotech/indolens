from django.shortcuts import render, redirect

from indolens_admin.admin_controllers import own_store_controller, \
    lab_technician_controller, lab_controller, \
    stores_inventory_controller, central_inventory_controller, customers_controller, area_head_controller, \
    orders_controller
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
    if request.method == 'POST':
        area_head_obj = area_head_auth_model.area_head_model_from_dict(request.POST)
        response, status_code = area_head_auth_controller.login(area_head_obj)
        if response['status']:
            if request.session.get('id') is not None:
                request.session.clear()
            for data in response['area_head']:
                if len(data['assigned_stores']) == 1:
                    assigned_stores = f"({data['assigned_stores'][0]})"
                else:
                    assigned_stores = tuple(data['assigned_stores'])
                request.session.update({
                    'is_area_head_logged_in': True,
                    'id': data['area_head_id'],
                    'assigned_stores': assigned_stores,
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
        return redirect('is_area_head_logged_in')


# =================================ADMIN DASH======================================

def dashboard(request):
    assigned_sores = getAreaHeadAssignedStores(request)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        new_order, status_code = area_head_dashboard_controller.get_order_stats('New', 1)
        delivered_orders, status_code = area_head_dashboard_controller.get_order_stats('Completed', 1)
        store_sales, status_code = area_head_dashboard_controller.get_sales_stats(1)
        orders_list, status_code = area_head_store_orders_controller.get_all_orders('All', 'All', assigned_sores)
        return render(request, 'dashboard.html', {"orders_list": orders_list['dash_orders_list']})
    else:
        return redirect('login_area_head')


# =================================ADMIN STORE MANAGEMENT======================================

def manageOwnStores(request, status):
    assigned_sores = getAreaHeadAssignedStores(request)
    print(assigned_sores)
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:

        response, status_code = stores_controller.get_area_head_own_stores(status, assigned_sores)
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
        orders_list, status_code = area_head_store_orders_controller.get_all_store_orders(ownStoreId)
        return render(request, 'ownStore/ownStore.html',
                      {"store_data": response['own_stores'], "products_list": products_list['products_list'],
                       "total_employee_count": store_stats['total_employee_count'],
                       "total_customer_count": store_stats['total_customer_count'],
                       "orders_list": orders_list['orders_list'], "sales_data": orders_list['orders_list'],
                       "revenue_generated": sum(item['total_cost'] for item in orders_list['orders_list']), })
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
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        print(employeeId)
        response, status_code = store_employee_controller.get_store_employee_by_id(employeeId)
        print(response)
        return render(request, 'storeEmployee/viewStoreEmployee.html',
                      {"store_employee": response['store_employee']})
    else:
        return redirect('login_area_head')


def viewAreaHeadProfile(request, areaHeadId):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = area_head_controller.get_area_head_by_id(areaHeadId)
        return render(request, 'areaHead/viewAreaHeadProfile.html',
                      {"area_head": response['area_head']})
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


# =================================ADMIN ORDERS MANAGEMENT======================================

def viewAllOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        orders_list, status_code = area_head_store_orders_controller.get_all_orders('All', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_stores'))
        return render(request, 'orders/viewAllOrders.html', {"orders_list": orders_list['orders_list']})
    else:
        return redirect('login_area_head')


def viewdispatchedOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        orders_list, status_code = area_head_store_orders_controller.get_all_orders('Dispatched', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_stores'))
        return render(request, 'orders/viewDispatchedOrders.html', {"orders_list": orders_list['orders_list']})
    else:
        return redirect('login_area_head')


def viewReceivedOrders(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return render(request, 'orders/viewNewOrders.html')
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
        return render(request, 'orders/viewCompletedOrders.html')
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


def viewOrderDetails(request, orderId):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        orders_list, status_code = area_head_store_orders_controller.get_order_details(orderId)
        return render(request, 'orders/viewOrderDetails.html', {"order_detail": orders_list['orders_details']})
    else:
        return redirect('login_area_head')


# =================================ADMIN CUSTOMERS MANAGEMENT======================================

def viewAllCustomers(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = area_head_customers_controller.get_all_area_stores_customers(
            request.session.get('assigned_stores'))
        return render(request, 'customers/viewAllCustomers.html', {"customers_list": response['customers_list']})
    else:
        return redirect('login_area_head')


def viewCustomerDetails(request, customerId):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        response, status_code = area_head_customers_controller.get_customers_by_id(customerId)
        orders_list, status_code = area_head_store_orders_controller.get_all_customer_orders(customerId)
        total_bill = 0
        membership = "Gold"
        for price in orders_list['orders_list']:
            total_bill = total_bill + price.get('total_cost')

        if total_bill > 5000 and total_bill < 25000:
            membership = "Platinum"
        elif total_bill > 25000:
            membership = "Luxuary"
        return render(request, 'customers/viewCustomerDetails.html',
                      {"customer": response['customer'], "orders_list": orders_list['orders_list'],
                       "membership": membership})
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


def manageTask(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return redirect('dashboard_area_head')
    else:
        return redirect('login_area_head')


def manageCampaigns(request):
    if request.session.get('is_area_head_logged_in') is not None and request.session.get(
            'is_area_head_logged_in') is True:
        return redirect('dashboard_area_head')
    else:
        return redirect('login_area_head')
