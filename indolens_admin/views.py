import time

from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from rest_framework.reverse import reverse

from indolens_admin.admin_controllers import admin_auth_controller, own_store_controller, franchise_store_controller, \
    sub_admin_controller, store_manager_controller, franchise_owner_controller, area_head_controller, \
    marketing_head_controller, sales_executives_controller, accountant_controller, lab_technician_controller, \
    lab_controller, other_employee_controller
from indolens_admin.admin_models.admin_req_model import admin_auth_model, own_store_model, franchise_store_model, \
    sub_admin_model, store_manager_model, franchise_owner_model, area_head_model, marketing_head_model, \
    sales_executives_model, accountant_model, lab_technician_model, lab_model, other_employee_model
from indolens_admin.admin_models.admin_req_model.files_model import FileData


# =================================ADMIN START======================================
def index(request):
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


def viewOwnStore(request, sid):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = own_store_controller.get_own_store_by_id(sid)
        return render(request, 'indolens_admin/ownStore/ownStore.html', {"store_data": response['own_stores']})
    else:
        return redirect('login')


def editOwnStore(request, sid):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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


def enableDisableOwnStore(request, sid, status):
    response = own_store_controller.enable_disable_own_store(sid, status)
    print(response)
    return redirect('manage_own_stores')


def manageFranchiseStores(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_store_controller.get_all_franchise_stores()
        return render(request, 'indolens_admin/franchiseStores/manageFranchiseStores.html',
                      {"franchise_store_list": response['franchise_store']})
    else:
        return redirect('login')


def viewFranchiseStore(request, fid):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_store_controller.get_franchise_store_by_id(fid)
        return render(request, 'indolens_admin/franchiseStores/franchiseStore.html',
                      {"franchise_store": response['franchise_store']})
    else:
        return redirect('login')


def editFranchiseStore(request, fid):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
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


def enableDisableFranchiseStore(request, fid, status):
    response = franchise_store_controller.enable_disable_franchise_store(fid, status)
    print(response)
    return redirect('manage_Franchise_stores')


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
            response = sub_admin_controller.create_sub_admin(sub_admin, file_data)
            url = reverse('view_sub_admin', kwargs={'said': response['said']})
            return redirect(url)

        else:
            return render(request, 'indolens_admin/subAdmin/createSubAdmin.html')
    else:
        return redirect('login')


def editSubAdmin(request, said):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            sub_admin = sub_admin_model.sub_admin_model_from_dict(request.POST)
            response, status_code = sub_admin_controller.edit_sub_admin(sub_admin)
            return redirect('manageSubAdmins')
        else:
            response, status_code = sub_admin_controller.get_sub_admin_by_id(said)
            return render(request, 'indolens_admin/subAdmin/editSubAdmin.html', {"sub_admin": response['sub_admin']})

    else:
        return redirect('login')


def viewSubAdmin(request, said):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sub_admin_controller.get_sub_admin_by_id(said)
        return render(request, 'indolens_admin/subAdmin/viewSubAdmin.html', {"sub_admin": response['sub_admin']})
    else:
        return redirect('login')


def enableDisableSubAdmin(request, said, status):
    response = sub_admin_controller.enable_disable_sub_admin(said, status)
    print(response)
    return redirect('manage_sub_admins')


# =================================ADMIN STORE MANAGERS MANAGEMENT======================================

def manageStoreManagers(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = store_manager_controller.get_all_store_manager()
        return render(request, 'indolens_admin/storeManagers/manageStoreManagers.html',
                      {"store_managers": response['store_managers']})
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

            store_manager = store_manager_model.store_manager_model_from_dict(request.POST)
            response, status_code = store_manager_controller.create_store_manager(store_manager, file_data)
            url = reverse('view_store_manager', kwargs={'mid': response['mid']})
            return redirect(url)

        else:
            return render(request, 'indolens_admin/storeManagers/createStoreManager.html')
    else:
        return redirect('login')


def viewStoreManager(request, mid):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = store_manager_controller.get_store_manager_by_id(mid)
        return render(request, 'indolens_admin/storeManagers/viewStoreManager.html',
                      {"store_manager": response['store_manager']})
    else:
        return redirect('login')


def editStoreManager(request, mid):
    if request.method == 'POST':
        print(request.POST)
        store_manager = store_manager_model.store_manager_model_from_dict(request.POST)
        print(store_manager)

    response, status_code = store_manager_controller.get_store_manager_by_id(mid)
    return render(request, 'indolens_admin/storeManagers/editStoreManager.html',
                  {"store_manager": response['store_manager']})


def enableDisableStoreManager(request, mid, status):
    response = store_manager_controller.enable_disable_store_manager(mid, status)
    print(response)
    return redirect('manage_store_managers')


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

        franchise_owner_obj = franchise_owner_model.franchise_owner_model_from_dict(request.POST)
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
            label = file_label_mapping.get(file_key, 'unknown')
            subdirectory = f"{label}/"

            for file_obj in file_objs:
                file_name = f"{subdirectory}{label}_{int(time.time())}_{str(file_obj)}"
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


def enableDisableFranchiseOwner(request, foid, status):
    response = franchise_owner_controller.enable_disable_franchise_owner(foid, status)
    print(response)
    return redirect('manage_franchise_owners')


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

        url = reverse('view_area_head', kwargs={'ahid': response['ahid']})
        return redirect(url)

    else:
        return render(request, 'indolens_admin/areaHead/createAreaHead.html')


def editAreaHead(request):
    return render(request, 'indolens_admin/areaHead/editAreaHead.html')


def enableDisableAreaHead(request, ahid, status):
    area_head_controller.enable_disable_area_head(ahid, status)
    return redirect('manage_area_head')


def viewAreaHead(request, ahid):
    response, status_code = area_head_controller.get_area_head_by_id(ahid)
    return render(request, 'indolens_admin/areaHead/viewAreaHead.html',
                  {"area_head": response['area_head']})


# =================================ADMIN MARKETING HEADS MANAGEMENT======================================

def manageMarketingHead(request):
    response, status_code = marketing_head_controller.get_all_marketing_head()
    return render(request, 'indolens_admin/marketingHeads/manageMarketingHead.html',
                  {"marketing_heads_list": response['marketing_heads_list']})


def createMarketingHead(request):
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
        resp = marketing_head_controller.create_marketing_head(marketing_head_obj, file_data)
        return redirect('manage_marketing_head')
    else:
        return render(request, 'indolens_admin/marketingHeads/createMarketingHead.html')


def editMarketingHead(request, mhid):
    response, status_code = marketing_head_controller.get_marketing_head_by_id(mhid)
    return render(request, 'indolens_admin/marketingHeads/editMarketingHead.html',
                  {"marketing_head": response['marketing_head']})


def viewMarketingHead(request, mhid):
    response, status_code = marketing_head_controller.get_marketing_head_by_id(mhid)
    print(response)
    return render(request, 'indolens_admin/marketingHeads/viewMarketingHead.html',
                  {"marketing_head": response['marketing_head']})


def enableDisableMarketingHead(request, mhid, status):
    marketing_head_controller.enable_disable_marketing_head(mhid, status)
    return redirect('manage_marketing_head')


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
    response, status_code = sales_executives_controller.get_all_sales_executive()
    print(response)
    return render(request, 'indolens_admin/salesExecutive/manageSaleExecutives.html',
                  {"sales_executive_list": response['sales_executive_list']})


def createSaleExecutives(request):
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

        print(form_data)
        file_data = FileData(form_data)
        sales_executives_obj = sales_executives_model.sales_executives_model_from_dict(request.POST)
        resp = sales_executives_controller.create_sales_executives(sales_executives_obj, file_data)
        return redirect('manage_sales_executives')
    else:
        return render(request, 'indolens_admin/salesExecutive/createSaleExecutives.html')


def editSaleExecutives(request):
    return render(request, 'indolens_admin/salesExecutive/editSaleExecutives.html')


def viewSaleExecutives(request, seid):
    response, status_code = sales_executives_controller.get_sales_executive_by_id(seid)
    print(response)
    return render(request, 'indolens_admin/salesExecutive/viewSaleExecutives.html',
                  {"sales_executive": response['sales_executive']})


def enableDisableSaleExecutives(request, seid, status):
    sales_executives_controller.enable_disable_sales_executive(seid, status)
    return redirect('manage_marketing_head')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageAccountant(request):
    response, status_code = accountant_controller.get_all_accountant()
    return render(request, 'indolens_admin/accountant/manageAccountant.html',
                  {"accountant_list": response['accountant_list']})


def createAccountant(request):
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

        print(form_data)
        file_data = FileData(form_data)

        accountant_obj = accountant_model.accountant_model_from_dict(request.POST)
        print(accountant_obj)
        resp = accountant_controller.create_accountant(accountant_obj, file_data)
        print(resp)
        return redirect('manage_accountant')

    else:
        return render(request, 'indolens_admin/accountant/createAccountant.html')


def editAccountant(request, aid):
    return render(request, 'indolens_admin/accountant/editAccountant.html')


def viewAccountant(request, aid):
    response, status_code = accountant_controller.get_accountant_by_id(aid)
    return render(request, 'indolens_admin/accountant/viewAccountant.html',
                  {"accountant": response['accountant']})


def enableDisableAccountant(request, aid, status):
    accountant_controller.enable_disable_accountant(aid, status)
    return redirect('manage_accountant')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageLabTechnician(request):
    response, status_code = lab_technician_controller.get_all_lab_technician()
    return render(request, 'indolens_admin/labTechnician/manageLabTechnician.html',
                  {"lab_technician_list": response['lab_technician_list']})


def createLabTechnician(request):
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
        resp = lab_technician_controller.create_lab_technician(lab_tech_obj, file_data)
        return redirect('manage_lab_technician')
    else:
        return render(request, 'indolens_admin/labTechnician/createLabTechnician.html')


def editLabTechnician(request, ltid):
    response, status_code = lab_technician_controller.get_lab_technician_by_id(ltid)
    return render(request, 'indolens_admin/labTechnician/editLabTechnician.html',
                  {"lab_technician": response['lab_technician']})


def viewLabTechnician(request, ltid):
    response, status_code = lab_technician_controller.get_lab_technician_by_id(ltid)
    return render(request, 'indolens_admin/labTechnician/viewLabTechnician.html',
                  {"lab_technician": response['lab_technician']})


def enableDisableLabTechnician(request, ltid, status):
    lab_technician_controller.enable_disable_lab_technician(ltid, status)
    return redirect('manage_lab_technician')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageOtherEmployees(request):
    response, status_code = other_employee_controller.get_all_other_emp()
    print(response)
    return render(request, 'indolens_admin/otherEmployees/manageOtherEmployees.html',
                  {"other_employee_list": response['other_emp_list']})


def createOtherEmployees(request):
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
        other_emp_obj = other_employee_model.other_employee_model_from_dict(request.POST)
        resp, status_code = other_employee_controller.create_other_employee(other_emp_obj, file_data)
        return redirect('manage_other_employees')
    else:
        return render(request, 'indolens_admin/otherEmployees/createOtherEmployees.html', )


def editOtherEmployees(request):
    return render(request, 'indolens_admin/otherEmployees/editOtherEmployees.html')


def viewOtherEmployees(request, empid):
    response, status_code = other_employee_controller.get_other_emp_by_id(empid)
    return render(request, 'indolens_admin/otherEmployees/viewOtherEmployees.html',
                  {"other_employee": response['other_employee']})


def enableDisableOtherEmployees(request, empid, status):
    other_employee_controller.enable_disable_other_employees(empid, status)
    return redirect('manage_other_employees')


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
    response, status_code = lab_controller.get_all_labs()
    return render(request, 'indolens_admin/labs/manageLabs.html', {"lab_list": response['lab_list']})


def createLab(request):
    if request.method == 'POST':
        lab_obj = lab_model.lab_model_from_dict(request.POST)
        lab_controller.create_lab(lab_obj)
    return render(request, 'indolens_admin/labs/createLab.html')


def editLab(request, labid):
    if request.method == 'POST':
        lab_obj = lab_model.lab_model_from_dict(request.POST)
        lab_controller.edit_lab_by_id(lab_obj)
        return redirect('manage_labs')
    else:
        response, status_code = lab_controller.get_lab_by_id(labid)
        return render(request, 'indolens_admin/labs/editLab.html', {"lab_data": response['lab_data']})


def viewLab(request, labid):
    response, status_code = lab_controller.get_lab_by_id(labid)
    return render(request, 'indolens_admin/labs/viewLab.html',
                  {"lab_data": response['lab_data']})


def enableDisableLab(request, labid, status):
    lab_controller.enable_disable_lab(labid, status)
    return redirect('manage_labs')


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
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'indolens_admin/masters/manageMastersCategory.html')


def addProductCategory(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'indolens_admin/masters/addProductCategory.html')


def manageMastersBrands(request):
    return render(request, 'indolens_admin/masters/manageMastersBrands.html')


def addMastersBrands(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'indolens_admin/masters/addMastersBrand.html')


def manageMastersShapes(request):
    return render(request, 'indolens_admin/masters/manageMastersShapes.html')


def addMastersShapes(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'indolens_admin/masters/addMastersShapes.html')


def manageMastersFrameType(request):
    return render(request, 'indolens_admin/masters/manageMastersFrameType.html')


def addMastersFrameType(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'indolens_admin/masters/addMastersFrameType.html')


def manageMastersColor(request):
    return render(request, 'indolens_admin/masters/manageMastersColor.html')


def addMastersColor(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'indolens_admin/masters/addMastersColor.html')


def manageMastersMaterials(request):
    return render(request, 'indolens_admin/masters/manageMastersMaterials.html')


def addMastersMaterials(request):
    if request.method == 'POST':
        print(request.POST)
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
