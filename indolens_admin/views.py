import time

from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.reverse import reverse

from indolens_admin.admin_controllers import admin_auth_controller, own_store_controller, franchise_store_controller, \
    sub_admin_controller, store_manager_controller, franchise_manager_controller, area_head_controller, \
    marketing_head_controller, sales_executives_controller, accountant_controller, lab_technician_controller, \
    lab_controller, other_employee_controller, master_category_controller, master_brand_controller, \
    master_shape_controller, master_frame_type_controller, master_color_controller, master_material_controller, \
    optimetry_controller, master_units_controller, central_inventory_controller, delete_documents_controller
from indolens_admin.admin_models.admin_req_model import admin_auth_model, own_store_model, franchise_store_model, \
    sub_admin_model, area_head_model, marketing_head_model, \
    accountant_model, lab_technician_model, lab_model, \
    product_category_model, master_brand_model, master_shape_model, master_frame_type_model, master_color_model, \
    master_material_model, store_employee_model, central_inventory_products_model
from indolens_admin.admin_models.admin_req_model.files_model import FileData


# =================================ADMIN START======================================
def home(request):
    return redirect('login')


# =================================ADMIN AUTH======================================

def login(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        return redirect('dashboard')
    else:
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


def adminLogout(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        request.session.clear()
        return redirect(login)
    else:
        return redirect(login)


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
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = own_store_controller.get_all_own_stores()
        return render(request, 'indolens_admin/ownStore/manageOwnStores.html',
                      {"own_store_list": response['own_stores']})
    else:
        return redirect('login')


def viewOwnStore(request, ownStoreId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = own_store_controller.get_own_store_by_id(ownStoreId)
        return render(request, 'indolens_admin/ownStore/ownStore.html', {"store_data": response['own_stores']})
    else:
        return redirect('login')


def editOwnStore(request, ownStoreId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            store_obj = own_store_model.own_store_model_from_dict(request.POST)
            response, status_code = own_store_controller.edit_own_store_by_id(store_obj)
            if status_code != 200:
                return render(request, 'indolens_admin/ownStore/editOwnStore.html', {"message": response['message']})
            else:
                return redirect('manage_own_stores')

        else:
            response, status_code = own_store_controller.get_own_store_by_id(ownStoreId)
            return render(request, 'indolens_admin/ownStore/editOwnStore.html',
                          {"store_data": response['own_stores'], "id": ownStoreId})
    else:
        return redirect('login')


def createOwnStore(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            store_obj = own_store_model.own_store_model_from_dict(request.POST)
            response, status_code = own_store_controller.create_own_store(store_obj)
            if status_code != 200:
                return render(request, 'indolens_admin/ownStore/createOwnStore.html', {"message": response['message']})
            else:
                return redirect('manage_own_stores')
        return render(request, 'indolens_admin/ownStore/createOwnStore.html')
    else:
        return redirect('login')


def enableDisableOwnStore(request, ownStoreId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response = own_store_controller.enable_disable_own_store(ownStoreId, status)

        return redirect('manage_own_stores')
    else:
        return redirect('login')


def manageFranchiseStores(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_store_controller.get_all_franchise_stores()
        return render(request, 'indolens_admin/franchiseStores/manageFranchiseStores.html',
                      {"franchise_store_list": response['franchise_store']})
    else:
        return redirect('login')


def viewFranchiseStore(request, franchiseStoreId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_store_controller.get_franchise_store_by_id(franchiseStoreId)
        return render(request, 'indolens_admin/franchiseStores/franchiseStore.html',
                      {"franchise_store": response['franchise_store']})
    else:
        return redirect('login')


def editFranchiseStore(request, franchiseStoreId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            franchise_obj = franchise_store_model.franchise_store_model_from_dict(request.POST)
            response, status_code = franchise_store_controller.edit_franchise_store_by_id(franchise_obj)
            if status_code != 200:
                return render(request, 'indolens_admin/ownStore/editOwnStore.html', {"message": response['message']})
            else:
                return redirect('manage_Franchise_stores')

        else:
            response, status_code = franchise_store_controller.get_franchise_store_by_id(franchiseStoreId)
            return render(request, 'indolens_admin/franchiseStores/editFranchiseStore.html',
                          {"franchise_store": response['franchise_store'], "id": franchiseStoreId})
    else:
        return redirect('login')


def createFranchiseStore(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            franchise_obj = franchise_store_model.franchise_store_model_from_dict(request.POST)
            response, status_code = franchise_store_controller.create_franchise_store(franchise_obj)
            if status_code != 200:
                return render(request, 'indolens_admin/franchiseStores/createFranchiseStore.html',
                              {"message": response['message']})
            else:
                return redirect('manage_Franchise_stores')

        return render(request, 'indolens_admin/franchiseStores/createFranchiseStore.html')
    else:
        return redirect('login')


def enableDisableFranchiseStore(request, franchiseStoreId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response = franchise_store_controller.enable_disable_franchise_store(franchiseStoreId, status)
        return redirect('manage_Franchise_stores')
    else:
        return redirect('login')


# =================================ADMIN SUB ADMIN MANAGEMENT======================================

def manageSubAdmins(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sub_admin_controller.get_all_sub_admin()
        return render(request, 'indolens_admin/subAdmin/manageSubAdmins.html',
                      {"sub_admin_list": response['sub_admins']})
    else:
        return redirect('login')


def createSubAdmin(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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

            sub_admin = sub_admin_model.sub_admin_model_from_dict(request.POST)
            response, status_code = sub_admin_controller.create_sub_admin(sub_admin, file_data)
            url = reverse('view_sub_admin', kwargs={'subAdminId': response['said']})
            return redirect(url)

        else:
            return render(request, 'indolens_admin/subAdmin/createSubAdmin.html')
    else:
        return redirect('login')


def editSubAdmin(request, subAdminId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            sub_admin = sub_admin_model.sub_admin_model_from_dict(request.POST)
            response, status_code = sub_admin_controller.edit_sub_admin(sub_admin)
            return redirect('manageSubAdmins')
        else:
            response, status_code = sub_admin_controller.get_sub_admin_by_id(subAdminId)
            return render(request, 'indolens_admin/subAdmin/editSubAdmin.html',
                          {"sub_admin": response['sub_admin']})
    else:
        return redirect('login')


def viewSubAdmin(request, subAdminId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sub_admin_controller.get_sub_admin_by_id(subAdminId)
        return render(request, 'indolens_admin/subAdmin/viewSubAdmin.html', {"sub_admin": response['sub_admin']})
    else:
        return redirect('login')


def enableDisableSubAdmin(request, subAdminId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response = sub_admin_controller.enable_disable_sub_admin(subAdminId, status)
        return redirect('manage_sub_admins')
    else:
        return redirect('login')


def updateSubAdminDocuments(request, subAdminId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sub_admin_controller.get_sub_admin_by_id(subAdminId)
        return render(request, 'indolens_admin/subAdmin/updateDocuments.html',
                      {"sub_admin": response['sub_admin']})
    else:
        return redirect('login')


def deleteSubAdminDocuments(request, subAdminId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'admin', 'admin_id', subAdminId)
        return JsonResponse(response)
    else:
        return redirect('login')


# =================================ADMIN STORE MANAGERS MANAGEMENT======================================

def manageStoreManagers(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = store_manager_controller.get_all_store_manager()
        available_stores_response, available_stores_status_code = own_store_controller.get_unassigned_active_own_store_for_manager()
        return render(request, 'indolens_admin/storeManagers/manageStoreManagers.html',
                      {"store_managers": response['store_managers'],
                       "available_stores": available_stores_response['available_stores']})
    else:
        return redirect('login')


def createStoreManager(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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

            store_manager = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = store_manager_controller.create_store_manager(store_manager, file_data)
            url = reverse('view_store_manager', kwargs={'storeManagerId': response['mid']})
            return redirect(url)

        else:
            return render(request, 'indolens_admin/storeManagers/createStoreManager.html')
    else:
        return redirect('login')


def viewStoreManager(request, storeManagerId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = store_manager_controller.get_store_manager_by_id(storeManagerId)
        return render(request, 'indolens_admin/storeManagers/viewStoreManager.html',
                      {"store_manager": response['store_manager']})
    else:
        return redirect('login')


def editStoreManager(request, storeManagerId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            store_manager = store_employee_model.store_employee_from_dict(request.POST)
            response = store_manager_controller.update_store_manager(store_manager, file_data)
            url = reverse('view_store_manager', kwargs={'storeManagerId': storeManagerId})
            return redirect(url)

        else:
            response, status_code = store_manager_controller.get_store_manager_by_id(storeManagerId)
            return render(request, 'indolens_admin/storeManagers/editStoreManager.html',
                          {"store_manager": response['store_manager']})
    else:
        return redirect('login')


def updateStoreManagerDocuments(request, storeManagerId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = store_manager_controller.get_store_manager_by_id(storeManagerId)
        return render(request, 'indolens_admin/storeManagers/updateDocuments.html',
                      {"store_manager": response['store_manager']})
    else:
        return redirect('login')


def deleteStoreManagerDocuments(request, storeManagerId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'own_store_employees',
                                                                            'employee_id', storeManagerId)
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableStoreManager(request, storeManagerId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response = store_manager_controller.enable_disable_store_manager(storeManagerId, status)
        return redirect('manage_store_managers')
    else:
        return redirect('login')


# =================================ADMIN FRANCHISE OWNERS MANAGEMENT======================================

def manageFranchiseOwners(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_manager_controller.get_all_franchise_owner()
        return render(request, 'indolens_admin/franchiseOwners/manageFranchiseOwners.html',
                      {"franchise_owners": response['franchise_owners']})
    else:
        return redirect('login')


def createFranchiseOwners(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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

            franchise_owner_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = franchise_manager_controller.create_franchise_owner(franchise_owner_obj, file_data)
            url = reverse('view_franchise_owner', kwargs={'franchiseOwnersId': response['franchiseOwnersId']})
            return redirect(url)

        else:
            return render(request, 'indolens_admin/franchiseOwners/createFranchiseOwner.html')
    else:
        return redirect('login')


def editFranchiseOwners(request, franchiseOwnersId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            franchise_owner = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = franchise_manager_controller.edit_franchise_owner(franchise_owner, file_data)
            url = reverse('view_franchise_owner', kwargs={'franchiseOwnersId': franchiseOwnersId})
            return redirect(url)

        else:
            response, status_code = franchise_manager_controller.get_franchise_owner_by_id(franchiseOwnersId)
            return render(request, 'indolens_admin/franchiseOwners/editFranchiseOwner.html',
                          {"franchise_owner": response['franchise_owner']})
    else:
        return redirect('login')


def enableDisableFranchiseOwner(request, franchiseOwnersId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response = franchise_manager_controller.enable_disable_franchise_owner(franchiseOwnersId, status)
        return redirect('manage_franchise_owners')
    else:
        return redirect('login')


def viewFranchiseOwners(request, franchiseOwnersId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_manager_controller.get_franchise_owner_by_id(franchiseOwnersId)
        return render(request, 'indolens_admin/franchiseOwners/viewFranchiseOwner.html',
                      {"franchise_owner": response['franchise_owner']})
    else:
        return redirect('login')


def updateFranchiseOwnersDocuments(request, franchiseOwnersId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_manager_controller.get_franchise_owner_by_id(franchiseOwnersId)
        return render(request, 'indolens_admin/franchiseOwners/updateDocuments.html',
                      {"franchise_owner": response['franchise_owner']})
    else:
        return redirect('login')


def deleteFranchiseOwnersDocuments(request, franchiseOwnersId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'franchise_store_employees',
                                                                            'employee_id', franchiseOwnersId)
        return JsonResponse(response)
    else:
        return redirect('login')


# =================================ADMIN AREA HEADS MANAGEMENT======================================

def manageAreaHead(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = area_head_controller.get_all_area_head()
        available_stores_response, available_stores_status_code = own_store_controller.get_active_own_stores()
        return render(request, 'indolens_admin/areaHead/manageAreaHead.html',
                      {"area_heads_list": response['area_heads_list'],
                       "available_stores": available_stores_response['available_stores']})
    else:
        return redirect('login')


def createAreaHead(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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

            url = reverse('view_area_head', kwargs={'areaHeadId': response['areaHeadId']})
            return redirect(url)

        else:
            return render(request, 'indolens_admin/areaHead/createAreaHead.html')
    else:
        return redirect('login')


def editAreaHead(request, areaHeadId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            response, status_code = area_head_controller.edit_area_head(area_head, file_data)
            url = reverse('view_area_head', kwargs={'areaHeadId': areaHeadId})
            return redirect(url)

        else:
            response, status_code = area_head_controller.get_area_head_by_id(areaHeadId)
            return render(request, 'indolens_admin/areaHead/editAreaHead.html',
                          {"area_head": response['area_head']})
    else:
        return redirect('login')


def enableDisableAreaHead(request, areaHeadId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        area_head_controller.enable_disable_area_head(areaHeadId, status)
        return redirect('manage_area_head')
    else:
        return redirect('login')


def viewAreaHead(request, areaHeadId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = area_head_controller.get_area_head_by_id(areaHeadId)
        return render(request, 'indolens_admin/areaHead/viewAreaHead.html',
                      {"area_head": response['area_head']})
    else:
        return redirect('login')


def UpdateAreaHeadDocuments(request, areaHeadId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = area_head_controller.get_area_head_by_id(areaHeadId)
        return render(request, 'indolens_admin/areaHead/updateDocuments.html',
                      {"area_head": response['area_head']})
    else:
        return redirect('login')


def deleteAreaHeadDocuments(request, subAdminId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'area_head', 'area_head_id', subAdminId)
        return JsonResponse(response)
    else:
        return redirect('login')


# =================================ADMIN MARKETING HEADS MANAGEMENT======================================

def manageMarketingHead(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = marketing_head_controller.get_all_marketing_head()
        return render(request, 'indolens_admin/marketingHeads/manageMarketingHead.html',
                      {"marketing_heads_list": response['marketing_heads_list']})
    else:
        return redirect('login')


def createMarketingHead(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            marketing_head_obj = marketing_head_model.marketing_head_model_from_dict(request.POST)
            response, status_code = marketing_head_controller.create_marketing_head(marketing_head_obj, file_data)
            url = reverse('view_marketing_head', kwargs={'marketingHeadId': response['marketingHeadId']})
            return redirect(url)
        else:
            return render(request, 'indolens_admin/marketingHeads/createMarketingHead.html')
    else:
        return redirect('login')


def editMarketingHead(request, marketingHeadId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            marketing_head_obj = marketing_head_model.marketing_head_model_from_dict(request.POST)
            response, status_code = marketing_head_controller.edit_marketing_head(marketing_head_obj, file_data)

            url = reverse('view_marketing_head', kwargs={'marketingHeadId': marketingHeadId})
            return redirect(url)
        else:
            response, status_code = marketing_head_controller.get_marketing_head_by_id(marketingHeadId)
            return render(request, 'indolens_admin/marketingHeads/editMarketingHead.html',
                          {"marketing_head": response['marketing_head']})
    else:
        return redirect('login')


def viewMarketingHead(request, marketingHeadId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = marketing_head_controller.get_marketing_head_by_id(marketingHeadId)
        return render(request, 'indolens_admin/marketingHeads/viewMarketingHead.html',
                      {"marketing_head": response['marketing_head']})
    else:
        return redirect('login')


def updateMarketingHeadDocuments(request, marketingHeadId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = marketing_head_controller.get_marketing_head_by_id(marketingHeadId)

        return render(request, 'indolens_admin/marketingHeads/updateDocuments.html',
                      {"marketing_head": response['marketing_head']})
    else:
        return redirect('login')


def enableDisableMarketingHead(request, marketingHeadId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        marketing_head_controller.enable_disable_marketing_head(marketingHeadId, status)
        return redirect('manage_marketing_head')
    else:
        return redirect('login')


# =================================ADMIN OWN STORE OPTIMETRY MANAGEMENT======================================


def manageOptimetry(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = optimetry_controller.get_all_optimetry()

        available_stores_response, available_stores_status_code = own_store_controller.get_active_own_stores()
        return render(request, 'indolens_admin/optimetry/manageOptimetry.html',
                      {"optimetry_list": response['optimetry_list'],
                       "available_stores": available_stores_response['available_stores']})
    else:
        return redirect('login')


def createOptimetry(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic',
                'document1': 'documents',
                'document2': 'documents',
                'certificates': 'certificates',
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            optimetry_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = optimetry_controller.create_optimetry(optimetry_obj, file_data)

            url = reverse('view_optimetry', kwargs={'ownOptimetryId': response['empid']})
            return redirect(url)
        else:
            return render(request, 'indolens_admin/optimetry/createOptimetry.html')
    else:
        return redirect('login')


def editOptimetry(request, ownOptimetryId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            optimetry_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = optimetry_controller.update_optimetry(optimetry_obj, file_data)
            url = reverse('view_optimetry', kwargs={'ownOptimetryId': ownOptimetryId})
            return redirect(url)
        else:
            response, status_code = optimetry_controller.get_optimetry_by_id(ownOptimetryId)
            return render(request, 'indolens_admin/optimetry/editOptimetry.html', {"optimetry": response['optimetry']})
    else:
        return redirect('login')


def viewOptimetry(request, ownOptimetryId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = optimetry_controller.get_optimetry_by_id(ownOptimetryId)
        return render(request, 'indolens_admin/optimetry/viewOptimetry.html',
                      {"optimetry": response['optimetry']})
    else:
        return redirect('login')


def updateOptimetryDocuments(request, ownOptimetryId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = optimetry_controller.get_optimetry_by_id(ownOptimetryId)

        return render(request, 'indolens_admin/optimetry/updateDocuments.html',
                      {"optimetry": response['optimetry']})
    else:
        return redirect('login')


def deleteOptimetryDocuments(request, ownOptimetryId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'own_store_employees',
                                                                            'employee_id', ownOptimetryId)
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableOptimetry(request, ownOptimetryId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        optimetry_controller.enable_disable_optimetry(ownOptimetryId, status)
        return redirect('manage_store_optimetry')
    else:
        return redirect('login')


# =================================ADMIN OWN STORE OPTIMETRY MANAGEMENT======================================


# =================================ADMIN FRANCHISE STORE OPTIMETRY MANAGEMENT======================================


def manageFranchiseOptimetry(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = optimetry_controller.get_all_franchise_optimetry()

        return render(request, 'indolens_admin/franchiseOptimetry/manageOptimetry.html',
                      {"optimetry_list": response['optimetry_list']})
    else:
        return redirect('login')


def createFranchiseOptimetry(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic',
                'document1': 'documents',
                'document2': 'documents',
                'certificates': 'certificates',
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            optimetry_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = optimetry_controller.create_franchise_optimetry(optimetry_obj, file_data)
            url = reverse('view_franchise_optimetry', kwargs={'franchiseOptimetryId': response['opid']})
            return redirect(url)
        else:
            return render(request, 'indolens_admin/franchiseOptimetry/createOptimetry.html')
    return redirect('login')


def editFranchiseOptimetry(request, franchiseOptimetryId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == "POST":
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            optimetry_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = optimetry_controller.edit_franchise_optimetry(optimetry_obj, file_data)
            url = reverse('view_franchise_optimetry', kwargs={'franchiseOptimetryId': franchiseOptimetryId})
            return redirect(url)
        else:
            response, status_code = optimetry_controller.get_franchise_optimetry_by_id(franchiseOptimetryId)
            return render(request, 'indolens_admin/franchiseOptimetry/editOptimetry.html',
                          {"optimetry": response['optimetry']})
    else:
        return redirect('login')


def viewFranchiseOptimetry(request, franchiseOptimetryId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = optimetry_controller.get_franchise_optimetry_by_id(franchiseOptimetryId)
        return render(request, 'indolens_admin/franchiseOptimetry/viewOptimetry.html',
                      {"optimetry": response['optimetry']})
    else:
        return redirect('login')


def updateFranchiseOptimetryDocuments(request, franchiseOptimetryId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = optimetry_controller.get_franchise_optimetry_by_id(franchiseOptimetryId)
        return render(request, 'indolens_admin/franchiseOptimetry/updateDocuments.html',
                      {"optimetry": response['optimetry']})
    else:
        return redirect('login')


def deleteFranchiseOptimetryDocuments(request, franchiseOptimetryId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'franchise_store_employees',
                                                                            'employee_id', franchiseOptimetryId)
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableFranchiseOptimetry(request, franchiseOptimetryId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        optimetry_controller.enable_disable_franchise_optimetry(franchiseOptimetryId, status)
        return redirect('manage_franchise_optimetry')
    else:
        return redirect('login')


# =================================ADMIN FRANCHISE STORE OPTIMETRY MANAGEMENT======================================
# =================================ADMIN OWN STORE SALES EXECUTIVE MANAGEMENT======================================


def manageSaleExecutives(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sales_executives_controller.get_all_own_sales_executive()
        return render(request, 'indolens_admin/salesExecutive/manageSaleExecutives.html',
                      {"sales_executive_list": response['sales_executive_list']})
    return redirect('login')


def createSaleExecutives(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            sales_executives_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = sales_executives_controller.create_own_sales_executives(sales_executives_obj,
                                                                                            file_data)
            url = reverse('view_sales_executives', kwargs={'ownSaleExecutivesId': response['seId']})
            return redirect(url)
        else:
            return render(request, 'indolens_admin/salesExecutive/createSaleExecutives.html')
    return redirect('login')


def editSaleExecutives(request, ownSaleExecutivesId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            sales_executives_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = sales_executives_controller.update_own_sales_executives(sales_executives_obj,
                                                                                            file_data)
            url = reverse('view_sales_executives', kwargs={'ownSaleExecutivesId': ownSaleExecutivesId})
            return redirect(url)
        else:
            response, status_code = sales_executives_controller.get_own_sales_executive_by_id(ownSaleExecutivesId)

            return render(request, 'indolens_admin/salesExecutive/editSaleExecutives.html',
                          {"sales_executive": response['sales_executive']})
    else:
        return redirect('login')


def viewSaleExecutives(request, ownSaleExecutivesId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sales_executives_controller.get_own_sales_executive_by_id(ownSaleExecutivesId)
        return render(request, 'indolens_admin/salesExecutive/viewSaleExecutives.html',
                      {"sales_executive": response['sales_executive']})
    else:
        return redirect('login')


def updateSaleExecutivesDocuments(request, ownSaleExecutivesId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sales_executives_controller.get_own_sales_executive_by_id(ownSaleExecutivesId)
        return render(request, 'indolens_admin/salesExecutive/updateDocuments.html',
                      {"sales_executive": response['sales_executive']})
    else:
        return redirect('login')


def deleteSaleExecutivesDocuments(request, ownSaleExecutivesId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'own_store_employees',
                                                                            'employee_id', ownSaleExecutivesId)
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableSaleExecutives(request, ownSaleExecutivesId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        sales_executives_controller.enable_disable_sales_executive(ownSaleExecutivesId, status)
        return redirect('manage_store_sales_executives')
    else:
        return redirect('login')


# =================================ADMIN OWN STORE SALES EXECUTIVE MANAGEMENT======================================
# =================================ADMIN FRANCHISE STORE SALES EXECUTIVE MANAGEMENT====================================


def manageFranchiseSaleExecutives(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sales_executives_controller.get_all_franchise_sales_executive()
        return render(request, 'indolens_admin/franchiseSalesExecutive/manageSaleExecutives.html',
                      {"franchise_sales_executive_list": response['franchise_sales_executive_list']})
    else:
        return redirect('login')


def createFranchiseSaleExecutives(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            sales_executives_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = sales_executives_controller.create_franchise_sales_executives(sales_executives_obj,
                                                                                                  file_data)
            url = reverse('view_franchise_sales_executives', kwargs={'franchiseSaleExecutivesId': response['foid']})
            return redirect(url)
        else:
            return render(request, 'indolens_admin/franchiseSalesExecutive/createSaleExecutives.html')
    return redirect('login')


def editFranchiseSaleExecutives(request, franchiseSaleExecutivesId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            sales_executives_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = sales_executives_controller.update_franchise_sales_executives(sales_executives_obj,
                                                                                                  file_data)
            url = reverse('view_franchise_sales_executives',
                          kwargs={'franchiseSaleExecutivesId': franchiseSaleExecutivesId})
            return redirect(url)
        else:
            response, status_code = sales_executives_controller.get_franchise_sales_executive_by_id(
                franchiseSaleExecutivesId)
            return render(request, 'indolens_admin/franchiseSalesExecutive/editSaleExecutives.html',
                          {"franchise_sales_executive": response['franchise_sales_executive']})
    else:
        return redirect('login')


def viewFranchiseSaleExecutives(request, franchiseSaleExecutivesId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sales_executives_controller.get_franchise_sales_executive_by_id(
            franchiseSaleExecutivesId)
        return render(request, 'indolens_admin/franchiseSalesExecutive/viewSaleExecutives.html',
                      {"franchise_sales_executive": response['franchise_sales_executive']})
    else:
        return redirect('login')


def updateFranchiseSaleExecutivesDocuments(request, franchiseSaleExecutivesId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sales_executives_controller.get_franchise_sales_executive_by_id(
            franchiseSaleExecutivesId)
        return render(request, 'indolens_admin/franchiseSalesExecutive/updateDocuments.html',
                      {"franchise_sales_executive": response['franchise_sales_executive']})
    else:
        return redirect('login')


def deleteFranchiseSaleExecutivesDocuments(request, franchiseSaleExecutivesId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'franchise_store_employees',
                                                                            'employee_id', franchiseSaleExecutivesId)
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableFranchiseSaleExecutives(request, franchiseSaleExecutivesId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        sales_executives_controller.enable_disable_franchise_sales_executive(franchiseSaleExecutivesId, status)
        return redirect('manage_franchise_sales_executives')
    else:
        return redirect('login')


# =================================ADMIN OWN STORE SALES EXECUTIVE MANAGEMENT======================================

# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageAccountant(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = accountant_controller.get_all_accountant()
        return render(request, 'indolens_admin/accountant/manageAccountant.html',
                      {"accountant_list": response['accountant_list']})
    else:
        return redirect('login')


def createAccountant(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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

            accountant_obj = accountant_model.accountant_model_from_dict(request.POST)
            response, status_code = accountant_controller.create_accountant(accountant_obj, file_data)
            url = reverse('view_accountant', kwargs={'accountantId': response['aid']})
            return redirect(url)

        else:
            return render(request, 'indolens_admin/accountant/createAccountant.html')
    return redirect('login')


def editAccountant(request, accountantId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            accountant_obj = accountant_model.accountant_model_from_dict(request.POST)
            response, status_code = accountant_controller.edit_accountant(accountant_obj, file_data)

            url = reverse('view_accountant', kwargs={'accountantId': accountantId})
            return redirect(url)
        else:
            response, status_code = accountant_controller.get_accountant_by_id(accountantId)

            return render(request, 'indolens_admin/accountant/editAccountant.html',
                          {"accountant": response['accountant']})
    else:
        return redirect('login')


def viewAccountant(request, accountantId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = accountant_controller.get_accountant_by_id(accountantId)
        return render(request, 'indolens_admin/accountant/viewAccountant.html',
                      {"accountant": response['accountant']})
    else:
        return redirect('login')


def updateAccountantDocuments(request, accountantId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = accountant_controller.get_accountant_by_id(accountantId)
        return render(request, 'indolens_admin/accountant/updateDocuments.html',
                      {"accountant": response['accountant']})
    else:
        return redirect('login')


def deleteAccountantDocuments(request, accountantId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'accountant', 'accountant_id', accountantId)
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableAccountant(request, accountantId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        accountant_controller.enable_disable_accountant(accountantId, status)
        return redirect('manage_accountant')
    else:
        return redirect('login')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageLabTechnician(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = lab_technician_controller.get_all_lab_technician()
        return render(request, 'indolens_admin/labTechnician/manageLabTechnician.html',
                      {"lab_technician_list": response['lab_technician_list']})
    else:
        return redirect('login')


def createLabTechnician(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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

            lab_tech_obj = lab_technician_model.lab_technician_model_from_dict(request.POST)
            response, status_code = lab_technician_controller.create_lab_technician(lab_tech_obj, file_data)
            url = reverse('view_lab_technician', kwargs={'labTechnicianId': response['ltid']})
            return redirect(url)
        else:
            return render(request, 'indolens_admin/labTechnician/createLabTechnician.html')
    else:
        return redirect('login')


def editLabTechnician(request, labTechnicianId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            lab_tech_obj = lab_technician_model.lab_technician_model_from_dict(request.POST)
            response, status_code = lab_technician_controller.edit_lab_technician(lab_tech_obj,
                                                                                  file_data)
            url = reverse('view_lab_technician', kwargs={'labTechnicianId': labTechnicianId})
            return redirect(url)
        else:
            response, status_code = lab_technician_controller.get_lab_technician_by_id(labTechnicianId)

            return render(request, 'indolens_admin/labTechnician/editLabTechnician.html',
                          {"lab_technician": response['lab_technician']})
    else:
        return redirect('login')


def viewLabTechnician(request, labTechnicianId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = lab_technician_controller.get_lab_technician_by_id(labTechnicianId)
        return render(request, 'indolens_admin/labTechnician/viewLabTechnician.html',
                      {"lab_technician": response['lab_technician']})
    else:
        return redirect('login')


def updateLabTechnicianDocuments(request, labTechnicianId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = lab_technician_controller.get_lab_technician_by_id(labTechnicianId)
        return render(request, 'indolens_admin/labTechnician/updateDocuments.html',
                      {"lab_technician": response['lab_technician']})
    else:
        return redirect('login')


def deleteLabTechnicianDocuments(request, labTechnicianId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'labTechnicianId', 'labTechnicianId',
                                                                            labTechnicianId)
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableLabTechnician(request, labTechnicianId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        lab_technician_controller.enable_disable_lab_technician(labTechnicianId, status)
        return redirect('manage_lab_technician')
    else:
        return redirect('login')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageOtherEmployees(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = other_employee_controller.get_all_other_emp()
        return render(request, 'indolens_admin/otherEmployees/manageOtherEmployees.html',
                      {"other_employee_list": response['other_emp_list']})
    else:
        return redirect('login')


def createOtherEmployees(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            other_emp_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = other_employee_controller.create_other_employee(other_emp_obj, file_data)
            url = reverse('view_other_employees', kwargs={'ownEmployeeId': response['empid']})
            return redirect(url)
        else:
            return render(request, 'indolens_admin/otherEmployees/createOtherEmployees.html', )
    else:
        return redirect('login')


def editOtherEmployees(request, ownEmployeeId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            other_emp_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = other_employee_controller.update_other_employee(other_emp_obj, file_data)
            url = reverse('view_other_employees', kwargs={'ownEmployeeId': ownEmployeeId})
            return redirect(url)

        else:
            response, status_code = other_employee_controller.get_other_emp_by_id(ownEmployeeId)

            return render(request, 'indolens_admin/otherEmployees/editOtherEmployees.html',
                          {"other_employee": response['other_employee']})
    else:
        return redirect('login')


def viewOtherEmployees(request, ownEmployeeId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = other_employee_controller.get_other_emp_by_id(ownEmployeeId)
        return render(request, 'indolens_admin/otherEmployees/viewOtherEmployees.html',
                      {"other_employee": response['other_employee']})
    else:
        return redirect('login')


def updateOtherEmployeesDocuments(request, ownEmployeeId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = other_employee_controller.get_other_emp_by_id(ownEmployeeId)
        return render(request, 'indolens_admin/otherEmployees/updateDocuments.html',
                      {"other_employee": response['other_employee']})
    else:
        return redirect('login')


def deleteOtherEmployeesDocuments(request, ownEmployeeId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'own_store_employees',
                                                                            'employee_id', ownEmployeeId)
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableOtherEmployees(request, ownEmployeeId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        other_employee_controller.enable_disable_other_employees(ownEmployeeId, status)
        return redirect('manage_store_other_employees')
    else:
        return redirect('login')


# FRANCHISE OTHER EMPLOYEES
def manageFranchiseOtherEmployees(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = other_employee_controller.get_all_franchise_other_emp()
        return render(request, 'indolens_admin/franchiseOtherEmployees/manageOtherEmployees.html',
                      {"other_employee_list": response['other_emp_list']})
    else:
        return redirect('login')


def createFranchiseOtherEmployees(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            other_emp_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = other_employee_controller.create_franchise_other_employee(other_emp_obj, file_data)
            url = reverse('view_franchise_other_employees', kwargs={'franchiseEmployeeId': response['empid']})
            return redirect(url)
        else:
            return render(request, 'indolens_admin/franchiseOtherEmployees/createOtherEmployees.html', )
    else:
        return redirect('login')


def editFranchiseOtherEmployees(request, franchiseEmployeeId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'profilePic': 'profile_pic'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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
            other_emp_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = other_employee_controller.update_franchise_other_employee(other_emp_obj, file_data)
            url = reverse('view_franchise_other_employees', kwargs={'franchiseEmployeeId': franchiseEmployeeId})
            return redirect(url)
        else:
            response, status_code = other_employee_controller.get_franchise_other_emp_by_id(franchiseEmployeeId)
            return render(request, 'indolens_admin/franchiseOtherEmployees/editOtherEmployees.html',
                          {"other_employee": response['other_employee']})
    else:
        return redirect('login')


def viewFranchiseOtherEmployees(request, franchiseEmployeeId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = other_employee_controller.get_franchise_other_emp_by_id(franchiseEmployeeId)
        return render(request, 'indolens_admin/franchiseOtherEmployees/viewOtherEmployees.html',
                      {"other_employee": response['other_employee']})
    else:
        return redirect('login')


def updateFranchiseOtherEmployeesDocuments(request, franchiseEmployeeId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = other_employee_controller.get_franchise_other_emp_by_id(franchiseEmployeeId)
        return render(request, 'indolens_admin/franchiseOtherEmployees/updateDocuments.html',
                      {"other_employee": response['other_employee']})
    else:
        return redirect('login')


def deleteFranchiseOtherEmployeesDocuments(request, franchiseSaleExecutivesId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'franchise_store_employees',
                                                                            'employee_id', franchiseSaleExecutivesId)
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableFranchiseOtherEmployees(request, franchiseEmployeeId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        other_employee_controller.enable_disable_franchise_other_employees(franchiseEmployeeId, status)
        return redirect('manage_franchise_other_employees')
    else:
        return redirect('login')


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
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = lab_controller.get_all_labs()

        return render(request, 'indolens_admin/labs/manageLabs.html', {"lab_list": response['lab_list']})
    else:
        return redirect('login')


def createLab(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            lab_obj = lab_model.lab_model_from_dict(request.POST)
            lab_controller.create_lab(lab_obj)
        return render(request, 'indolens_admin/labs/createLab.html')
    else:
        return redirect('login')


def editLab(request, labId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            lab_obj = lab_model.lab_model_from_dict(request.POST)
            lab_controller.edit_lab_by_id(lab_obj)
            return redirect('manage_labs')
        else:
            response, status_code = lab_controller.get_lab_by_id(labId)
            return render(request, 'indolens_admin/labs/editLab.html', {"lab_data": response['lab_data']})
    return redirect('login')


def viewLab(request, labId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = lab_controller.get_lab_by_id(labId)
        return render(request, 'indolens_admin/labs/viewLab.html',
                      {"lab_data": response['lab_data']})
    else:
        return redirect('login')


def enableDisableLab(request, labId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        lab_controller.enable_disable_lab(labId, status)
        return redirect('manage_labs')
    else:
        return redirect('login')


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
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:

        response, status_code = master_category_controller.get_all_central_inventory_category()

        return render(request, 'indolens_admin/masters/manageMastersCategory.html',
                      {"product_category": response['product_category']})
    else:
        return redirect('login')


def addProductCategory(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            product_cat_obj = product_category_model.product_category_model_from_dict(request.POST)
            master_category_controller.add_product_category(product_cat_obj)
            return redirect('manage_central_inventory_category')
        else:
            return render(request, 'indolens_admin/masters/addProductCategory.html')
    else:
        return redirect('login')


def enableDisableProductCategory(request, categoryId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        master_category_controller.enable_disable_product_category(categoryId, status)
        return redirect('manage_central_inventory_category')
    else:
        return redirect('login')


def manageMastersBrands(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:

        response, status_code = master_brand_controller.get_all_central_inventory_brand()

        return render(request, 'indolens_admin/masters/manageMastersBrands.html',
                      {"product_brand": response["product_brand"]})
    else:
        return redirect('login')


def addMastersBrands(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':

            master_brand_obj = master_brand_model.master_brand_model_from_dict(request.POST)
            resp = master_brand_controller.add_product_brand(master_brand_obj)

            return redirect('manage_central_inventory_brands')
        else:
            return render(request, 'indolens_admin/masters/addMastersBrand.html')
    else:
        return redirect('login')


def enableDisableMastersBrands(request, brandId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        master_brand_controller.enable_disable_product_brand(brandId, status)
        return redirect('manage_central_inventory_brands')
    else:
        return redirect('login')


def manageMastersShapes(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:

        response, status_code = master_shape_controller.get_all_central_inventory_shapes()
        return render(request, 'indolens_admin/masters/manageMastersShapes.html',
                      {"product_shape": response["product_shape"]})
    else:
        return redirect('login')


def addMastersShapes(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':

            master_shape_obj = master_shape_model.master_shape_model_from_dict(request.POST)
            resp = master_shape_controller.add_frame_shape(master_shape_obj)

            return redirect('manage_central_inventory_shapes')
        else:
            return render(request, 'indolens_admin/masters/addMastersShapes.html')
    else:
        return redirect('login')


def enableDisableMastersShapes(request, shapeId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        master_shape_controller.enable_disable_frame_shape(shapeId, status)
        return redirect('manage_central_inventory_shapes')
    else:
        return redirect('login')


def manageMastersFrameType(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = master_frame_type_controller.get_all_central_inventory_frame_types()
        return render(request, 'indolens_admin/masters/manageMastersFrameType.html',
                      {"frame_type": response["frame_type"]})
    else:
        return redirect('login')


def addMastersFrameType(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':

            frame_type_obj = master_frame_type_model.master_frame_type_model_from_dict(request.POST)
            resp = master_frame_type_controller.add_frame_type(frame_type_obj)
            return redirect('manage_central_inventory_frame_types')
        else:
            return render(request, 'indolens_admin/masters/addMastersFrameType.html')
    else:
        return redirect('login')


def enableDisableMastersFrameType(request, frametypeId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        master_frame_type_controller.enable_disable_frame_type(frametypeId, status)
        return redirect('manage_central_inventory_frame_types')
    else:
        return redirect('login')


def manageMastersColor(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = master_color_controller.get_all_central_inventory_color()
        return render(request, 'indolens_admin/masters/manageMastersColor.html',
                      {"frame_color": response["frame_color"]})
    else:
        return redirect('login')


def addMastersColor(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':

            color_obj = master_color_model.master_color_model_from_dict(request.POST)
            resp = master_color_controller.add_master_color(color_obj)
            return redirect('manage_central_inventory_color')
        else:
            return render(request, 'indolens_admin/masters/addMastersColor.html')
    else:
        return redirect('login')


def enableDisableMastersColor(request, colorId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        master_color_controller.enable_disable_master_color(colorId, status)
        return redirect('manage_central_inventory_color')
    else:
        return redirect('login')


def manageMastersMaterials(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = master_material_controller.get_all_central_inventory_materials()
        return render(request, 'indolens_admin/masters/manageMastersMaterials.html',
                      {"frame_material": response["frame_material"]})
    else:
        return redirect('login')


def addMastersMaterials(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':

            material_obj = master_material_model.master_material_model_from_dict(request.POST)
            resp = master_material_controller.add_master_material(material_obj)
            return redirect('manage_central_inventory_materials')
        else:
            return render(request, 'indolens_admin/masters/addMastersMaterials.html')
    else:
        return redirect('login')


def enableDisableMastersMaterials(request, materialId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        master_material_controller.enable_disable_master_material(materialId, status)
        return redirect('manage_central_inventory_materials')
    else:
        return redirect('login')


def manageMastersUnits(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = master_units_controller.get_all_units()

        return render(request, 'indolens_admin/masters/manageMastersUnits.html',
                      {"units_list": response['units_list']})
    else:
        return redirect('login')


def addMastersUnits(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            data = request.POST
            resp = master_units_controller.add_masters_units(data)

        return redirect('manage_central_inventory_units')
    else:
        return redirect('login')


def enableDisableMastersUnits(request, unitId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        master_units_controller.enable_disable_master_units(unitId, status)
        return redirect('manage_central_inventory_units')
    else:
        return redirect('login')


# =================================ADMIN STORE MANAGEMENT======================================


def manageCentralInventoryProducts(request):
    response, status_code = central_inventory_controller.get_all_central_inventory_products()
    return render(request, 'indolens_admin/centralInventory/manageCentralInventoryProducts.html',
                  {"product_list": response['product_list']})


def centralInventoryAddProducts(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            form_data = {}
            file_data = {}
            file_label_mapping = {
                'productImages': 'products'
            }

            for file_key, file_objs in request.FILES.lists():
                label = file_label_mapping.get(file_key, 'unknown')
                subdirectory = f"{label}/"
                file_list = []

                for index, file_obj in enumerate(file_objs):
                    file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
                    form_data_key = f"prod_img"
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
            product_obj = central_inventory_products_model.inventory_add_products_from_dict(request.POST)
            response, status_code = central_inventory_controller.add_central_inventory_products(product_obj, file_data)
            return redirect('manage_central_inventory_products')
        else:
            response, status_code = central_inventory_controller.get_all_active_types()
            return render(request, 'indolens_admin/centralInventory/centralInventoryAddProducts.html', response)

    else:
        return redirect('login')


def manageCentralInventoryOutOfStock(request):
    response, status_code = central_inventory_controller.get_all_out_of_stock_central_inventory_products(15)
    return render(request, 'indolens_admin/centralInventory/manageCentralInventoryOutOfStock.html',
                  {"stocks_list": response['stocks_list']})


def manageMoveStocks(request):
    response, status_code = own_store_controller.get_all_own_stores()
    return render(request, 'indolens_admin/centralInventory/manageMoveStocks.html',
                  {"own_store_list": response['own_stores']})


def manageMoveAStock(request):
    return render(request, 'indolens_admin/centralInventory/manageMoveAStock.html')


# =================================ADMIN STORE MANAGEMENT======================================


def viewAllStockRequests(request):
    response, status_code = central_inventory_controller.get_all_stock_requests('%')
    return render(request, 'indolens_admin/stockRequests/viewAllStockRequests.html',
                  {"stocks_request_list": response['stocks_request_list']})


def viewPendingStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewPendingStockRequests.html')


def viewCompletedStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewCompletedStockRequests.html')


def viewRejectedStockRequests(request):
    return render(request, 'indolens_admin/stockRequests/viewrejectedStockRequests.html')


def assignManagerOwnStore(request):
    if request.method == 'POST':
        response, status_code = store_manager_controller.assignStore(request.POST['emp_id'], request.POST['store_id'])
        return redirect('manage_store_managers')


def unAssignManagerOwnStore(request, empId, storeId):
    response, status_code = store_manager_controller.unAssignStore(empId, storeId)
    return redirect('manage_store_managers')


def assignOptimetryOwnStore(request):
    if request.method == 'POST':
        response, status_code = store_manager_controller.assignStore(request.POST['emp_id'], request.POST['store_id'])
        return redirect('manage_store_optimetry')


def unAssignOptimetryOwnStore(request, empId, storeId):
    response, status_code = store_manager_controller.unAssignStore(empId, storeId)
    return redirect('manage_store_optimetry')


def assignAreaHeadOwnStore(request):
    if request.method == 'POST':
        response, status_code = store_manager_controller.assignStore(request.POST['emp_id'], request.POST['store_id'])
        return redirect('manage_area_head')


def unAssignAreaHeadOwnStore(request, empId, storeId):
    response, status_code = store_manager_controller.unAssignStore(empId, storeId)
    return redirect('manage_area_head')
