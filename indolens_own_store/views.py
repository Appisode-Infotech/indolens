import json

from django.shortcuts import redirect, render
from rest_framework.reverse import reverse

from indolens_admin.admin_controllers import central_inventory_controller, orders_controller
from indolens_own_store.own_store_controller import own_store_auth_controller, store_inventory_controller, \
    expense_controller, store_employee_controller, store_customers_controller, store_orders_controller, \
    own_store_dashboard_controller, own_store_lab_controller, own_store_eye_test_controller
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


def getAssignedStores(request):
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        assigned_store = own_store_auth_controller.get_assigned_store(request.session.get('id'))
        if assigned_store == 0:
            request.session.clear()
            return assigned_store
        else:
            return assigned_store
    else:
        return redirect('own_store_login')


# ================================= OWN STORE DASHBOARD ======================================
def dashboard(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        own_store_new_order, status_code = own_store_dashboard_controller.get_order_stats('New', 1, assigned_store)
        own_store_delivered_orders, status_code = own_store_dashboard_controller.get_order_stats('Completed', 1,
                                                                                                 assigned_store)
        own_store_sales, status_code = own_store_dashboard_controller.get_sales_stats(1, assigned_store)
        out_of_stock, status_code = store_inventory_controller.get_all_out_of_stock_products_for_store(15,
                                                                                                       assigned_store)
        orders_list, status_code = store_orders_controller.get_all_orders('All', 'All',
                                                                          assigned_store)
        return render(request, 'dashboardOwnStore.html',
                      {"own_store_new_order": own_store_new_order['count'],
                       "own_store_delivered_orders": own_store_delivered_orders['count'],
                       "own_store_sale": own_store_sales['sale'], "out_of_stock": len(out_of_stock['stocks_list']),
                       "orders_list": orders_list['dash_orders_list']})
    else:
        return redirect('own_store_login')


# ================================= OWN STORE EMPLOYEES ======================================
def manageStoreEmployees(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        assigned_store = assigned_store
        response, status_code = store_employee_controller.get_all_store_employee(assigned_store)
        return render(request, 'ownEmployee/manageEmployees.html',
                      {"store_employee_list": response['store_employee_list']})
    else:
        return redirect('own_store_login')


def viewEmployees(request, employeeId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_employee_controller.get_store_employee_by_id(employeeId)
        return render(request, 'ownEmployee/viewEmployee.html', {"store_employee": response['store_employee']})
    else:
        return redirect('own_store_login')

def viewFranchiseEmployees(request, employeeId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_employee_controller.get_franchise_employee_by_id(employeeId)
        return render(request, 'ownEmployee/viewEmployee.html', {"store_employee": response['store_employee']})
    else:
        return redirect('own_store_login')


# ================================= OWN STORE ORDER MANAGEMENT ======================================
def allStoreOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        orders_list, status_code = store_orders_controller.get_all_orders('All', 'All', assigned_store)
        return render(request, 'orders/allStoreOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('own_store_login')


def dispatchedStoreOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        orders_list, status_code = store_orders_controller.get_all_orders('Dispatched', 'All',
                                                                          assigned_store)
        return render(request, 'orders/pendingStoreOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('own_store_login')


def newStoreOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        orders_list, status_code = store_orders_controller.get_all_orders('New', 'All',
                                                                          assigned_store)
        return render(request, 'orders/receivedStoreOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('own_store_login')


def processingStoreOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        orders_list, status_code = store_orders_controller.get_all_orders('Processing', 'All',
                                                                          assigned_store)
        return render(request, 'orders/processingStoreOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('own_store_login')


def readyStoreOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        orders_list, status_code = store_orders_controller.get_all_orders('Ready', 'All',
                                                                          assigned_store)
        return render(request, 'orders/readyStoreOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('own_store_login')


def completedStoreOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        orders_list, status_code = store_orders_controller.get_all_orders('Completed', 'All',
                                                                          assigned_store)
        return render(request, 'orders/deliveredStoreOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('own_store_login')


def cancelledStoreOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        orders_list, status_code = store_orders_controller.get_all_orders('Cancelled', 'All',
                                                                          assigned_store)
        return render(request, 'orders/cancelledStoreOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('own_store_login')


def refundedStoreOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        orders_list, status_code = store_orders_controller.get_all_orders('Cancelled', 'Refunded',
                                                                          assigned_store)
        return render(request, 'orders/refundedStoreOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('own_store_login')


def orderDetails(request, orderId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        order_detail, status_code = orders_controller.get_order_details(orderId)
        return render(request, 'orders/orderDetails.html', {"order_detail": order_detail['orders_details']})
    else:
        return redirect('own_store_login')


def orderInvoice(request, orderId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        order_detail, status_code = orders_controller.get_order_details(orderId)
        store_data, store_status_code = orders_controller.get_store_details(
            order_detail['orders_details'][0]['created_by_store'],
            order_detail['orders_details'][0]['created_by_store_type'])
        return render(request, 'orders/store_order_invoice.html', {"order_detail": order_detail['orders_details'],
                                                                   "store_data": store_data['store_data']})
    else:
        return redirect('own_store_login')


def orderStatusChange(request, orderId, status):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        order_update, status_code = store_orders_controller.order_status_change(orderId, status)
        url = reverse('order_details_store', kwargs={'orderId': orderId})
        return redirect(url)
    else:
        return redirect('own_store_login')


def orderPaymentStatusChange(request, orderId, status):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        order_detail, status_code = store_orders_controller.order_payment_status_change(orderId, status)
        url = reverse('order_details_store', kwargs={'orderId': orderId})
        return redirect(url)
    else:
        return redirect('own_store_login')


# ================================= OWN STORE CUSTOMER MANAGEMENT ======================================

def viewStoreCustomers(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_customers_controller.get_all_store_customers(
            assigned_store)
        return render(request, 'customers/viewAllCustomersStore.html',
                      {"store_customers_list": response['store_customers_list']})
    else:
        return redirect('own_store_login')


def viewStoreCustomerDetails(request, customerId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_customers_controller.get_customers_by_id(customerId)
        sales_data, resp_code = orders_controller.get_all_customer_orders(customerId)
        total_bill = 0
        membership = "Gold"
        for price in sales_data['orders_list']:
            total_bill = total_bill + price.get('total_cost')

        if total_bill > 5000 and total_bill < 25000:
            membership = "Platinum"
        elif total_bill > 25000:
            membership = "Luxuary"
        return render(request, 'customers/viewCustomerDetailsStore.html',
                      {"customers": response['customers'], "sales_data": sales_data['orders_list'],
                       "membership": membership})
    else:
        return redirect('own_store_login')


# ================================= OWN STORE STOCK REQUESTS MANAGEMENT ======================================

def createStockRequestStore(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        if request.method == 'POST':
            print(request.POST)
            stock_obj = store_create_stock_request_model.store_create_stock_request_model_from_dict(request.POST)
            print(vars(stock_obj))
            response = store_inventory_controller.create_store_stock_request(stock_obj)
            print(response)
            route = request.POST.get('route')
            return redirect(route)
        else:
            response, status_code = store_inventory_controller.get_all_central_inventory_products(
                assigned_store)
            return render(request, 'stockRequests/createStockRequestStore.html',
                          {"product_list": response['product_list']})
    else:
        return redirect('own_store_login')


def viewAllStockRequestsStore(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.view_all_store_stock_request(
            assigned_store, '%')
        return render(request, 'stockRequests/viewAllStockRequestsStore.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('own_store_login')


def viewPendingStockRequestsStore(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.view_all_store_stock_request(
            assigned_store, '0')
        return render(request, 'stockRequests/viewPendingStockRequestsStore.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('own_store_login')


def viewCompletedStockRequestsStore(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.view_all_store_stock_request(
            assigned_store, '1')
        return render(request, 'stockRequests/viewCompletedStockRequestsStore.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('own_store_login')


def viewRejectedStockRequestsStore(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.view_all_store_stock_request(
            assigned_store, '2')
        return render(request, 'stockRequests/viewrejectedStockRequestsStore.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('own_store_login')


def stockRequestDeliveryStatusChange(request, requestId, status):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.request_delivery_status_change(requestId, status,
                                                                                          request.session.get('id'))
        print(response)
        return redirect('completed_store_stock_requests')
    else:
        return redirect('own_store_login')


# ================================= OWN STORE INVENTORY MANAGEMENT ======================================

def storeInventoryProducts(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.get_all_products_for_store(
            assigned_store)
        return render(request, 'inventory/storeInventoryProducts.html', {"stocks_list": response['stocks_list'],
                                                                         "categories_List": response[
                                                                             'product_category']})
    else:
        return redirect('own_store_login')


def inventoryOutOfStock(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = store_inventory_controller.get_all_out_of_stock_products_for_store(15, assigned_store)
        return render(request, 'inventory/inventoryOutOfStock.html', {"stocks_list": response['stocks_list'],
                                                                      "categories_List": response['product_category']})
    else:
        return redirect('own_store_login')


# ================================= SALES AND EXPENSES ======================================

def allExpenseStore(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        if request.method == 'POST':
            expense_obj = store_expense_model.store_expense_model_from_dict(request.POST)
            response, status_code = expense_controller.create_store_expense(expense_obj)
            return redirect('all_expenses_store')
        else:
            response, status_code = expense_controller.get_all_store_expense(assigned_store,
                                                                             request.session.get('store_type'))
            return render(request, 'expenses/allExpenseStore.html',
                          {"stor_expense_list": response['stor_expense_list']})
    else:
        return redirect('own_store_login')


def makeSaleOwnStore(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        if request.method == 'POST':
            cart_data = json.loads(request.POST['cartData'])
            customerData = json.loads(request.POST['customerData'])
            billingDetailsData = json.loads(request.POST['billingDetailsData'])
            make_order, status_code = expense_controller.make_sale(cart_data, customerData, billingDetailsData,
                                                                   request.session.get('id'),
                                                                   assigned_store)
            url = reverse('order_details_store', kwargs={'orderId': make_order['order_id']})
            return redirect(url)
        else:
            employee_list, emp_status_code = store_employee_controller.get_all_active_store_employee(
                assigned_store)
            lab_list, lab_status_code = own_store_lab_controller.get_all_active_labs()
            store_products, status_code = store_inventory_controller.get_all_products_for_store(
                assigned_store)
            customerResponse, cust_status_code = store_customers_controller.get_all_customers()
            lens_response, lens_status_code = central_inventory_controller.get_central_inventory_lens(
                assigned_store)
            return render(request, 'expenses/makeSaleOwnStore.html',
                          {"other_products_list": store_products['stocks_list'],
                           'customers_list': customerResponse['customers_list'],
                           "lens_list": lens_response['lens_list'],
                           "contact_lens_list": lens_response['contact_lens_list'],
                           "employee_list": employee_list['active_employee_list'],
                           "lab_list": lab_list['lab_list']})
    else:
        return redirect('own_store_login')


# ================================= Eye Test ======================================

def ownStoreEyeTest(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        if request.method == 'POST':
            response = own_store_eye_test_controller.add_eye_test(request.POST, request.session.get('id'),
                                                       assigned_store)
        customerResponse, cust_status_code = store_customers_controller.get_all_customers()
        return render(request, 'ownStoreEyeTest/ownStoreEyeTest.html',
                      {'customers_list': customerResponse['customers_list']})
    else:
        return redirect('own_store_login')


def getOwnStoreEyeTest(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = own_store_eye_test_controller.get_eye_test()
        print(response)
        return render(request, 'ownStoreEyeTest/viewAllStoreEyeTest.html',
                      {'eye_test_list': response['eye_test_list']})

    else:
        return redirect('own_store_login')

def getOwnStoreEyeTestById(request, testId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        response, status_code = own_store_eye_test_controller.get_eye_test_by_id(testId)
        print(response)
        return render(request, 'ownStoreEyeTest/viewAllStoreEyeTest.html',
                      {'eye_test_list': response['eye_test']})

    else:
        return redirect('own_store_login')

