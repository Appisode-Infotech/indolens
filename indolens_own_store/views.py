from django.shortcuts import redirect, render

from indolens_own_store.own_store_controller import own_store_auth_controller, store_inventory_controller, \
    expense_controller
from indolens_own_store.own_store_model.request_model import own_store_employee_model, expense_model


# =================================ADMIN START======================================

def index(request):
    return redirect('own_store_login')


# ================================= OWN STORE AUTH ======================================

def login(request):
    if request.method == 'POST':
        store_obj = own_store_employee_model.store_employee_from_dict(request.POST)
        response, status_code = own_store_auth_controller.login(store_obj)
        if response['status']:
            for data in response['store']:
                request.session.update({
                    'is_store_logged_in': True,
                    'id': data['employee_id'],
                    'name': data['name'],
                    'email': data['email'],
                    'store_name': data['store_name'],
                    'assigned_store_id': data['assigned_store_id'],
                    'profile_pic': data['profile_pic'],
                })
            return redirect('own_store_dashboard')
        else:
            return render(request, 'auth/own_store_sign_in.html', {"message": response['message']})
    return render(request, 'auth/own_store_sign_in.html')


def forgotPassword(request):
    return render(request, 'auth/own_store_forgot_password.html')


def resetPassword(request):
    return render(request, 'auth/own_store_reset_password.html')


def storeManagerLogout(request):
    return redirect('own_store_login')


# ================================= OWN STORE DASHBOARD ======================================
def dashboard(request):
    return render(request, 'dashboardOwnStore.html')


# ================================= OWN STORE EMPLOYEES ======================================
def manageStoreEmployees(request):
    return render(request, 'employee/manageEmployees.html')


def viewEmployees(request):
    return render(request, 'employee/viewEmployee.html')


# ================================= OWN STORE ORDER MANAGEMENT ======================================
def allStoreOrders(request):
    return render(request, 'orders/allStoreOrders.html')


def pendingStoreOrders(request):
    return render(request, 'orders/pendingStoreOrders.html')


def receivedStoreOrders(request):
    return render(request, 'orders/receivedStoreOrders.html')


def processingStoreOrders(request):
    return render(request, 'orders/processingStoreOrders.html')


def readyStoreOrders(request):
    return render(request, 'orders/readyStoreOrders.html')


def deliveredStoreOrders(request):
    return render(request, 'orders/deliveredStoreOrders.html')


def cancelledStoreOrders(request):
    return render(request, 'orders/cancelledStoreOrders.html')


def refundedStoreOrders(request):
    return render(request, 'orders/refundedStoreOrders.html')


def orderDetails(request):
    return render(request, 'orders/orderDetails.html')


# ================================= OWN STORE CUSTIOMER MANAGEMENT ======================================

def viewStoreCustomers(request):
    return render(request, 'customers/viewAllCustomersStore.html')


def viewStoreCustomerDetails(request):
    return render(request, 'customers/viewCustomerDetailsStore.html')


# ================================= OWN STORE STOCK REQUESTS MANAGEMENT ======================================

def createStockRequestStore(request):
    if request.method == 'POST':
        response = store_inventory_controller.create_store_stock_request(request.POST,
                                                                         request.session.get('assigned_store_id'),
                                                                         request.session.get('id'))
        response, status_code = store_inventory_controller.get_all_central_inventory_products()
        return render(request, 'stockRequests/createStockRequestStore.html', {"product_list": response['product_list']})
    else:
        response, status_code = store_inventory_controller.get_all_central_inventory_products()
        return render(request, 'stockRequests/createStockRequestStore.html', {"product_list": response['product_list']})


def viewAllStockRequestsStore(request):
    response, status_code = store_inventory_controller.view_all_store_stock_request(
        request.session.get('assigned_store_id'), '%')
    return render(request, 'stockRequests/viewAllStockRequestsStore.html',
                  {"stocks_request_list": response['stocks_request_list']})


def viewPendingStockRequestsStore(request):
    response, status_code = store_inventory_controller.view_all_store_stock_request(
        request.session.get('assigned_store_id'), '0')
    return render(request, 'stockRequests/viewPendingStockRequestsStore.html',
                  {"stocks_request_list": response['stocks_request_list']})


def viewCompletedStockRequestsStore(request):
    response, status_code = store_inventory_controller.view_all_store_stock_request(
        request.session.get('assigned_store_id'), '1')
    return render(request, 'stockRequests/viewCompletedStockRequestsStore.html',
                  {"stocks_request_list": response['stocks_request_list']})


def viewRejectedStockRequestsStore(request):
    response, status_code = store_inventory_controller.view_all_store_stock_request(
        request.session.get('assigned_store_id'), '2')
    return render(request, 'stockRequests/viewRejectedStockRequestsStore.html',
                  {"stocks_request_list": response['stocks_request_list']})


# ================================= OWN STORE INVENTORY MANAGEMENT ======================================

def storeInventoryProducts(request):
    response, status_code = store_inventory_controller.get_all_products_for_store(
        request.session.get('assigned_store_id'))
    return render(request, 'inventory/storeInventoryProducts.html', {"stocks_list": response['stocks_list']})


def inventoryOutOfStock(request):
    response, status_code = store_inventory_controller.get_all_out_of_stock_products_for_store(15, request.session.get(
        'assigned_store_id'))
    return render(request, 'inventory/inventoryOutOfStock.html', {"stocks_list": response['stocks_list']})


def moveStocksStore(request):
    return render(request, 'inventory/moveStocksStore.html')


# ================================= SALES AND EXPENSES ======================================

def allExpenseStore(request):
    if request.method == 'POST':
        print(request.POST)
        expense_obj = expense_model.expense_model_from_dict(request.POST)
        expense_controller.create_store_expense(expense_obj)
        return render(request, 'expenses/allExpenseStore.html')
    else:
        expense_controller.get_all_store_expense()
        return render(request, 'expenses/allExpenseStore.html')


def makeSaleOwnStore(request):
    return render(request, 'expenses/makeSaleOwnStore.html')
