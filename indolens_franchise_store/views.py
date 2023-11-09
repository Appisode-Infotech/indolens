from django.shortcuts import redirect, render

from indolens_franchise_store.franchise_store_controller import franchise_store_auth_controller, \
    franchise_store_customers_controller, franchise_expense_controller, franchise_inventory_controller
from indolens_franchise_store.franchise_store_model.franchise_store_req_model import franchise_store_employee_model, \
    franchise_expense_model, franchise_create_stock_request_model


# =================================ADMIN START======================================

def index(request):
    return redirect('franchise_store_login')


# ================================= FRANCHISE STORE AUTH ======================================

def login(request):
    if request.method == 'POST':
        store_obj = franchise_store_employee_model.store_employee_from_dict(request.POST)
        response, status_code = franchise_store_auth_controller.login(store_obj)
        if response['status']:
            for data in response['store']:
                request.session.update({
                    'is_franchise_store_logged_in': True,
                    'id': data['employee_id'],
                    'name': data['name'],
                    'email': data['email'],
                    'store_name': data['store_name'],
                    'store_type': '2',
                    'assigned_store_id': data['assigned_store_id'],
                    'profile_pic': data['profile_pic'],
                })
            return redirect('franchise_store_dashboard')
        else:
            return render(request, 'auth/franchise_sign_in.html', {"message": response['message']})
    else:
        return render(request, 'auth/franchise_sign_in.html')


def forgotPassword(request):
    if request.method == 'POST':
        response, status_code = franchise_store_auth_controller.forgot_password(request.POST['email'])
        return render(request, 'auth/franchise_store_forgot_password.html', {"message": response['message']})
    else:
        return render(request, 'auth/franchise_store_forgot_password.html')


def resetPassword(request, code):
    if request.method == 'POST':
        response, status_code = franchise_store_auth_controller.update_store_employee_password(request.POST['password'],
                                                                                               request.POST['email'])
        return render(request, 'auth/franchise_store_reset_password.html', {"code": code})
    else:
        response, status_code = franchise_store_auth_controller.check_link_validity(code)
        return render(request, 'auth/franchise_store_reset_password.html',
                      {"code": code, "message": response['message'], "email": response['email']})


def franchiseOwnerLogout(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        request.session.clear()
        return redirect('franchise_store_login')
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE DASHBOARD ======================================
def dashboard(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'franchise_dashboard.html')
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE ORDER MANAGEMENT ======================================
def allFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'orders/allFranchiseOrders.html')
    else:
        return redirect('franchise_store_login')


def pendingFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'orders/pendingFranchiseOrders.html')
    else:
        return redirect('franchise_store_login')


def receivedFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'orders/receivedFranchiseOrders.html')
    else:
        return redirect('franchise_store_login')


def processingFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'orders/processingFranchiseOrders.html')
    else:
        return redirect('franchise_store_login')


def readyFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'orders/readyFranchiseOrders.html')
    else:
        return redirect('franchise_store_login')


def deliveredFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'orders/deliveredFranchiseOrders.html')
    else:
        return redirect('franchise_store_login')


def cancelledFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'orders/cancelledFranchiseOrders.html')
    else:
        return redirect('franchise_store_login')


def refundedFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'orders/refundedFranchiseOrders.html')
    else:
        return redirect('franchise_store_login')


def orderDetailsFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'orders/orderDetailsFranchise.html')
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE CUSTIOMER MANAGEMENT ======================================

def viewAllCustomersFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_customers_controller.get_all_franchise_store_customers(
            request.session.get('assigned_store_id'))
        return render(request, 'customers/viewAllCustomersFranchise.html',
                      {"store_customers_list": response['store_customers_list']})
    else:
        return redirect('franchise_store_login')


def viewCustomerDetailsFranchise(request, customerId):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_customers_controller.get_customers_by_id(customerId)
        return render(request, 'customers/viewCustomerDetailsFranchise.html', {"customers": response['customers']})
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE STOCK REQUESTS MANAGEMENT ======================================

def createStockRequestFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        if request.method == 'POST':
            stock_obj = franchise_create_stock_request_model.franchise_create_stock_request_model_from_dict(
                request.POST)
            response = franchise_inventory_controller.create_store_stock_request(stock_obj)
            print(response)
            products, status_code = franchise_inventory_controller.get_all_central_inventory_products()
            return render(request, 'stockRequests/createStockRequestFranchise.html',
                          {"product_list": products['product_list']})
        else:
            response, status_code = franchise_inventory_controller.get_all_central_inventory_products()
            return render(request, 'stockRequests/createStockRequestFranchise.html',
                          {"product_list": response['product_list']})
    else:
        return redirect('franchise_store_login')


def viewAllStockRequestsFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.view_all_store_stock_request(
            request.session.get('assigned_store_id'), '%')
        return render(request, 'stockRequests/viewAllStockRequestsFranchise.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('franchise_store_login')


def viewPendingStockRequestsFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.view_all_store_stock_request(
            request.session.get('assigned_store_id'), '0')
        return render(request, 'stockRequests/viewPendingStockRequestsFranchise.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('franchise_store_login')


def viewCompletedStockRequestsFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.view_all_store_stock_request(
            request.session.get('assigned_store_id'), '1')
        return render(request, 'stockRequests/viewCompletedStockRequestsFranchise.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('franchise_store_login')


def viewRejectedStockRequestsFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.view_all_store_stock_request(
            request.session.get('assigned_store_id'), '2')
        return render(request, 'stockRequests/viewRejectedStockRequestsFranchise.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE INVENTORY MANAGEMENT ======================================

def franchiseInventoryProducts(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.get_all_products_for_franchise_store(
            request.session.get('assigned_store_id'))
        print(response)
        return render(request, 'inventory/franchiseInventoryProducts.html', {"stocks_list": response['stocks_list']})
    else:
        return redirect('franchise_store_login')


def inventoryOutOfStockFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.get_all_out_of_stock_products_for_franchise_store(15,
                                                                                                                 request.session.get(
                                                                                                                     'assigned_store_id'))
        return render(request, 'inventory/inventoryOutOfStockFranchise.html', {"stocks_list": response['stocks_list']})
    else:
        return redirect('franchise_store_login')


def moveStocksFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'inventory/moveStocksFranchise.html')
    else:
        return redirect('franchise_store_login')


# ================================= SALES AND EXPENSES ======================================

def allExpenseFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        if request.method == 'POST':
            expense_obj = franchise_expense_model.franchise_expense_model_from_dict(request.POST)
            response, status_code = franchise_expense_controller.create_franchise_store_expense(expense_obj)
            return redirect('all_expenses_franchise_store')
        else:
            response, status_code = franchise_expense_controller.get_all_franchise_store_expense(
                request.session.get('assigned_store_id'),
                request.session.get('store_type'))
            print(response)

            return render(request, 'expenses/allExpenseFranchise.html',
                          {"stor_expense_list": response['stor_expense_list']})
    else:
        return redirect('franchise_store_login')


def makeSaleFranchiseStore(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        return render(request, 'expenses/makeSaleFranchiseStore.html')
    else:
        return redirect('franchise_store_login')
