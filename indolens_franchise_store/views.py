import json

from django.shortcuts import redirect, render
from rest_framework.reverse import reverse

from indolens_admin.admin_controllers import central_inventory_controller, eye_test_controller, orders_controller, \
    lab_controller, customers_controller
from indolens_admin.admin_controllers.central_inventory_controller import get_central_inventory_product_single
from indolens_franchise_store.franchise_store_controller import franchise_store_auth_controller, \
    franchise_store_customers_controller, franchise_expense_controller, franchise_inventory_controller, \
    franchise_store_employee_controller, franchise_store_orders_controller, franchise_store_dashboard_controller, \
    franchise_store_lab_controller, franchise_store_eye_test_controller
from indolens_franchise_store.franchise_store_model.franchise_store_req_model import franchise_store_employee_model, \
    franchise_expense_model, franchise_create_stock_request_model
from indolens_own_store.own_store_model.request_model import order_payment_status_change_model


# =================================ADMIN START======================================

def index(request):
    return redirect('franchise_store_login')


# ================================= FRANCHISE STORE AUTH ======================================

def login(request):
    if request.method == 'POST':
        store_obj = franchise_store_employee_model.store_employee_from_dict(request.POST)
        response, status_code = franchise_store_auth_controller.login(store_obj)
        if response['status']:
            if request.session.get('id') is not None:
                request.session.clear()
            request.session.update({
                'is_franchise_store_logged_in': True,
                'id': response['fse']['fse_employee_id'],
                'name': response['fse']['fse_name'],
                'email': response['fse']['fse_email'],
                'store_name': response['fse']['store_name'],
                'store_type': '2',
                'assigned_store_id': response['fse']['fse_assigned_store_id'],
                'profile_pic': response['fse']['fse_profile_pic'],
                'role': response['fse']['fse_role'],
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
        return render(request, 'auth/franchise_store_forgot_password.html', {"status": False})


def resetPassword(request, code):
    if request.method == 'POST':
        response, status_code = franchise_store_auth_controller.update_store_employee_password(request.POST['password'],
                                                                                               request.POST['email'])
        return render(request, 'auth/franchise_store_reset_password.html',
                      {"code": code, "message": response['message']})
    else:
        response, status_code = franchise_store_auth_controller.check_link_validity(code)
        return render(request, 'auth/franchise_store_reset_password.html',
                      {"code": code, "message": response['message'], "email": response['email']})


def franchiseStoreLogout(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        request.session.clear()
        return redirect('franchise_store_login')
    else:
        return redirect('franchise_store_login')


def getAssignedStores(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        assigned_store = franchise_store_auth_controller.get_assigned_store(request.session.get('id'))
        if assigned_store == 0:
            request.session.clear()
            return assigned_store
        else:
            return assigned_store
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE DASHBOARD ======================================
def dashboard(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:

        franchise_store_new_order, status_code = franchise_store_dashboard_controller.get_order_stats('New', 2,
                                                                                                      assigned_store)
        franchise_store_delivered_orders, status_code = franchise_store_dashboard_controller.get_order_stats(
            'Completed', 2, assigned_store)
        franchise_store_sales, status_code = franchise_store_dashboard_controller.get_sales_stats(2, assigned_store)
        out_of_stock, status_code = franchise_inventory_controller.get_all_out_of_stock_products_for_franchise_store(15,
                                                                                                                     assigned_store)
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('All', 'All', assigned_store)

        return render(request, 'franchise_dashboard.html',
                      {"franchise_store_new_order": franchise_store_new_order['count'],
                       "franchise_store_delivered_orders": franchise_store_delivered_orders['count'],
                       "out_of_stock": len(out_of_stock['stocks_list']), "orders_list": orders_list['dash_orders_list'],
                       "franchise_store_sale": franchise_store_sales['sale']})
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE ORDER MANAGEMENT ======================================
def allFranchiseOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('All', 'All', assigned_store)
        return render(request, 'orders/allFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def dispatchedFranchiseOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Dispatched', 'All', assigned_store)
        return render(request, 'orders/pendingFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def newFranchiseOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('New', 'All', assigned_store)
        return render(request, 'orders/receivedFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def processingFranchiseOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Processing', 'All', assigned_store)
        return render(request, 'orders/processingFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def readyFranchiseOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Ready', 'All', assigned_store)
        return render(request, 'orders/readyFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def storeDeliverdFranchiseOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Delivered Store', 'All',
                                                                                    assigned_store)
        return render(request, 'orders/readyFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def deliveredFranchiseOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_completed_orders('Delivered Customer', 'All',
                                                                                          assigned_store)
        return render(request, 'orders/deliveredFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def cancelledFranchiseOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Cancelled', 'All', assigned_store)
        return render(request, 'orders/cancelledFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def refundedFranchiseOrders(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        orders_list, status_code = franchise_store_orders_controller.get_all_orders('Cancelled', 'Refunded',
                                                                                    assigned_store)
        return render(request, 'orders/refundedFranchiseOrders.html', {"orders_list": orders_list["orders_list"]})
    else:
        return redirect('franchise_store_login')


def orderDetailsFranchise(request, orderId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        order_detail, status_code = franchise_store_orders_controller.get_order_details(orderId)
        payment_logs, status_code = orders_controller.get_payment_logs(orderId)
        lab_details, lab_status_code = lab_controller.get_lab_by_id(
            order_detail['orders_details'][0]['so_assigned_lab'])
        return render(request, 'orders/orderDetailsFranchise.html', {"order_detail": order_detail['orders_details'],
                                                                     "payment_logs": payment_logs['payment_logs'],
                                                                     "lab_details": lab_details['lab_data']})
    else:
        return redirect('franchise_store_login')


def orderInvoiceFranchise(request, orderId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        order_detail, status_code = franchise_store_orders_controller.get_order_details(orderId)
        invoice_details, inv_status_code = orders_controller.get_invoice_details(orderId)
        store_data, store_status_code = franchise_store_orders_controller.get_store_details(
            order_detail['orders_details'][0]['so_created_by_store'],
            order_detail['orders_details'][0]['so_created_by_store_type'])
        return render(request, 'orders/franchise_order_invoice.html', {"order_detail": order_detail['orders_details'],
                                                                       "store_data": store_data['store_data'],
                                                                       "invoice_details": invoice_details[
                                                                           'invoice_details']})
    else:
        return redirect('franchise_store_login')


def franchiseOrderStatusChange(request, orderId, status):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        order_detail, status_code = franchise_store_orders_controller.franchise_order_status_change(orderId, status,
                                                                                                    request.session.get(
                                                                                                        'id'),
                                                                                                    assigned_store)
        url = reverse('order_details_franchise_store', kwargs={'orderId': orderId})
        return redirect(url)
    else:
        return redirect('franchise_store_login')


def franchisePaymentStatusChange(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        order_obj = order_payment_status_change_model.order_payment_status_change_model_from_dict(request.POST)
        order_detail, status_code = franchise_store_orders_controller.franchise_payment_status_change(vars(order_obj),
                                                                                                      assigned_store,
                                                                                                      request.session.get(
                                                                                                          'id'))
        url = reverse('order_details_franchise_store', kwargs={'orderId': order_obj.get_attribute('order_id')})
        return redirect(url)
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE CUSTIOMER MANAGEMENT ======================================

def viewAllCustomersFranchise(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_customers_controller.get_all_franchise_store_customers(assigned_store)
        return render(request, 'customers/viewAllCustomersFranchise.html',
                      {"store_customers_list": response['store_customers_list']})
    else:
        return redirect('franchise_store_login')


def viewCustomerDetailsFranchise(request, customerId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_customers_controller.get_customers_by_id(customerId)
        spending, status_code = customers_controller.get_customer_spend(customerId)
        sales_data, sale_status_code = franchise_store_orders_controller.get_all_customer_orders(customerId)

        membership = "Gold"

        if spending['total_spending'] > 5000 and spending['total_spending'] < 25000:
            membership = "Platinum"
        elif spending['total_spending'] > 25000:
            membership = "Luxury"
        return render(request, 'customers/viewCustomerDetailsFranchise.html', {"customers": response['customers'],
                                                                               "sales_data": sales_data[
                                                                                   'orders_list'],
                                                                               "membership": membership})
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE EMPLOYEE MANAGEMENT ======================================

def viewAllEmployeFranchise(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_employee_controller.get_all_franchise_emp(assigned_store)
        print(response)
        return render(request, 'employee/manageFranchiseEmployees.html',
                      {"franchise_employee_list": response['franchise_employee_list']})
    else:
        return redirect('franchise_store_login')


def viewEmployeeDetailsFranchise(request, employeeId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_employee_controller.get_franchise_emp_by_id(assigned_store, employeeId)
        print(response)
        return render(request, 'employee/viewEmployee.html',
                      {"franchise_employee": response['franchise_employee']})
    else:
        return redirect('franchise_store_login')


def viewEmployeeDetailsOwn(request, employeeId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_employee_controller.get_own_store_employee_by_id(employeeId)

        return render(request, 'employee/viewEmployee.html',
                      {"franchise_employee": response['franchise_employee']})
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE STOCK REQUESTS MANAGEMENT ======================================

def createStockRequestFranchise(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        if request.method == 'POST':
            stock_obj = franchise_create_stock_request_model.franchise_create_stock_request_model_from_dict(
                request.POST)
            response = franchise_inventory_controller.create_store_stock_request(stock_obj)
            return redirect('create_request_franchise_store')
        else:
            response, status_code = franchise_inventory_controller.get_all_central_inventory_products(assigned_store)

            return render(request, 'stockRequests/createStockRequestFranchise.html',
                          {"product_list": response['product_list']})
    else:
        return redirect('franchise_store_login')


def viewAllStockRequestsFranchise(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.view_all_store_stock_request(assigned_store, '%')
        return render(request, 'stockRequests/viewAllStockRequestsFranchise.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('franchise_store_login')


def viewPendingStockRequestsFranchise(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.view_all_store_stock_request(assigned_store, '0')
        return render(request, 'stockRequests/viewPendingStockRequestsFranchise.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('franchise_store_login')


def viewCompletedStockRequestsFranchise(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.view_all_store_stock_request(
            assigned_store, '1')
        return render(request, 'stockRequests/viewCompletedStockRequestsFranchise.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('franchise_store_login')


def viewRejectedStockRequestsFranchise(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.view_all_store_stock_request(
            assigned_store, '2')
        return render(request, 'stockRequests/viewRejectedStockRequestsFranchise.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('franchise_store_login')


def stockRequestDeliveryStatusChange(request, requestId, status):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.request_delivery_status_change(requestId, status,
                                                                                              request.session.get('id'))

        return redirect('completed_franchise_store_stock_requests')
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE INVENTORY MANAGEMENT ======================================

def franchiseInventoryProducts(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.get_all_products_for_franchise_store(
            assigned_store)
        return render(request, 'inventory/franchiseInventoryProducts.html', {"stocks_list": response['stocks_list'],
                                                                             "categories_List": response[
                                                                                 'product_category']})
    else:
        return redirect('franchise_store_login')


def viewFranchiseStoreInventoryProducts(request, productId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.get_products_for_franchise_store_by_id(assigned_store,
                                                                                                      productId)
        return render(request, 'inventory/franchiseStoreInventoryProductsView.html',
                      {"stocks_list": response['stocks_list']})
    else:
        return redirect('franchise_store_login')


def viewFranchiseCentralStoreInventoryProducts(request, productId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = get_central_inventory_product_single(productId)

        return render(request, 'inventory/franchiseCentralInventoryProductsView.html',
                      {"product_data": response['product_data']})
    else:
        return redirect('franchise_store_login')


def inventoryOutOfStockFranchise(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_inventory_controller.get_all_out_of_stock_products_for_franchise_store(15,
                                                                                                                 assigned_store)
        return render(request, 'inventory/inventoryOutOfStockFranchise.html', {"stocks_list": response['stocks_list'],
                                                                               "categories_List": response[
                                                                                   'product_category']})
    else:
        return redirect('franchise_store_login')


# ================================= SALES AND EXPENSES ======================================

def allExpenseFranchise(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        if request.method == 'POST':
            expense_obj = franchise_expense_model.franchise_expense_model_from_dict(request.POST)
            response, status_code = franchise_expense_controller.create_franchise_store_expense(expense_obj)
            return redirect('all_expenses_franchise_store')
        else:
            response, status_code = franchise_expense_controller.get_all_franchise_store_expense(
                assigned_store,
                request.session.get('store_type'))
            return render(request, 'expenses/allExpenseFranchise.html',
                          {"stor_expense_list": response['stor_expense_list']})
    else:
        return redirect('franchise_store_login')


def makeSaleFranchiseStore(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        if request.method == 'POST':
            order_id = f"""fs_{assigned_store}_{franchise_expense_controller.get_current_epoch_time()}"""
            cart_data = json.loads(request.POST['cartData'])
            customerData = json.loads(request.POST['customerData'])
            billingDetailsData = json.loads(request.POST['billingDetailsData'])
            make_order, status_code = franchise_expense_controller.make_sale(cart_data, customerData,
                                                                             billingDetailsData,
                                                                             request.session.get('id'),
                                                                             assigned_store, order_id)
            url = reverse('order_details_franchise_store', kwargs={'orderId': order_id})
            return redirect(url)
        else:
            employee_list, emp_status_code = franchise_store_employee_controller.get_all_active_franchise_emp(
                assigned_store)
            lab_list, lab_status_code = franchise_store_lab_controller.get_all_active_labs()
            store_products, status_code = franchise_inventory_controller.get_all_products_for_store(
                assigned_store)
            customerResponse, cust_status_code = franchise_store_customers_controller.get_all_customers()
            lens_response, lens_status_code = central_inventory_controller.get_central_inventory_lens(
                assigned_store)

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
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        if request.method == 'POST':
            response = franchise_store_eye_test_controller.add_eye_test(request.POST, request.session.get('id'),
                                                                        assigned_store)
            return redirect('get_franchise_eye_test')
        else:
            customerResponse, cust_status_code = franchise_store_customers_controller.get_all_customers()
            print(customerResponse)
            optometryResponse, cust_status_code = franchise_store_employee_controller.get_all_active_store_optometry(
                assigned_store)
            print(optometryResponse)
            return render(request, 'franchiseStoreEyeTest/franchiseStoreEyeTest.html',
                          {'customers_list': customerResponse['customers_list'],
                           'optometry_list': optometryResponse['optometry_list']})
    else:
        return redirect('franchise_store_login')


def getfranchiseStoreEyeTest(request):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_eye_test_controller.get_eye_test()
        return render(request, 'franchiseStoreEyeTest/viewAllStoreEyeTest.html',
                      {'eye_test_list': response['eye_test_list']})

    else:
        return redirect('franchise_store_login')


def getfranchiseStoreEyeTestById(request, testId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = franchise_store_eye_test_controller.get_eye_test_by_id(testId)

        return render(request, 'franchiseStoreEyeTest/viewAllStoreEyeTest.html',
                      {'eye_test_list': response['eye_test']})

    else:
        return redirect('franchise_store_login')


def franchiseStoreEyeTestPrint(request, testId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get(
            'is_franchise_store_logged_in') is True:
        response, status_code = eye_test_controller.get_eye_test_by_id(testId)

        return render(request, 'franchiseStoreEyeTest/franchiseStoreEyeTestPrint.html',
                      {'eye_test_list': response['eye_test']})

    else:
        return redirect('franchise_store_login')

def viewFranchiseJobAuthenticityCard(request, saleId, frame):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get('is_franchise_store_logged_in') is True:
        job_detail, status_code = lab_controller.get_lab_job_authenticity_card(saleId)
        print(job_detail)
        return render(request, 'orders/authenticityCar.html', {"order_detail": job_detail['orders_details'],
                                                               "frame": frame})
    else:
        return redirect('franchise_store_login')

def franchiseStoreContactLensPowerCard(request, saleId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get('is_franchise_store_logged_in') is True:
        job_detail, status_code = lab_controller.get_lab_job_authenticity_card(saleId)
        print(job_detail)
        return render(request, 'indolens_admin/labs/contactLensPowerCard.html',
                      {"order_detail": job_detail['orders_details']})
    else:
        return redirect('franchise_store_login')

def viewFranchiseJobItemDetails(request, saleId):
    assigned_store = getAssignedStores(request)
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get('is_franchise_store_logged_in') is True:
        job_detail, status_code = lab_controller.get_lab_job_authenticity_card(saleId)
        print(job_detail['frame_list'])
        return render(request, 'orders/franchiseJobItemDetails.html',
                      {"job_item_detail": job_detail['orders_details'],
                       "frame_list": job_detail['frame_list']})
    else:
        return redirect('franchise_store_login')
