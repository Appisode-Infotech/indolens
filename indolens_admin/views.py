from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
import time

from rest_framework.reverse import reverse

from indolens_admin.admin_controllers import admin_auth_controller, own_store_controller, franchise_store_controller, \
    sub_admin_controller, store_manager_controller, franchise_owner_controller, area_head_controller
from indolens_admin.admin_controllers.employee_files_model import FileData
from indolens_admin.admin_models.admin_req_model import admin_auth_model, own_store_model, franchise_store_model, \
    sub_admin_model, store_manager_model, franchise_owner_model, area_head_model


# =================================ADMIN START======================================
def index(request):
    return redirect('login')


# =================================ADMIN AUTH======================================

def login(request):
    if request.method == 'POST':
        admin_obj = admin_auth_model.admin_auth_model_from_dict(request.POST)
        response, status_code = admin_auth_controller.login(admin_obj)
        if response['status']:
            request.session.update({
                'is_admin_logged_in': True,
                'id': response['admin'].admin_id,
                'name': response['admin'].name,
                'profile_pic': response['admin'].profile_pic,
            })
            return redirect('dashboard')
        else:
            return render(request, 'indolens_admin/auth/sign_in.html', {"message": response['message']})

    else:
        return render(request, 'indolens_admin/auth/sign_in.html')


def forgotPassword(request):
    return render(request, 'indolens_admin/auth/forgot_password.html')


def resetPassword(request):
    return render(request, 'indolens_admin/auth/reset_password.html')


# =================================ADMIN DASH======================================

def dashboard(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        own_stores, status_code = own_store_controller.get_all_own_stores()
        franchise_store, status_code = franchise_store_controller.get_all_franchise_stores()
        return render(request, 'indolens_admin/dashboard.html',
                      {"own_store_list": own_stores['own_stores'],
                       "franchise_store_list": franchise_store['franchise_store']})
    else:
        return redirect('login')


# =================================ADMIN STORE MANAGEMENT======================================

def manageOwnStores(request):
    response, status_code = own_store_controller.get_all_own_stores()
    return render(request, 'indolens_admin/ownStore/manageOwnStores.html', {"own_store_list": response['own_stores']})


def viewOwnStore(request, sid):
    response, status_code = own_store_controller.get_own_store_by_id(sid)
    return render(request, 'indolens_admin/ownStore/ownStore.html', {"store_data": response['own_stores']})


def editOwnStore(request, sid):
    if request.method == 'POST':
        store_obj = own_store_model.own_store_model_from_dict(request.POST)
        response, status_code = own_store_controller.edit_own_store_by_id(store_obj)
        if status_code != 200:
            return render(request, 'indolens_admin/ownStore/editOwnStore.html', {"message": response['message']})
        else:
            return redirect('manage_own_stores')

    else:
        response, status_code = own_store_controller.get_own_store_by_id(sid)
        return render(request, 'indolens_admin/ownStore/editOwnStore.html',
                      {"store_data": response['own_stores'], "id": sid})


def createOwnStore(request):
    if request.method == 'POST':
        store_obj = own_store_model.own_store_model_from_dict(request.POST)
        response, status_code = own_store_controller.create_own_store(store_obj)
        if status_code != 200:
            return render(request, 'indolens_admin/ownStore/createOwnStore.html', {"message": response['message']})
        else:
            return redirect('manage_own_stores')
    return render(request, 'indolens_admin/ownStore/createOwnStore.html')


def manageFranchiseStores(request):
    response, status_code = franchise_store_controller.get_all_franchise_stores()
    return render(request, 'indolens_admin/franchiseStores/manageFranchiseStores.html',
                  {"franchise_store_list": response['franchise_store']})


def viewFranchiseStore(request, fid):
    response, status_code = franchise_store_controller.get_franchise_store_by_id(fid)
    return render(request, 'indolens_admin/franchiseStores/franchiseStore.html',
                  {"franchise_store": response['franchise_store']})


def editFranchiseStore(request, fid):
    if request.method == 'POST':
        franchise_obj = franchise_store_model.franchise_store_model_from_dict(request.POST)
        response, status_code = franchise_store_controller.edit_franchise_store_by_id(franchise_obj)
        if status_code != 200:
            return render(request, 'indolens_admin/ownStore/editOwnStore.html', {"message": response['message']})
        else:
            return redirect('manage_Franchise_stores')

    else:
        response, status_code = franchise_store_controller.get_franchise_store_by_id(fid)
        return render(request, 'indolens_admin/franchiseStores/editFranchiseStore.html',
                      {"franchise_store": response['franchise_store'], "id": fid})


def createFranchiseStore(request):
    if request.method == 'POST':
        franchise_obj = franchise_store_model.franchise_store_model_from_dict(request.POST)
        response, status_code = franchise_store_controller.create_franchise_store(franchise_obj)
        if status_code != 200:
            return render(request, 'indolens_admin/franchiseStores/createFranchiseStore.html',
                          {"message": response['message']})
        else:
            return redirect('manage_Franchise_stores')

    return render(request, 'indolens_admin/franchiseStores/createFranchiseStore.html')


# =================================ADMIN SUB ADMIN MANAGEMENT======================================

def manageSubAdmins(request):
    response, status_code = sub_admin_controller.get_all_sub_admin()
    return render(request, 'indolens_admin/subAdmin/manageSubAdmins.html', {"sub_admin_list": response['sub_admins']})


def createSubAdmin(request):
    if request.method == 'POST':
        form_data = {}
        file_data = {}
        file_label_mapping = {
            'profilePic': 'profile_pic',
            'document1': 'documents',
            'document2': 'documents',
        }

        for file_key, file_objs in request.FILES.lists():
            label = file_label_mapping.get(file_key, 'unknown')
            subdirectory = f"{label}/"
            file_list = []

            for index, file_obj in enumerate(file_objs):
                file_name = f"{subdirectory}{label}_{str(file_obj)}_{int(time.time())}"
                form_data_key = f"doc"
                file_dict = {form_data_key: file_name}

                with default_storage.open(file_name, 'wb+') as destination:
                    for chunk in file_obj.chunks():
                        destination.write(chunk)

                file_list.append(file_dict)

            if len(file_list) == 1:
                file_data[file_key] = file_list[0]
            else:
                file_data[file_key] = file_list

        # Combine the file data with the original form data
        for key, value in file_data.items():
            form_data[key] = value

        file_data = FileData(form_data)

        sub_admin = sub_admin_model.sub_admin_model_from_dict(form_data)
        response = sub_admin_controller.create_sub_admin(sub_admin, file_data)
        print(response)
        return redirect('manage_sub_admins')

    else:
        return render(request, 'indolens_admin/subAdmin/createSubAdmin.html')


def editSubAdmin(request, said):
    if request.method == 'POST':
        sub_admin = sub_admin_model.sub_admin_model_from_dict(request.POST)
        response, status_code = sub_admin_controller.edit_sub_admin(sub_admin)
        return redirect('manageSubAdmins')
    else:
        response, status_code = sub_admin_controller.get_sub_admin_by_id(said)
        return render(request, 'indolens_admin/subAdmin/editSubAdmin.html', {"sub_admin": response['sub_admin']})


def viewSubAdmin(request, said):
    response, status_code = sub_admin_controller.get_sub_admin_by_id(said)
    return render(request, 'indolens_admin/subAdmin/viewSubAdmin.html', {"sub_admin": response['sub_admin']})


# =================================ADMIN STORE MANAGERS MANAGEMENT======================================

def manageStoreManagers(request):
    response, status_code = store_manager_controller.get_all_store_manager()
    return render(request, 'indolens_admin/storeManagers/manageStoreManagers.html',
                  {"store_managers": response['store_managers']})


def createStoreManager(request):
    if request.method == 'POST':
        form_data = {}
        file_data = {}
        file_label_mapping = {
            'profilePic': 'profile_pic',
            'document1': 'documents',
            'document2': 'documents',
        }

        for file_key, file_objs in request.FILES.lists():
            label = file_label_mapping.get(file_key, 'unknown')
            subdirectory = f"{label}/"
            file_list = []

            for index, file_obj in enumerate(file_objs):
                file_name = f"{subdirectory}{label}_{str(file_obj)}_{int(time.time())}"
                form_data_key = f"doc"
                file_dict = {form_data_key: file_name}

                with default_storage.open(file_name, 'wb+') as destination:
                    for chunk in file_obj.chunks():
                        destination.write(chunk)

                file_list.append(file_dict)

            if len(file_list) == 1:
                file_data[file_key] = file_list[0]
            else:
                file_data[file_key] = file_list

        # Combine the file data with the original form data
        for key, value in file_data.items():
            form_data[key] = value

        file_data = FileData(form_data)

        store_manager = store_manager_model.store_manager_model_from_dict(form_data)
        resp, status_code = store_manager_controller.create_store_manager(store_manager, file_data)
        return redirect('manage_store_managers')
    else:
        return render(request, 'indolens_admin/storeManagers/createStoreManager.html')


def viewStoreManager(request, mid):
    response, status_code = store_manager_controller.get_store_manager_by_id(mid)
    return render(request, 'indolens_admin/storeManagers/viewStoreManager.html',
                  {"store_manager": response['store_manager']})


def editStoreManager(request, mid):
    if request.method == 'POST':
        print(request.POST)
        store_manager = store_manager_model.store_manager_model_from_dict(request.POST)
        print(store_manager)

    response, status_code = store_manager_controller.get_store_manager_by_id(mid)
    return render(request, 'indolens_admin/storeManagers/editStoreManager.html',
                  {"store_manager": response['store_manager']})


# =================================ADMIN FRANCHISE OWNERS MANAGEMENT======================================

def manageFranchiseOwners(request):
    response, status_code = franchise_owner_controller.get_all_franchise_owner()
    return render(request, 'indolens_admin/franchiseOwners/manageFranchiseOwners.html',
                  {"franchise_owners": response['franchise_owners']})


def createFranchiseOwners(request):
    if request.method == 'POST':
        form_data = {}
        file_data = {}
        file_label_mapping = {
            'profilePic': 'profile_pic',
            'document1': 'documents',
            'document2': 'documents',
        }

        for file_key, file_objs in request.FILES.lists():
            label = file_label_mapping.get(file_key, 'unknown')
            subdirectory = f"{label}/"
            file_list = []

            for index, file_obj in enumerate(file_objs):
                file_name = f"{subdirectory}{label}_{str(file_obj)}_{int(time.time())}"
                form_data_key = f"doc"
                file_dict = {form_data_key: file_name}

                with default_storage.open(file_name, 'wb+') as destination:
                    for chunk in file_obj.chunks():
                        destination.write(chunk)

                file_list.append(file_dict)

            if len(file_list) == 1:
                file_data[file_key] = file_list[0]
            else:
                file_data[file_key] = file_list

        # Combine the file data with the original form data
        for key, value in file_data.items():
            form_data[key] = value

        file_data = FileData(form_data)

        franchise_owner_obj = franchise_owner_model.franchise_owner_model_from_dict(form_data)
        response, status_code = franchise_owner_controller.create_franchise_owner(franchise_owner_obj, file_data)
        url = reverse('view_franchise_owner', kwargs={'foid': response['foid']})
        return redirect(url)

    else:
        return render(request, 'indolens_admin/franchiseOwners/createFranchiseOwner.html')


def editFranchiseOwners(request, foid):
    if request.method == 'POST':
        form_data = request.POST
        file_label_mapping = {
            'profilePic': 'profile_pic',
            'document1': 'documents',
            'document2': 'documents',
        }
        for file_key, file_objs in request.FILES.lists():
            print("file also updated")
            label = file_label_mapping.get(file_key, 'unknown')
            subdirectory = f"{label}/"

            for file_obj in file_objs:
                file_name = f"{subdirectory}{label}_{str(file_obj)}_{int(time.time())}"
                form_data_key = f"{file_key}"

                form_data = form_data.copy()
                form_data[form_data_key] = file_name

                with default_storage.open(file_name, 'wb+') as destination:
                    for chunk in file_obj.chunks():
                        destination.write(chunk)

        franchise_owner = franchise_owner_model.franchise_owner_model_from_dict(form_data)
        response, status_code = franchise_owner_controller.edit_franchise_owner(franchise_owner)
        url = reverse('view_franchise_owner', kwargs={'foid': franchise_owner.franchise_owner_id})
        return redirect(url)

    else:
        response, status_code = franchise_owner_controller.get_franchise_owner_by_id(foid)
        return render(request, 'indolens_admin/franchiseOwners/editFranchiseOwner.html',
                      {"franchise_owner": response['franchise_owner']})


def viewFranchiseOwners(request, foid):
    response, status_code = franchise_owner_controller.get_franchise_owner_by_id(foid)

    return render(request, 'indolens_admin/franchiseOwners/viewFranchiseOwner.html',
                  {"franchise_owner": response['franchise_owner']})


# =================================ADMIN AREA HEADS MANAGEMENT======================================

def manageAreaHead(request):
    response, status_code = area_head_controller.get_all_area_head()
    return render(request, 'indolens_admin/areaHead/manageAreaHead.html',
                  {"area_heads_list": response['area_heads_list']})


def createAreaHead(request):
    if request.method == 'POST':
        form_data = {}
        file_data = {}
        file_label_mapping = {
            'profilePic': 'profile_pic',
            'document1': 'documents',
            'document2': 'documents',
        }

        for file_key, file_objs in request.FILES.lists():
            label = file_label_mapping.get(file_key, 'unknown')
            subdirectory = f"{label}/"
            file_list = []

            for index, file_obj in enumerate(file_objs):
                file_name = f"{subdirectory}{label}_{str(file_obj)}_{int(time.time())}"
                form_data_key = f"doc"
                file_dict = {form_data_key: file_name}

                with default_storage.open(file_name, 'wb+') as destination:
                    for chunk in file_obj.chunks():
                        destination.write(chunk)

                file_list.append(file_dict)

            if len(file_list) == 1:
                file_data[file_key] = file_list[0]
            else:
                file_data[file_key] = file_list

        # Combine the file data with the original form data
        for key, value in file_data.items():
            form_data[key] = value

        file_data = FileData(form_data)

        area_head = area_head_model.area_head_model_from_dict(request.POST)
        response, status_code = area_head_controller.create_area_head(area_head, file_data)

        url = reverse('view_area_head', kwargs={'foid': response['ahid']})
        return redirect(url)

    else:
        return render(request, 'indolens_admin/areaHead/createAreaHead.html')


def editAreaHead(request):
    return render(request, 'indolens_admin/areaHead/editAreaHead.html')


def viewAreaHead(request, ahid):
    response, status_code = area_head_controller.get_area_head_by_id(ahid)
    return render(request, 'indolens_admin/areaHead/viewAreaHead.html',
                  {"area_head": response['area_head']})


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
    response, status_code = own_store_controller.get_all_own_stores()
    return render(request, 'indolens_admin/centralInventory/manageMoveStocks.html',
                  {"own_store_list": response['own_stores']})


def manageMoveAStock(request):
    return render(request, 'indolens_admin/centralInventory/manageMoveAStock.html')


# =================================ADMIN STORE MANAGEMENT======================================


def viewAllStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewAllStockRequests.html')


def viewPendingStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewPendingStockRequests.html')


def viewCompletedStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewCompletedStockRequests.html')


def viewRejectedStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewrejectedStockRequests.html')
