from django.shortcuts import redirect, render

from indolens_franchise_store.franchise_store_controller import franchise_store_auth_controller
from indolens_franchise_store.franchise_store_model.franchise_store_req_model import franchise_store_employee_model


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
    return render(request, 'auth/franchise_store_forgot_password.html')


def resetPassword(request):
    return render(request, 'auth/franchise_store_reset_password.html')


def franchiseOwnerLogout(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get('is_franchise_store_logged_in') is True:
        request.session.clear()
        return redirect('franchise_store_login')
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE DASHBOARD ======================================
def dashboard(request):
    if request.session.get('is_franchise_store_logged_in') is not None and request.session.get('is_franchise_store_logged_in') is True:
        return render(request, 'franchise_dashboard.html')
    else:
        return redirect('franchise_store_login')


# ================================= FRANCHISE STORE ORDER MANAGEMENT ======================================
def allFranchiseOrders(request):
    return render(request, 'orders/allFranchiseOrders.html')


def pendingFranchiseOrders(request):
    return render(request, 'orders/pendingFranchiseOrders.html')


def receivedFranchiseOrders(request):
    return render(request, 'orders/receivedFranchiseOrders.html')


def processingFranchiseOrders(request):
    return render(request, 'orders/processingFranchiseOrders.html')


def readyFranchiseOrders(request):
    return render(request, 'orders/readyFranchiseOrders.html')


def deliveredFranchiseOrders(request):
    return render(request, 'orders/deliveredFranchiseOrders.html')


def cancelledFranchiseOrders(request):
    return render(request, 'orders/cancelledFranchiseOrders.html')


def refundedFranchiseOrders(request):
    return render(request, 'orders/refundedFranchiseOrders.html')


def orderDetailsFranchise(request):
    return render(request, 'orders/orderDetailsFranchise.html')


# ================================= FRANCHISE STORE CUSTIOMER MANAGEMENT ======================================

def viewAllCustomersFranchise(request):
    return render(request, 'customers/viewAllCustomersFranchise.html')


def viewCustomerDetailsFranchise(request):
    return render(request, 'customers/viewCustomerDetailsFranchise.html')


# ================================= FRANCHISE STORE STOCK REQUESTS MANAGEMENT ======================================

def createStockRequestFranchise(request):
    return render(request, 'stockRequests/createStockRequestFranchise.html')


def viewAllStockRequestsFranchise(request):
    return render(request, 'stockRequests/viewAllStockRequestsFranchise.html')


def viewPendingStockRequestsFranchise(request):
    return render(request, 'stockRequests/viewPendingStockRequestsFranchise.html')


def viewCompletedStockRequestsFranchise(request):
    return render(request, 'stockRequests/viewCompletedStockRequestsFranchise.html')


def viewRejectedStockRequestsFranchise(request):
    return render(request, 'stockRequests/viewRejectedStockRequestsFranchise.html')


# ================================= FRANCHISE STORE INVENTORY MANAGEMENT ======================================

def franchiseInventoryProducts(request):
    return render(request, 'inventory/franchiseInventoryProducts.html')


def inventoryOutOfStockFranchise(request):
    return render(request, 'inventory/inventoryOutOfStockFranchise.html')


def moveStocksFranchise(request):
    return render(request, 'inventory/moveStocksFranchise.html')


# ================================= SALES AND EXPENSES ======================================

def allExpenseFranchise(request):
    return render(request, 'expenses/allExpenseFranchise.html')


def makeSaleFranchiseStore(request):
    return render(request, 'expenses/makeSaleFranchiseStore.html')
