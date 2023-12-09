from django.shortcuts import redirect, render

from indolens_admin.admin_controllers import customers_controller, central_inventory_controller
from indolens_own_store.own_store_controller import own_store_auth_controller, store_inventory_controller, \
    expense_controller, store_employee_controller, store_customers_controller
from indolens_own_store.own_store_model.request_model import own_store_employee_model, \
    store_expense_model, store_create_stock_request_model


# =================================ADMIN START======================================

def index(request):
    return redirect('own_store_login')


# ================================= OWN STORE AUTH ======================================

def login(request):
    if request.method == 'POST':
        store_obj = own_store_employee_model.store_employee_from_dict(request.POST)
        response, status_code = own_store_auth_controller.login(store_obj)
        if response['status']:
            request.session.clear()
            for data in response['store']:
                request.session.update({
                    'is_store_logged_in': True,
                    'id': data['employee_id'],
                    'name': data['name'],
                    'email': data['email'],
                    'store_name': data['store_name'],
                    'store_type': '1',
                    'assigned_store_id': data['assigned_store_id'],
                    'profile_pic': data['profile_pic'],
                })
            return redirect('own_store_dashboard')
        else:
            return render(request, 'auth/own_store_sign_in.html', {"message": response['message']})
    else:
        return render(request, 'auth/own_store_sign_in.html')


def forgotPassword(request):
    if request.method == 'POST':
        response, status_code = own_store_auth_controller.forgot_password(request.POST['email'])
        return render(request, 'auth/own_store_forgot_password.html', {"message": response['message']})
    else:
        return render(request, 'auth/own_store_forgot_password.html')


def resetPassword(request, code):
    if request.method == 'POST':
        response, status_code = own_store_auth_controller.update_store_employee_password(request.POST['password'],
                                                                                         request.POST['email'])
        return render(request, 'auth/own_store_reset_password.html', {"code": code})
    else:
        response, status_code = own_store_auth_controller.check_link_validity(code)
        return render(request, 'auth/own_store_reset_password.html',
                      {"code": code, "message": response['message'], "email": response['email']})


def storeEmployeeLogout(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        request.session.clear()
        return redirect('own_store_login')
    else:
        return redirect('own_store_login')


# ================================= OWN STORE DASHBOARD ======================================
def dashboard(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        return render(request, 'dashboardOwnStore.html')
    else:
        return redirect('own_store_login')


# ================================= OWN STORE EMPLOYEES ======================================
def manageStoreEmployees(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_employee_controller.get_all_store_employee(
            request.session.get('assigned_store_id'))
        return render(request, 'ownEmployee/manageEmployees.html',
                      {"store_employee_list": response['store_employee_list']})
    else:
        return redirect('own_store_login')


def viewEmployees(request, employeeId):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_employee_controller.get_store_employee_by_id(employeeId)
        print("ownstore view ownEmployee")
        print(response['store_employee'])
        return render(request, 'ownEmployee/viewEmployee.html', {"store_employee": response['store_employee']})
    else:
        return redirect('own_store_login')


# ================================= OWN STORE ORDER MANAGEMENT ======================================
def allStoreOrders(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        return render(request, 'orders/allStoreOrders.html')
    else:
        return redirect('own_store_login')


def pendingStoreOrders(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        return render(request, 'orders/pendingStoreOrders.html')
    else:
        return redirect('own_store_login')


def receivedStoreOrders(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        return render(request, 'orders/receivedStoreOrders.html')
    else:
        return redirect('own_store_login')


def processingStoreOrders(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        return render(request, 'orders/processingStoreOrders.html')
    else:
        return redirect('own_store_login')


def readyStoreOrders(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        return render(request, 'orders/readyStoreOrders.html')
    else:
        return redirect('own_store_login')


def deliveredStoreOrders(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        return render(request, 'orders/deliveredStoreOrders.html')
    else:
        return redirect('own_store_login')


def cancelledStoreOrders(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        return render(request, 'orders/cancelledStoreOrders.html')
    else:
        return redirect('own_store_login')


def refundedStoreOrders(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        return render(request, 'orders/refundedStoreOrders.html')
    else:
        return redirect('own_store_login')


def orderDetails(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        return render(request, 'orders/orderDetails.html')
    else:
        return redirect('own_store_login')


# ================================= OWN STORE CUSTOMER MANAGEMENT ======================================

def viewStoreCustomers(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_customers_controller.get_all_store_customers(
            request.session.get('assigned_store_id'))
        return render(request, 'customers/viewAllCustomersStore.html',
                      {"store_customers_list": response['store_customers_list']})
    else:
        return redirect('own_store_login')


def viewStoreCustomerDetails(request, customerId):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_customers_controller.get_customers_by_id(customerId)
        return render(request, 'customers/viewCustomerDetailsStore.html',
                      {"customers": response['customers']})
    else:
        return redirect('own_store_login')


# ================================= OWN STORE STOCK REQUESTS MANAGEMENT ======================================

def createStockRequestStore(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        if request.method == 'POST':
            stock_obj = store_create_stock_request_model.store_create_stock_request_model_from_dict(request.POST)
            response = store_inventory_controller.create_store_stock_request(stock_obj)
            products, status_code = store_inventory_controller.get_all_central_inventory_products()
            return render(request, 'stockRequests/createStockRequestStore.html',
                          {"product_list": products['product_list']})
        else:
            response, status_code = store_inventory_controller.get_all_central_inventory_products()
            print(response)
            return render(request, 'stockRequests/createStockRequestStore.html',
                          {"product_list": response['product_list']})
    else:
        return redirect('own_store_login')


def viewAllStockRequestsStore(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.view_all_store_stock_request(
            request.session.get('assigned_store_id'), '%')
        return render(request, 'stockRequests/viewAllStockRequestsStore.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('own_store_login')


def viewPendingStockRequestsStore(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.view_all_store_stock_request(
            request.session.get('assigned_store_id'), '0')
        return render(request, 'stockRequests/viewPendingStockRequestsStore.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('own_store_login')


def viewCompletedStockRequestsStore(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.view_all_store_stock_request(
            request.session.get('assigned_store_id'), '1')
        return render(request, 'stockRequests/viewCompletedStockRequestsStore.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('own_store_login')


def viewRejectedStockRequestsStore(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.view_all_store_stock_request(
            request.session.get('assigned_store_id'), '2')
        return render(request, 'stockRequests/viewRejectedStockRequestsStore.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('own_store_login')


# ================================= OWN STORE INVENTORY MANAGEMENT ======================================

def storeInventoryProducts(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.get_all_products_for_store(
            request.session.get('assigned_store_id'))
        return render(request, 'inventory/storeInventoryProducts.html', {"stocks_list": response['stocks_list']})
    else:
        return redirect('own_store_login')


def inventoryOutOfStock(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.get_all_out_of_stock_products_for_store(15,
                                                                                                   request.session.get(
                                                                                                       'assigned_store_id'))
        return render(request, 'inventory/inventoryOutOfStock.html', {"stocks_list": response['stocks_list']})
    else:
        return redirect('own_store_login')


# ================================= SALES AND EXPENSES ======================================

def allExpenseStore(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        if request.method == 'POST':
            expense_obj = store_expense_model.store_expense_model_from_dict(request.POST)
            response, status_code = expense_controller.create_store_expense(expense_obj)
            return redirect('all_expenses_store')
        else:
            response, status_code = expense_controller.get_all_store_expense(request.session.get('assigned_store_id'),
                                                                             request.session.get('store_type'))
            print(response['stor_expense_list'])
            return render(request, 'expenses/allExpenseStore.html',
                          {"stor_expense_list": response['stor_expense_list']})
    else:
        return redirect('own_store_login')


def makeSaleOwnStore(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.get_all_products_for_store(
            request.session.get('assigned_store_id'))
        customerResponse, status_code_cust = customers_controller.get_all_stores_customers()
        lense_response, status_code = central_inventory_controller.get_central_inventory_lens()
        print("===================== stock_lens ============================")
        print(lense_response['stock_lens'])
        print("=================== rx_lens ==============================")
        print(lense_response['rx_lens'])
        return render(request, 'expenses/makeSaleOwnStore.html',
                      {"stocks_list": response['stocks_list'], 'customers_list': customerResponse['customers_list'],
                       "stock_bifocal_lens": lense_response['stock_bifocal_lens'],
                       "stock_single_vision_lens": lense_response['stock_single_vision_lens'],
                       "stock_progressive_lens": lense_response['stock_progressive_lens'],
                       "rx_progressive_lens": lense_response['rx_progressive_lens'],
                       "rx_bifocal_lens": lense_response['rx_bifocal_lens'],
                       "rx_single_vision_lens": lense_response['rx_single_vision_lens']
                       })
    else:
        return redirect('own_store_login')
