import json

from django.shortcuts import redirect, render
from rest_framework.reverse import reverse

from indolens_admin.admin_controllers import central_inventory_controller
from indolens_franchise_store.franchise_store_controller import franchise_store_auth_controller, \
    franchise_store_customers_controller, franchise_expense_controller, franchise_inventory_controller, \
    franchise_store_employee_controller, franchise_store_orders_controller, franchise_store_dashboard_controller, \
    franchise_store_lab_controller, franchise_store_eye_test_controller
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
        franchise_store_new_order, status_code = franchise_store_dashboard_controller.get_order_stats('New', 2,
                                                                                                      request.session.get(
                                                                                                          'assigned_store_id'))
        franchise_store_delivered_orders, status_code = franchise_store_dashboard_controller.get_order_stats(
            'Completed', 2, request.session.get('assigned_store_id'))
        franchise_store_sales, status_code = franchise_store_dashboard_controller.get_sales_stats(2,
                                                                                                  request.session.get(
                                                                                                      'assigned_store_id'))
        out_of_stock, status_code = franchise_inventory_controller.get_all_out_of_stock_products_for_franchise_store(15,
                                                                                                                     request.session.get(
                                                                                                                         'assigned_store_id'))
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('All', 'All', request.session.get(
            'assigned_store_id'))
        return render(request, 'franchise_dashboard.html',
                      {"franchise_store_new_order": franchise_store_new_order['count'],
                       "franchise_store_delivered_orders": franchise_store_delivered_orders['count'],
                       "out_of_stock": len(out_of_stock['stocks_list']), "orders_list": orders_list['orders_list'],
                       "franchise_store_sale": franchise_store_sales['sale']})
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE ORDER MANAGEMENT ======================================
def allFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('All', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_store_id'))
        return render(request, 'orders/allFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def dispatchedFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Dispatched', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_store_id'))
        return render(request, 'orders/pendingFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def newFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('New', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_store_id'))
        return render(request, 'orders/receivedFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def processingFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Processing', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_store_id'))
        return render(request, 'orders/processingFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def readyFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Ready', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_store_id'))
        return render(request, 'orders/readyFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def deliveredFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Completed', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_store_id'))
        return render(request, 'orders/deliveredFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def cancelledFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Cancelled', 'All',
                                                                                    request.session.get(
                                                                                        'assigned_store_id'))
        return render(request, 'orders/cancelledFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def refundedFranchiseOrders(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Cancelled', 'Refunded',
                                                                                    request.session.get(
                                                                                        'assigned_store_id'))
        return render(request, 'orders/refundedFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def orderDetailsFranchise(request, orderId):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        order_detail, status_code = franchise_store_orders_controller.get_order_details(orderId)
        print(order_detail)
        return render(request, 'orders/orderDetailsFranchise.html', {"order_detail": order_detail['orders_details']})
    else:
        return redirect('franchise_store_login')


def orderInvoiceFranchise(request, orderId):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        order_detail, status_code = franchise_store_orders_controller.get_order_details(orderId)
        store_data, store_status_code = franchise_store_orders_controller.get_store_details(
            order_detail['orders_details'][0]['created_by_store'],
            order_detail['orders_details'][0]['created_by_store_type'])
        return render(request, 'orders/franchise_order_invoice.html', {"order_detail": order_detail['orders_details'],
                                                                       "store_data": store_data['store_data']})
    else:
        return redirect('franchise_store_login')


def franchiseOrderStatusChange(request, orderId, status):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        order_detail, status_code = franchise_store_orders_controller.franchise_order_status_change(orderId, status)
        url = reverse('order_details_franchise_store', kwargs={'orderId': orderId})
        return redirect(url)
    else:
        return redirect('franchise_store_login')


def franchisePaymentStatusChange(request, orderId, status):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        order_detail, status_code = franchise_store_orders_controller.franchise_payment_status_change(orderId, status)
        url = reverse('order_details_franchise_store', kwargs={'orderId': orderId})
        return redirect(url)
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
        response, status_code = franchise_store_customers_controller.get_customers_by_id(customerId, )
        sales_data, sale_status_code = franchise_store_orders_controller.get_all_customer_orders(customerId)
        total_bill = 0
        membership = "Gold"
        for price in sales_data['orders_list']:
            total_bill = total_bill + price.get('total_cost')

        if total_bill > 5000 and total_bill < 25000:
            membership = "Platinum"
        elif total_bill > 25000:
            membership = "Luxuary"
        return render(request, 'customers/viewCustomerDetailsFranchise.html', {"customers": response['customers'],
                                                                               "sales_data": sales_data[
                                                                                   'orders_list'],
                                                                               "membership": membership})
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE EMPLOYEE MANAGEMENT ======================================

def viewAllEmployeFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_employee_controller.get_all_franchise_emp(
            request.session.get('assigned_store_id'))
        print(response)
        return render(request, 'employee/manageFranchiseEmployees.html',
                      {"franchise_employee_list": response['franchise_employee_list']})
    else:
        return redirect('franchise_store_login')


def viewEmployeeDetailsFranchise(request, employeeId):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_employee_controller.get_franchise_emp_by_id(
            request.session.get('assigned_store_id'), employeeId)
        print(response)
        return render(request, 'employee/viewEmployee.html',
                      {"franchise_employee": response['franchise_employee']})
    else:
        return redirect('franchise_store_login')


def viewEmployeeDetailsOwn(request, employeeId):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get('is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_employee_controller.get_own_store_employee_by_id(employeeId)
        print(response)
        return render(request, 'employee/viewEmployee.html',
                      {"franchise_employee": response['franchise_employee']})
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
            products, status_code = franchise_inventory_controller.get_all_central_inventory_products()
            return render(request, 'stockRequests/createStockRequestFranchise.html',
                          {"product_list": products['product_list']})
        else:
            response, status_code = franchise_inventory_controller.get_all_central_inventory_products()
            print(response)
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


def stockRequestDeliveryStatusChange(request, requestId, status):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        print(request)
        response, status_code = franchise_inventory_controller.request_delivery_status_change(requestId, status,
                                                                                              request.session.get('id'))
        print(response)
        return redirect('completed_franchise_store_stock_requests')
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE INVENTORY MANAGEMENT ======================================

def franchiseInventoryProducts(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.get_all_products_for_franchise_store(
            request.session.get('assigned_store_id'))
        return render(request, 'inventory/franchiseInventoryProducts.html', {"stocks_list": response['stocks_list'],
                                                                             "categories_List": response[
                                                                                 'product_category']})
    else:
        return redirect('franchise_store_login')


def inventoryOutOfStockFranchise(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.get_all_out_of_stock_products_for_franchise_store(15,
                                                                                                                 request.session.get(
                                                                                                                     'assigned_store_id'))
        return render(request, 'inventory/inventoryOutOfStockFranchise.html', {"stocks_list": response['stocks_list'],
                                                                             "categories_List": response[
                                                                                 'product_category']})
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
            return render(request, 'expenses/allExpenseFranchise.html',
                          {"stor_expense_list": response['stor_expense_list']})
    else:
        return redirect('franchise_store_login')


def makeSaleFranchiseStore(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        if request.method == 'POST':
            cart_data = json.loads(request.POST['cartData'])
            customerData = json.loads(request.POST['customerData'])
            billingDetailsData = json.loads(request.POST['billingDetailsData'])
            make_order, status_code = franchise_expense_controller.make_sale(cart_data, customerData,
                                                                             billingDetailsData,
                                                                             request.session.get('assigned_store_id'))
            print(make_order)
            url = reverse('order_details_franchise_store', kwargs={'orderId': make_order['order_id']})
            return redirect(url)
        else:
            employee_list, emp_status_code = franchise_store_employee_controller.get_all_active_franchise_emp(
                request.session.get('assigned_store_id'))
            lab_list, lab_status_code = franchise_store_lab_controller.get_all_active_labs()
            store_products, status_code = franchise_inventory_controller.get_all_products_for_store(
                request.session.get('assigned_store_id'))
            customerResponse, cust_status_code = franchise_store_customers_controller.get_all_customers()
            lens_response, lens_status_code = central_inventory_controller.get_central_inventory_lens(
                request.session.get('assigned_store_id'))

            return render(request, 'expenses/makeSaleFranchiseStore.html',
                          {"other_products_list": store_products['stocks_list'],
                           'customers_list': customerResponse['customers_list'],
                           "lens_list": lens_response['lens_list'],
                           "contact_lens_list": lens_response['contact_lens_list'],
                           "employee_list": employee_list['active_employee_list'],
                           "lab_list": lab_list['lab_list']})
    else:
        return redirect('franchise_store_login')


# ================================= Eye Test ======================================

def franchiseStoreEyeTest(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get('is_franchise_store_logged_in') is True:
        if request.method == 'POST':
            response = franchise_store_eye_test_controller.add_eye_test(request.POST, request.session.get('id'),
                                                       request.session.get('assigned_store_id'))
        customerResponse, cust_status_code = franchise_store_customers_controller.get_all_customers()
        print(customerResponse)
        return render(request, 'franchiseStoreEyeTest/franchiseStoreEyeTest.html',
                      {'customers_list': customerResponse['customers_list']})
    else:
        return redirect('franchise_store_login')


def getfranchiseStoreEyeTest(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get('is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_eye_test_controller.get_eye_test()
        print(response)
        return render(request, 'franchiseStoreEyeTest/viewAllStoreEyeTest.html',
                      {'eye_test_list': response['eye_test_list']})

    else:
        return redirect('franchise_store_login')

def getfranchiseStoreEyeTestById(request, testId):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get('is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_eye_test_controller.get_eye_test_by_id(testId)
        print(response)
        return render(request, 'franchiseStoreEyeTest/viewAllStoreEyeTest.html',
                      {'eye_test_list': response['eye_test']})

    else:
        return redirect('franchise_store_login')
