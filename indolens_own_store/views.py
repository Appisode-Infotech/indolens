# =================================ADMIN START======================================
from django.shortcuts import redirect, render


def index(request):
    return redirect('own_store_login')


# ================================= OWN STORE AUTH ======================================

def login(request):
    if request.method == 'POST':
        return redirect('own_store_dashboard')
    return render(request, 'auth/sign_in.html')


def forgotPassword(request):
    return render(request, 'auth/forgot_password.html')


def resetPassword(request):
    return render(request, 'auth/reset_password.html')


# ================================= OWN STORE DASHBOARD ======================================
def dashboard(request):
    return render(request, 'dashboard.html')


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
    return render(request, 'stockRequests/createStockRequestStore.html')


def viewAllStockRequestsStore(request):
    return render(request, 'stockRequests/viewAllStockRequestsStore.html')


def viewPendingStockRequestsStore(request):
    return render(request, 'stockRequests/viewPendingStockRequestsStore.html')


def viewCompletedStockRequestsStore(request):
    return render(request, 'stockRequests/viewCompletedStockRequestsStore.html')


def viewRejectedStockRequestsStore(request):
    return render(request, 'stockRequests/viewRejectedStockRequestsStore.html')


# ================================= OWN STORE INVENTORY MANAGEMENT ======================================

def storeInventoryProducts(request):
    return render(request, 'inventory/storeInventoryProducts.html')


def inventoryOutOfStock(request):
    return render(request, 'inventory/inventoryOutOfStock.html')


def moveStocksStore(request):
    return render(request, 'inventory/moveStocksStore.html')


# ================================= SALES AND EXPENSES ======================================

def allExpenseStore(request):
    return render(request, 'expenses/allExpenseStore.html')


def makeSaleOwnStore(request):
    return render(request, 'expenses/makeSaleOwnStore.html')
