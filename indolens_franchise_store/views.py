from django.shortcuts import redirect, render


# =================================ADMIN START======================================

def index(request):
    return redirect('franchise_store_login')


# ================================= FRANCHISE STORE AUTH ======================================

def login(request):
    if request.method == 'POST':
        return redirect('franchise_store_dashboard')
    return render(request, 'auth/franchise_sign_in.html')


def forgotPassword(request):
    return render(request, 'auth/franchise_store_forgot_password.html')


def resetPassword(request):
    return render(request, 'auth/franchise_store_reset_password.html')


def franchiseOwnerLogout(request):
    return redirect('franchise_store_login')


# ================================= FRANCHISE STORE DASHBOARD ======================================
def dashboard(request):
    return render(request, 'franchise_dashboard.html')


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
