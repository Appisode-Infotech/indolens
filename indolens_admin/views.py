from django.shortcuts import render, redirect


# =================================ADMIN START======================================
def index(request):
    return redirect('login')


# =================================ADMIN AUTH======================================

def login(request):
    if request.method == 'POST':
        return redirect('dashboard')
    else:
        return render(request, 'indolens_admin/auth/sign_in.html')


def forgotPassword(request):
    return render(request, 'indolens_admin/auth/forgot_password.html')


def resetPassword(request):
    return render(request, 'indolens_admin/auth/reset_password.html')


# =================================ADMIN DASH======================================

def dashboard(request):
    return render(request, 'indolens_admin/dashboard.html')


# =================================ADMIN STORE MANAGEMENT======================================

def manageOwnStores(request):
    return render(request, 'indolens_admin/ownStore/manageOwnStores.html')


def viewOwnStore(request):
    return render(request, 'indolens_admin/ownStore/ownStore.html')


def editOwnStore(request):
    return render(request, 'indolens_admin/ownStore/editOwnStore.html')


def createOwnStore(request):
    return render(request, 'indolens_admin/ownStore/createOwnStore.html')


def manageFranchiseStores(request):
    return render(request, 'indolens_admin/franchiseStores/manageFranchiseStores.html')


def viewFranchiseStore(request):
    return render(request, 'indolens_admin/franchiseStores/franchiseStore.html')


def editFranchiseStore(request):
    return render(request, 'indolens_admin/franchiseStores/editFranchiseStore.html')


def createFranchiseStore(request):
    return render(request, 'indolens_admin/franchiseStores/createFranchiseStore.html')


# =================================ADMIN SUB ADMIN MANAGEMENT======================================

def manageSubAdmins(request):
    return render(request, 'indolens_admin/subAdmin/manageSubAdmins.html')


def createSubAdmin(request):
    return render(request, 'indolens_admin/subAdmin/createSubAdmin.html')


def editSubAdmin(request):
    return render(request, 'indolens_admin/subAdmin/editSubAdmin.html')


def viewSubAdmin(request):
    return render(request, 'indolens_admin/subAdmin/viewSubAdmin.html')


# =================================ADMIN STORE MANAGERS MANAGEMENT======================================

def manageStoreManagers(request):
    return render(request, 'indolens_admin/storeManagers/manageStoreManagers.html')


def createStoreManager(request):
    return render(request, 'indolens_admin/storeManagers/createStoreManager.html')


def viewStoreManager(request):
    return render(request, 'indolens_admin/storeManagers/viewStoreManager.html')


def editStoreManager(request):
    return render(request, 'indolens_admin/storeManagers/editStoreManager.html')


# =================================ADMIN FRANCHISE OWNERS MANAGEMENT======================================

def manageFranchiseOwners(request):
    return render(request, 'indolens_admin/franchiseOwners/manageFranchiseOwners.html')


def createFranchiseOwners(request):
    return render(request, 'indolens_admin/franchiseOwners/createFranchiseOwner.html')


def editFranchiseOwners(request):
    return render(request, 'indolens_admin/franchiseOwners/editFranchiseOwner.html')


def viewFranchiseOwners(request):
    return render(request, 'indolens_admin/franchiseOwners/viewFranchiseOwner.html')


# =================================ADMIN AREA HEADS MANAGEMENT======================================

def manageAreaHead(request):
    return render(request, 'indolens_admin/areaHead/manageAreaHead.html')


def createAreaHead(request):
    return render(request, 'indolens_admin/areaHead/createAreaHead.html')


def editAreaHead(request):
    return render(request, 'indolens_admin/areaHead/editAreaHead.html')


def viewAreaHead(request):
    return render(request, 'indolens_admin/areaHead/viewAreaHead.html')


# =================================ADMIN MARKETING HEADS MANAGEMENT======================================

def manageMarketingHead(request):
    return render(request, 'indolens_admin/marketingHeads/manageMarketingHead.html')


def createMarketingHead(request):
    return render(request, 'indolens_admin/marketingHeads/createMarketingHead.html')


def editMarketingHead(request):
    return render(request, 'indolens_admin/marketingHeads/editMarketingHead.html')


def viewMarketingHead(request):
    return render(request, 'indolens_admin/marketingHeads/viewMarketingHead.html')


# =================================ADMIN OPTIMETRY MANAGEMENT======================================


def manageOptimetry(request):
    return render(request, 'indolens_admin/optimetry/manageOptimetry.html')


def createOptimetry(request):
    return render(request, 'indolens_admin/optimetry/createOptimetry.html')


def editOptimetry(request):
    return render(request, 'indolens_admin/optimetry/editOptimetry.html')


def viewOptimetry(request):
    return render(request, 'indolens_admin/optimetry/viewOptimetry.html')


# =================================ADMIN OPTIMETRY MANAGEMENT======================================


def manageSaleExecutives(request):
    return render(request, 'indolens_admin/salesExecutive/manageSaleExecutives.html')


def createSaleExecutives(request):
    return render(request, 'indolens_admin/salesExecutive/createSaleExecutives.html')


def editSaleExecutives(request):
    return render(request, 'indolens_admin/salesExecutive/editSaleExecutives.html')


def viewSaleExecutives(request):
    return render(request, 'indolens_admin/salesExecutive/viewSaleExecutives.html')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageAccountant(request):
    return render(request, 'indolens_admin/accountant/manageAccountant.html')


def createAccountant(request):
    return render(request, 'indolens_admin/accountant/createAccountant.html')


def editAccountant(request):
    return render(request, 'indolens_admin/accountant/editAccountant.html')


def viewAccountant(request):
    return render(request, 'indolens_admin/accountant/viewAccountant.html')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageLabTechnician(request):
    return render(request, 'indolens_admin/labTechnician/manageLabTechnician.html')


def createLabTechnician(request):
    return render(request, 'indolens_admin/labTechnician/createLabTechnician.html')


def editLabTechnician(request):
    return render(request, 'indolens_admin/labTechnician/editLabTechnician.html')


def viewLabTechnician(request):
    return render(request, 'indolens_admin/labTechnician/viewLabTechnician.html')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageOtherEmployees(request):
    return render(request, 'indolens_admin/otherEmployees/manageOtherEmployees.html')


def createOtherEmployees(request):
    return render(request, 'indolens_admin/otherEmployees/createOtherEmployees.html')


def editOtherEmployees(request):
    return render(request, 'indolens_admin/otherEmployees/editOtherEmployees.html')


def viewOtherEmployees(request):
    return render(request, 'indolens_admin/otherEmployees/viewOtherEmployees.html')


# =================================ADMIN ORDERS MANAGEMENT======================================

def viewAllOrders(request):
    return render(request, 'indolens_admin/orders/viewAllOrders.html')


def viewPendingOrders(request):
    return render(request, 'indolens_admin/orders/viewPendingOrders.html')


def viewReceivedOrders(request):
    return render(request, 'indolens_admin/orders/viewReceivedOrders.html')


def viewProcessingOrders(request):
    return render(request, 'indolens_admin/orders/viewProcessingOrders.html')


def viewReadyOrders(request):
    return render(request, 'indolens_admin/orders/viewReadyOrders.html')


def viewDeliveredOrders(request):
    return render(request, 'indolens_admin/orders/viewDeliveredOrders.html')


def viewCancelledOrders(request):
    return render(request, 'indolens_admin/orders/viewCancelledOrders.html')


def viewRefundedOrders(request):
    return render(request, 'indolens_admin/orders/viewRefundedOrders.html')


def viewOrderDetails(request):
    return render(request, 'indolens_admin/orders/viewOrderDetails.html')


# =================================ADMIN CUSTOMERS MANAGEMENT======================================

def viewAllCustomers(request):
    return render(request, 'indolens_admin/customers/viewAllCustomers.html')


def viewCustomerDetails(request):
    return render(request, 'indolens_admin/customers/viewCustomerDetails.html')


# =================================ADMIN LABS MANAGEMENT======================================

def manageLabs(request):
    return render(request, 'indolens_admin/labs/manageLabs.html')


def createLab(request):
    return render(request, 'indolens_admin/labs/createLab.html')


def editLab(request):
    return render(request, 'indolens_admin/labs/editLab.html')


def viewLab(request):
    return render(request, 'indolens_admin/labs/viewLab.html')


def viewActiveJobs(request):
    return render(request, 'indolens_admin/labs/viewActiveJobs.html')


def viewAllJobs(request):
    return render(request, 'indolens_admin/labs/viewAllJobs.html')


def jobDetails(request):
    return render(request, 'indolens_admin/labs/jobDetails.html')


def manageAuthenticityCard(request):
    return render(request, 'indolens_admin/labs/manageAuthenticityCard.html')


def createAuthenticityCard(request):
    return render(request, 'indolens_admin/labs/createAuthenticityCard.html')


# =================================ADMIN LABS MANAGEMENT======================================

def manageMastersCategory(request):
    return render(request, 'indolens_admin/masters/manageMastersCategory.html')


def addProductCategory(request):
    return render(request, 'indolens_admin/masters/addProductCategory.html')


def manageMastersBrands(request):
    return render(request, 'indolens_admin/masters/manageMastersBrands.html')


def addMastersBrands(request):
    return render(request, 'indolens_admin/masters/addMastersBrand.html')


def manageMastersShapes(request):
    return render(request, 'indolens_admin/masters/manageMastersShapes.html')


def addMastersShapes(request):
    return render(request, 'indolens_admin/masters/addMastersShapes.html')


def manageMastersFrameType(request):
    return render(request, 'indolens_admin/masters/manageMastersFrameType.html')


def addMastersFrameType(request):
    return render(request, 'indolens_admin/masters/addMastersFrameType.html')


def manageMastersColor(request):
    return render(request, 'indolens_admin/masters/manageMastersColor.html')


def addMastersColor(request):
    return render(request, 'indolens_admin/masters/addMastersColor.html')


def manageMastersMaterials(request):
    return render(request, 'indolens_admin/masters/manageMastersMaterials.html')


def addMastersMaterials(request):
    return render(request, 'indolens_admin/masters/addMastersMaterials.html')


def manageMastersUnits(request):
    return render(request, 'indolens_admin/masters/manageMastersUnits.html')


# =================================ADMIN STORE MANAGEMENT======================================


def manageCentralInventoryProducts(request):
    return render(request, 'indolens_admin/centralInventory/manageCentralInventoryProducts.html')


def centralInventoryAddProducts(request):
    return render(request, 'indolens_admin/centralInventory/centralInventoryAddProducts.html')


def manageCentralInventoryOutOfStock(request):
    return render(request, 'indolens_admin/centralInventory/manageCentralInventoryOutOfStock.html')


def manageMoveStocks(request):
    return render(request, 'indolens_admin/centralInventory/manageMoveStocks.html')


def manageMoveAStock(request):
    return render(request, 'indolens_admin/centralInventory/manageMoveAStock.html')


# =================================ADMIN STORE MANAGEMENT======================================


def viewAllStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewAllStockRequests.html')


def viewPendingStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewPendingStockRequests.html')


def viewCompletedStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewCompletedStockRequests.html')


def viewrejectedStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewrejectedStockRequests.html')
