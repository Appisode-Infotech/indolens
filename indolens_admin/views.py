import re
import time

from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from indolens_admin.admin_controllers import admin_auth_controller, own_store_controller, franchise_store_controller, \
    sub_admin_controller, store_manager_controller, franchise_manager_controller, area_head_controller, \
    marketing_head_controller, sales_executives_controller, accountant_controller, lab_technician_controller, \
    lab_controller, other_employee_controller, master_category_controller, master_brand_controller, \
    master_shape_controller, master_frame_type_controller, master_color_controller, master_material_controller, \
    optimetry_controller, master_units_controller, central_inventory_controller, delete_documents_controller, \
    customers_controller, stores_inventory_controller, lens_power_attribute_controller, add_documents_controller, \
    orders_controller, store_expenses, dashboard_controller, eye_test_controller, admin_setting_controller, \
    email_template_controller, send_notification_controller
from indolens_admin.admin_controllers.central_inventory_controller import get_central_inventory_product_single, \
    get_central_inventory_product_restoc_log
from indolens_admin.admin_models.admin_req_model import admin_auth_model, own_store_model, franchise_store_model, \
    sub_admin_model, area_head_model, marketing_head_model, \
    accountant_model, lab_technician_model, lab_model, \
    product_category_model, master_brand_model, master_shape_model, master_frame_type_model, master_color_model, \
    master_material_model, store_employee_model, central_inventory_products_model
from indolens_admin.admin_models.admin_req_model.files_model import FileData
from indolens_own_store.own_store_model.request_model import store_create_stock_request_model


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
            print(response)

            if response['status']:
                if request.session.get('id') is not None:
                    request.session.clear()
                request.session.update({
                    'is_admin_logged_in': True,
                    'id': response['admin']['admin_admin_id'],
                    'name': response['admin']['admin_name'],
                    'profile_pic': response['admin']['admin_profile_pic'],
                    'role': response['admin']['admin_role'],
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
    if request.method == 'POST':
        response, status_code = admin_auth_controller.forgot_password(request.POST['email'])
        return render(request, 'indolens_admin/auth/forgot_password.html',
                      {"message": response['message'], "status": response['status']})
    else:
        return render(request, 'indolens_admin/auth/forgot_password.html', {"status": False})


def resetPassword(request, code):
    if request.method == 'POST':
        response, status_code = admin_auth_controller.update_admin_password(request.POST['password'],
                                                                            request.POST['email'])
        print(response)
        return render(request, 'indolens_admin/auth/reset_password.html',
                      {"code": code, "message": response['message']})
    else:
        response, status_code = admin_auth_controller.check_link_validity(code)
        return render(request, 'indolens_admin/auth/reset_password.html',
                      {"code": code, "message": response['message'], "email": response['email']})


# =================================ADMIN DASH======================================

def dashboard(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        own_store_count, status_code = own_store_controller.get_own_store_count()
        # print(own_store_count)
        franchise_store_count, status_code = franchise_store_controller.get_franchise_stores_count()
        # print(franchise_store_count)
        sales, status_code = orders_controller.get_all_orders('All', 'All', 'All')
        # print(sales)
        own_store_new_order, status_code = dashboard_controller.get_order_stats('New', 1)
        print(own_store_new_order)
        own_store_delivered_orders, status_code = dashboard_controller.get_order_stats('Completed', 1)
        print(own_store_delivered_orders)
        own_store_sales, status_code = dashboard_controller.get_sales_stats(1)
        # print(own_store_sales)
        store_sales_expense_analytics, status_code = dashboard_controller.get_store_analytics()
        # print(store_sales_expense_analytics)
        franchise_store_new_order, status_code = dashboard_controller.get_order_stats('New', 2)
        # print(franchise_store_new_order)
        franchise_store_delivered_orders, status_code = dashboard_controller.get_order_stats('Completed', 2)
        # print(franchise_store_delivered_orders)
        franchise_store_sales, status_code = dashboard_controller.get_sales_stats(2)
        # print(franchise_store_sales)
        out_of_stock, status_code = central_inventory_controller.get_all_out_of_stock_central_inventory_products(15)
        # print(out_of_stock)
        return render(request, 'indolens_admin/dashboard.html',
                      {"own_store_count": own_store_count['own_stores'],
                       "franchise_store_list": franchise_store_count['franchise_store'],
                       "orders_list": sales['latest_orders'], "out_of_stock": len(out_of_stock['stocks_list']),
                       "own_store_new_order": own_store_new_order['count'],
                       "own_store_delivered_orders": own_store_delivered_orders['count'],
                       "franchise_store_new_order": franchise_store_new_order['count'],
                       "franchise_store_delivered_orders": franchise_store_delivered_orders['count'],
                       "own_store_sale": own_store_sales['sale'],
                       "franchise_store_sale": franchise_store_sales['sale'],
                       "own_store_sales_expense_analytics": store_sales_expense_analytics['own_sales_analytics'],
                       "franchise_store_sales_expense_analytics": store_sales_expense_analytics[
                           'franchise_sales_analytics']})
    else:
        return redirect('login')


# =================================ADMIN STORE MANAGEMENT======================================

def manageOwnStores(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = own_store_controller.get_all_own_stores(status)
        print(response)
        return render(request, 'indolens_admin/ownStore/manageOwnStores.html',
                      {"own_store_list": response['own_stores'], "status": status})
    else:
        return redirect('login')


def viewOwnStore(request, ownStoreId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, resp_status_code = own_store_controller.get_own_store_by_id(ownStoreId)
        # print(response)
        products_list, prod_status_code = stores_inventory_controller.get_all_products_for_own_store(ownStoreId)
        # print(products_list)
        store_stats, store_stats_status_code = own_store_controller.get_own_storestore_stats(ownStoreId)
        # print(store_stats)
        sales_data, sale_status_code = orders_controller.get_all_store_orders(ownStoreId, 1)
        print(sales_data)
        revenue_generated, sale_status_code = orders_controller.get_store_sales(ownStoreId, 1)
        # print(revenue_generated)
        store_expense, store_exp_status_code = store_expenses.get_store_expense_amount(ownStoreId, 1)
        # print(store_expense)
        store_expense_list, store_exp_list_status_code = store_expenses.get_store_expense_list(ownStoreId, 1)
        # print(store_expense_list)

        return render(request, 'indolens_admin/ownStore/ownStore.html',
                      {"store_data": response['own_stores'], "products_list": products_list['products_list'],
                       "total_employee_count": store_stats['total_employee_count'],
                       "total_customer_count": store_stats['total_customer_count'],
                       "sales_data": sales_data['orders_list'], "store_expense": store_expense['store_expense'],
                       "revenue_generated": revenue_generated['sale'],
                       "net_income": int(revenue_generated['sale']) - store_expense[
                           'store_expense'], "store_expense_list": store_expense_list['store_expense']})
    else:
        return redirect('login')


def editOwnStore(request, ownStoreId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            store_obj = own_store_model.own_store_model_from_dict(request.POST)
            response, status_code = own_store_controller.edit_own_store_by_id(store_obj)
            print(response)
            if status_code != 200:
                return render(request, 'indolens_admin/ownStore/editOwnStore.html', {"message": response['message']})
            else:
                url = reverse('view_own_store', kwargs={'ownStoreId': ownStoreId})
                return redirect(url)

        else:
            response, status_code = own_store_controller.get_own_store_by_id(ownStoreId)
            print(response)
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
                url = reverse('view_own_store', kwargs={'ownStoreId': response['storeId']})
                return redirect(url)
        return render(request, 'indolens_admin/ownStore/createOwnStore.html')
    else:
        return redirect('login')


def enableDisableOwnStore(request, ownStoreId, status, route):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response = own_store_controller.enable_disable_own_store(ownStoreId, status)
        url = reverse('manage_own_stores', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


def manageFranchiseStores(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_store_controller.get_all_franchise_stores(status)
        print(response)
        return render(request, 'indolens_admin/franchiseStores/manageFranchiseStores.html',
                      {"franchise_store_list": response['franchise_store'], "status": status})
    else:
        return redirect('login')


def viewFranchiseStore(request, franchiseStoreId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_store_controller.get_franchise_store_by_id(franchiseStoreId)
        # print(response)
        products_list, status_code = franchise_store_controller.get_all_products_for_franchise_store(franchiseStoreId)
        print(products_list)
        store_stats, status_code = franchise_store_controller.get_franchise_store_stats(franchiseStoreId)
        # print(store_stats)
        sales_data, status_code = orders_controller.get_all_store_orders(franchiseStoreId, 2)
        # print(sales_data)
        revenue_generated, sale_status_code = orders_controller.get_store_sales(franchiseStoreId, 2)
        store_expense, store_exp_status_code = store_expenses.get_store_expense_amount(franchiseStoreId, 2)
        store_expense_list, store_exp_list_status_code = store_expenses.get_store_expense_list(franchiseStoreId, 2)
        # print(store_expense_list)
        return render(request, 'indolens_admin/franchiseStores/franchiseStore.html',
                      {"franchise_store": response['franchise_store'], "products_list": products_list['products_list'],
                       "total_employee_count": store_stats['total_employee_count'],
                       "total_customer_count": store_stats['total_customer_count'],
                       "sales_data": sales_data['orders_list'], "store_expense": store_expense['store_expense'],
                       "revenue_generated": revenue_generated['sale'],
                       "net_income": int(revenue_generated['sale']) - store_expense[
                           'store_expense'], "store_expense_list": store_expense_list['store_expense']})

    else:
        return redirect('login')


def editFranchiseStore(request, franchiseStoreId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            franchise_obj = franchise_store_model.franchise_store_model_from_dict(request.POST)
            print(vars(franchise_obj))
            response, status_code = franchise_store_controller.edit_franchise_store_by_id(franchise_obj)
            print(response)
            if status_code != 200:
                return render(request, 'indolens_admin/ownStore/editOwnStore.html', {"message": response['message']})
            else:
                url = reverse('view_franchise_store', kwargs={'franchiseStoreId': franchiseStoreId})
                return redirect(url)

        else:
            response, status_code = franchise_store_controller.get_franchise_store_by_id(franchiseStoreId)
            print(response)
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
                url = reverse('view_franchise_store', kwargs={'franchiseStoreId': response['storeId']})
                return redirect(url)

        return render(request, 'indolens_admin/franchiseStores/createFranchiseStore.html')
    else:
        return redirect('login')


def enableDisableFranchiseStore(request, franchiseStoreId, status, route):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response = franchise_store_controller.enable_disable_franchise_store(franchiseStoreId, status)
        url = reverse('manage_Franchise_stores', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# =================================ADMIN SUB ADMIN MANAGEMENT======================================

def manageSubAdmins(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sub_admin_controller.get_all_sub_admin(status)
        print(response)
        return render(request, 'indolens_admin/subAdmin/manageSubAdmins.html',
                      {"sub_admin_list": response['sub_admins'], "status": status})
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
            if status_code == 200:
                url = reverse('view_sub_admin', kwargs={'subAdminId': response['said']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/subAdmin/createSubAdmin.html',
                              {"message": "Something went wrong or email is already in use"})

        else:
            return render(request, 'indolens_admin/subAdmin/createSubAdmin.html')
    else:
        return redirect('login')


def editSubAdmin(request, subAdminId):
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
            sub_admin = sub_admin_model.sub_admin_model_from_dict(request.POST)
            response, status_code = sub_admin_controller.edit_sub_admin(sub_admin, file_data)
            url = reverse('view_sub_admin', kwargs={'subAdminId': subAdminId})
            return redirect(url)
        else:
            response, status_code = sub_admin_controller.get_sub_admin_by_id(subAdminId)
            return render(request, 'indolens_admin/subAdmin/editSubAdmin.html',
                          {"sub_admin": response['sub_admin']})
    else:
        return redirect('login')


def viewSubAdmin(request, subAdminId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sub_admin_controller.get_sub_admin_by_id(subAdminId)
        print(response)
        return render(request, 'indolens_admin/subAdmin/viewSubAdmin.html', {"sub_admin": response['sub_admin']})
    else:
        return redirect('login')


def enableDisableSubAdmin(request, route, subAdminId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response = sub_admin_controller.enable_disable_sub_admin(subAdminId, status)
        url = reverse('manage_sub_admins', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


def updateSubAdminDocuments(request, subAdminId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sub_admin_controller.get_sub_admin_by_id(subAdminId)
        return render(request, 'indolens_admin/subAdmin/updateDocuments.html',
                      {"sub_admin": response['sub_admin']})
    else:
        return redirect('login')


# =================================ADMIN STORE MANAGERS MANAGEMENT======================================

def manageStoreManagers(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = store_manager_controller.get_all_store_manager(status)
        print(response)
        available_stores_response, available_stores_status_code = own_store_controller.get_unassigned_active_own_store_for_manager()
        print(available_stores_response)
        return render(request, 'indolens_admin/storeManagers/manageStoreManagers.html',
                      {"store_managers": response['store_managers'],
                       "available_stores": available_stores_response['available_stores'], "status": status})
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
                    file_name = f"{subdirectory}{file_key}_{int(time.time())}_{str(file_obj)}"
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
            if status_code == 200:
                url = reverse('view_store_manager', kwargs={'storeManagerId': response['mid']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/storeManagers/createStoreManager.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})

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
                                                                            'employee_id', storeManagerId
                                                                            , request.session.get('id'))
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableStoreManager(request, route, storeManagerId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response = store_manager_controller.enable_disable_store_manager(storeManagerId, status)
        url = reverse('manage_store_managers', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# =================================ADMIN FRANCHISE OWNERS MANAGEMENT======================================

def manageFranchiseOwners(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_manager_controller.get_all_franchise_owner(status)
        print(response)
        available_stores_response, available_stores_status_code = franchise_manager_controller.get_active_unassigned_franchise_stores()
        print(available_stores_response)
        return render(request, 'indolens_admin/franchiseOwners/manageFranchiseOwners.html',
                      {"franchise_owners": response['franchise_owners'],
                       "available_stores": available_stores_response['available_stores'], "status": status})
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
            print("==================response=============")
            print(response)
            if status_code == 200:
                url = reverse('view_franchise_owner', kwargs={'franchiseOwnersId': response['franchiseOwnersId']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/franchiseOwners/createFranchiseOwner.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})

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


def enableDisableFranchiseOwner(request, route, franchiseOwnersId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response = franchise_manager_controller.enable_disable_franchise_owner(franchiseOwnersId, status)
        url = reverse('manage_franchise_owners', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


def viewFranchiseOwners(request, franchiseOwnersId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_manager_controller.get_franchise_owner_by_id(franchiseOwnersId)
        print(response)
        return render(request, 'indolens_admin/franchiseOwners/viewFranchiseOwner.html',
                      {"franchise_owner": response['franchise_owner']})
    else:
        return redirect('login')


def updateFranchiseOwnersDocuments(request, franchiseOwnersId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = franchise_manager_controller.get_franchise_owner_by_id(franchiseOwnersId)
        print(response)
        return render(request, 'indolens_admin/franchiseOwners/updateDocuments.html',
                      {"franchise_owner": response['franchise_owner']})
    else:
        return redirect('login')


def deleteFranchiseOwnersDocuments(request, franchiseOwnersId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'franchise_store_employees',
                                                                            'employee_id', franchiseOwnersId
                                                                            , request.session.get('id'))
        return JsonResponse(response)
    else:
        return redirect('login')


# =================================ADMIN AREA HEADS MANAGEMENT======================================

def manageAreaHead(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = area_head_controller.get_all_area_head(status)
        print(response)
        available_stores_response, available_stores_status_code = own_store_controller.get_active_own_stores()
        print(available_stores_response)
        return render(request, 'indolens_admin/areaHead/manageAreaHead.html',
                      {"area_heads_list": response['area_heads_list'],
                       "available_stores": available_stores_response['available_stores'],
                       "status": status})
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

            if status_code == 200:
                url = reverse('view_area_head', kwargs={'areaHeadId': response['areaHeadId']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/areaHead/createAreaHead.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})

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


def enableDisableAreaHead(request, route, areaHeadId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        area_head_controller.enable_disable_area_head(areaHeadId, status)
        url = reverse('manage_area_head', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


def viewAreaHead(request, areaHeadId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = area_head_controller.get_area_head_by_id(areaHeadId)
        print(response)
        return render(request, 'indolens_admin/areaHead/viewAreaHead.html',
                      {"area_head": response['area_head']})
    else:
        return redirect('login')


def UpdateAreaHeadDocuments(request, areaHeadId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = area_head_controller.get_area_head_by_id(areaHeadId)
        print(response)
        return render(request, 'indolens_admin/areaHead/updateDocuments.html',
                      {"area_head": response['area_head']})
    else:
        return redirect('login')


# =================================ADMIN MARKETING HEADS MANAGEMENT======================================

def manageMarketingHead(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = marketing_head_controller.get_all_marketing_head(status)
        return render(request, 'indolens_admin/marketingHeads/manageMarketingHead.html',
                      {"marketing_heads_list": response['marketing_heads_list'], "status": status})
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
            if status_code == 200:
                url = reverse('view_marketing_head', kwargs={'marketingHeadId': response['marketingHeadId']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/marketingHeads/createMarketingHead.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})
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


def enableDisableMarketingHead(request, route, marketingHeadId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        marketing_head_controller.enable_disable_marketing_head(marketingHeadId, status)
        url = reverse('manage_marketing_head', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# =================================ADMIN OWN STORE OPTIMETRY MANAGEMENT======================================


def manageOptimetry(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = optimetry_controller.get_all_optimetry(status)
        print(response)

        available_stores_response, available_stores_status_code = own_store_controller.get_active_own_stores()
        print(available_stores_response)
        return render(request, 'indolens_admin/optimetry/manageOptimetry.html',
                      {"optimetry_list": response['optimetry_list'],
                       "available_stores": available_stores_response['available_stores'], "status": status})
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
            print(response)
            if status_code == 200:
                url = reverse('view_optimetry', kwargs={'ownOptimetryId': response['empid']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/optimetry/createOptimetry.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})
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
            print(response)
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
        print(response)
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
                                                                            'employee_id', ownOptimetryId
                                                                            , request.session.get('id'))
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableOptimetry(request, route, ownOptimetryId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        optimetry_controller.enable_disable_optimetry(ownOptimetryId, status)
        url = reverse('manage_store_optimetry', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# =================================ADMIN OWN STORE OPTIMETRY MANAGEMENT======================================


# =================================ADMIN FRANCHISE STORE OPTIMETRY MANAGEMENT======================================


def manageFranchiseOptimetry(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = optimetry_controller.get_all_franchise_optimetry(status)
        print(response)
        available_stores_response, available_stores_status_code = franchise_manager_controller.get_active_franchise_stores()
        print(available_stores_response)
        return render(request, 'indolens_admin/franchiseOptimetry/manageOptimetry.html',
                      {"optimetry_list": response['optimetry_list'],
                       "available_stores": available_stores_response['available_stores'], "status": status})
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
            if status_code == 200:
                url = reverse('view_franchise_optimetry', kwargs={'franchiseOptimetryId': response['opid']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/franchiseOptimetry/createOptimetry.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})
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
        print(response)
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
                                                                            'employee_id', franchiseOptimetryId
                                                                            , request.session.get('id'))
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableFranchiseOptimetry(request, route, franchiseOptimetryId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        optimetry_controller.enable_disable_franchise_optimetry(franchiseOptimetryId, status)
        url = reverse('manage_franchise_optimetry', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# =================================ADMIN FRANCHISE STORE OPTIMETRY MANAGEMENT======================================
# =================================ADMIN OWN STORE SALES EXECUTIVE MANAGEMENT======================================


def manageSaleExecutives(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sales_executives_controller.get_all_own_sales_executive(status)
        print(response)
        available_stores_response, available_stores_status_code = own_store_controller.get_active_own_stores()
        print(available_stores_response)
        return render(request, 'indolens_admin/salesExecutive/manageSaleExecutives.html',
                      {"sales_executive_list": response['sales_executive_list'],
                       "available_stores": available_stores_response['available_stores'], "status": status})
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
            if status_code == 200:
                url = reverse('view_sales_executives', kwargs={'ownSaleExecutivesId': response['seId']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/salesExecutive/createSaleExecutives.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})
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
        print(response)
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
                                                                            'employee_id', ownSaleExecutivesId
                                                                            , request.session.get('id'))
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableSaleExecutives(request, route, ownSaleExecutivesId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        sales_executives_controller.enable_disable_sales_executive(ownSaleExecutivesId, status)
        url = reverse('manage_store_sales_executives', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# =================================ADMIN OWN STORE SALES EXECUTIVE MANAGEMENT======================================
# =================================ADMIN FRANCHISE STORE SALES EXECUTIVE MANAGEMENT====================================


def manageFranchiseSaleExecutives(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = sales_executives_controller.get_all_franchise_sales_executive(status)
        print(response)
        available_stores_response, available_stores_status_code = franchise_manager_controller.get_active_franchise_stores()
        print(available_stores_response)
        return render(request, 'indolens_admin/franchiseSalesExecutive/manageSaleExecutives.html',
                      {"franchise_sales_executive_list": response['franchise_sales_executive_list'],
                       "available_stores": available_stores_response['available_stores'], "status": status})
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
            if status_code == 200:
                url = reverse('view_franchise_sales_executives',
                              kwargs={'franchiseSaleExecutivesId': response['franchiseSaleExecutivesId']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/franchiseSalesExecutive/createSaleExecutives.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})
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
        print(response)
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
                                                                            'employee_id', franchiseSaleExecutivesId
                                                                            , request.session.get('id'))
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableFranchiseSaleExecutives(request, route, franchiseSaleExecutivesId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        sales_executives_controller.enable_disable_franchise_sales_executive(franchiseSaleExecutivesId, status)
        url = reverse('manage_franchise_sales_executives', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# =================================ADMIN OWN STORE SALES EXECUTIVE MANAGEMENT======================================

# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageAccountant(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = accountant_controller.get_all_accountant(status)
        return render(request, 'indolens_admin/accountant/manageAccountant.html',
                      {"accountant_list": response['accountant_list'], "status": status})
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
            if status_code == 200:
                url = reverse('view_accountant', kwargs={'accountantId': response['aid']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/accountant/createAccountant.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})

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
        print(response)
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


def enableDisableAccountant(request, route, accountantId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        accountant_controller.enable_disable_accountant(accountantId, status)
        url = reverse('manage_accountant', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageLabTechnician(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = lab_technician_controller.get_all_lab_technician(status)
        print(response)
        lab_list, status_code = lab_controller.get_all_active_labs()
        print(lab_list)
        return render(request, 'indolens_admin/labTechnician/manageLabTechnician.html',
                      {"lab_technician_list": response['lab_technician_list'], "lab_list": lab_list['lab_list'],
                       "status": status})
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
            if status_code == 200:
                url = reverse('view_lab_technician', kwargs={'labTechnicianId': response['ltid']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/labTechnician/createLabTechnician.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})
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


def enableDisableLabTechnician(request, route, labTechnicianId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        lab_technician_controller.enable_disable_lab_technician(labTechnicianId, status)
        url = reverse('manage_lab_technician', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# =================================ADMIN ACCOUNTANT MANAGEMENT======================================

def manageOtherEmployees(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = other_employee_controller.get_all_other_emp(status)
        print(response)
        available_stores_response, available_stores_status_code = own_store_controller.get_active_own_stores()
        print(available_stores_response)
        return render(request, 'indolens_admin/otherEmployees/manageOtherEmployees.html',
                      {"other_employee_list": response['other_emp_list'],
                       "available_stores": available_stores_response['available_stores'], "status": status})
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
            if status_code == 200:
                url = reverse('view_other_employees', kwargs={'ownEmployeeId': response['empid']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/otherEmployees/createOtherEmployees.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})
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
        print(response)
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
                                                                            'employee_id', ownEmployeeId
                                                                            , request.session.get('id'))
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableOtherEmployees(request, route, ownEmployeeId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        other_employee_controller.enable_disable_other_employees(ownEmployeeId, status)
        url = reverse('manage_store_other_employees', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# FRANCHISE OTHER EMPLOYEES
def manageFranchiseOtherEmployees(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = other_employee_controller.get_all_franchise_other_emp(status)
        available_stores_response, available_stores_status_code = franchise_manager_controller.get_active_franchise_stores()
        return render(request, 'indolens_admin/franchiseOtherEmployees/manageOtherEmployees.html',
                      {"other_employee_list": response['other_emp_list'],
                       "available_stores": available_stores_response['available_stores'], "status": status})
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
            if status_code == 200:
                url = reverse('view_franchise_other_employees', kwargs={'franchiseEmployeeId': response['empid']})
                return redirect(url)
            else:
                return render(request, 'indolens_admin/franchiseOtherEmployees/createOtherEmployees.html',
                              {
                                  "message": "This email address is already associated with an existing employee account. Please use a different email address."})
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
                                                                            'employee_id', franchiseSaleExecutivesId
                                                                            , request.session.get('id'))
        return JsonResponse(response)
    else:
        return redirect('login')


def enableDisableFranchiseOtherEmployees(request, route, franchiseEmployeeId, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        other_employee_controller.enable_disable_franchise_other_employees(franchiseEmployeeId, status)
        url = reverse('manage_franchise_other_employees', kwargs={'status': route})
        return redirect(url)
    else:
        return redirect('login')


# =================================ADMIN ORDERS MANAGEMENT======================================

def viewAllOrders(request, store):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = orders_controller.get_all_orders('All', 'All', store)
        print(response)
        return render(request, 'indolens_admin/orders/viewAllOrders.html',
                      {"orders_list": response['orders_list'], "store": store})
    else:
        return redirect('login')


def viewDispatchedOrders(request, store):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = orders_controller.get_all_orders('Dispatched', 'All', store)
        return render(request, 'indolens_admin/orders/viewDispatchedOrders.html',
                      {"orders_list": response['orders_list'], "store": store})
    else:
        return redirect('login')


def viewNewOrders(request, store):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = orders_controller.get_all_orders('New', 'All', store)
        return render(request, 'indolens_admin/orders/viewNewOrders.html',
                      {"orders_list": response['orders_list'], "store": store})
    else:
        return redirect('login')


def viewProcessingOrders(request, store):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = orders_controller.get_all_orders('Processing', 'All', store)
        return render(request, 'indolens_admin/orders/viewProcessingOrders.html',
                      {"orders_list": response['orders_list'], "store": store})
    else:
        return redirect('login')


def viewReadyOrders(request, store):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = orders_controller.get_all_orders('Ready', 'All', store)
        return render(request, 'indolens_admin/orders/viewReadyOrders.html',
                      {"orders_list": response['orders_list'], "store": store})
    else:
        return redirect('login')


def viewStoreReadyOrders(request, store):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = orders_controller.get_all_orders('Delivered Store', 'All', store)
        return render(request, 'indolens_admin/orders/viewReadyOrders.html',
                      {"orders_list": response['orders_list'], "store": store})
    else:
        return redirect('login')


def viewCompletedOrders(request, store):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = orders_controller.get_completed_orders('Delivered Customer', 'All', store)
        print(response)
        return render(request, 'indolens_admin/orders/viewCompletedOrders.html',
                      {"orders_list": response['orders_list'], "store": store})
    else:
        return redirect('login')


def viewCancelledOrders(request, store):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = orders_controller.get_all_orders('Cancelled', 'All', store)
        return render(request, 'indolens_admin/orders/viewCancelledOrders.html',
                      {"orders_list": response['orders_list'], "store": store})
    else:
        return redirect('login')


def viewRefundedOrders(request, store):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = orders_controller.get_all_orders('Cancelled', 'Refunded', store)
        return render(request, 'indolens_admin/orders/viewRefundedOrders.html',
                      {"orders_list": response['orders_list'], "store": store})
    else:
        return redirect('login')


def viewOrderDetails(request, orderId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        order_detail, order_status_code = orders_controller.get_order_details(orderId)
        print(order_detail)
        payment_logs, payment_status_code = orders_controller.get_payment_logs(orderId)
        # print(payment_logs)
        return render(request, 'indolens_admin/orders/viewOrderDetails.html',
                      {"order_detail": order_detail['orders_details'], "payment_logs": payment_logs['payment_logs']})
    else:
        return redirect('login')


def orderInvoice(request, orderId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        order_detail, status_code = orders_controller.get_order_details(orderId)
        print(order_detail['orders_details'][0])
        invoice_details, inv_status_code = orders_controller.get_invoice_details(orderId)
        print(invoice_details)
        store_data, store_status_code = orders_controller.get_store_details(
            order_detail['orders_details'][0]['so_created_by_store'],
            order_detail['orders_details'][0]['so_created_by_store_type'])
        print(store_data)
        return render(request, 'indolens_admin/orders/order_invoice.html',
                      {"order_detail": order_detail['orders_details'],
                       "store_data": store_data['store_data'], "invoice_details": invoice_details['invoice_details']})
    else:
        return redirect('login')


def viewRecordCreator(request, employeeID, storeType):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        creator_detail, status_code = orders_controller.get_order_creator_role(employeeID, storeType)
        print(creator_detail)
        role = creator_detail['role']
        role_urls = {}
        if storeType == 1:
            role_urls = {
                1: ('view_store_manager', 'storeManagerId'),
                2: ('view_optimetry', 'ownOptimetryId'),
                3: ('view_sales_executives', 'ownSaleExecutivesId')
            }
        elif storeType == 2:
            role_urls = {
                1: ('view_franchise_owner', 'franchiseOwnersId'),
                2: ('view_franchise_optimetry', 'franchiseOptimetryId'),
                3: ('view_franchise_sales_executives', 'franchiseSaleExecutivesId')
            }

        if role in role_urls:
            url_name, id_key = role_urls[role]
            url = reverse(url_name, kwargs={id_key: employeeID})
            return redirect(url)
        else:
            return redirect('dashboard')
    else:
        return redirect('login')


# =================================ADMIN CUSTOMERS MANAGEMENT======================================

def viewAllCustomers(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = customers_controller.get_all_stores_customers()
        print(response)
        return render(request, 'indolens_admin/customers/viewAllCustomers.html',
                      {"customers_list": response['customers_list']})
    else:
        return redirect('login')


def viewCustomerDetails(request, customerId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = customers_controller.get_customers_by_id(customerId)
        print(response)
        # spending, status_code = customers_controller.get_customer_spend(customerId)
        print(response['customer']['total_spend'])
        sales_data, sale_status_code = orders_controller.get_all_customer_orders(customerId)
        # print(sales_data)
        membership = "Gold"

        if response['customer']['total_spend'] > 5000 and response['customer']['total_spend'] < 25000:
            membership = "Platinum"
        elif response['customer']['total_spend'] > 25000:
            membership = "Luxury"
        return render(request, 'indolens_admin/customers/viewCustomerDetails.html', {"customer": response['customer'],
                                                                                     "sales_data": sales_data[
                                                                                         'orders_list'],
                                                                                     "membership": membership})
    else:
        return redirect('login')


# =================================ADMIN LABS MANAGEMENT======================================

def manageLabs(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = lab_controller.get_all_labs()
        print(response)
        return render(request, 'indolens_admin/labs/manageLabs.html', {"lab_list": response['lab_list']})
    else:
        return redirect('login')


def createLab(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            lab_obj = lab_model.lab_model_from_dict(request.POST)
            response, status_code = lab_controller.create_lab(lab_obj)
            url = reverse('view_lab', kwargs={'labId': response['labId']})
            return redirect(url)
        else:
            return render(request, 'indolens_admin/labs/createLab.html')
    else:
        return redirect('login')


def editLab(request, labId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            lab_obj = lab_model.lab_model_from_dict(request.POST)
            print(vars(lab_obj))
            lab_controller.edit_lab_by_id(lab_obj)
            return redirect('manage_labs')
        else:
            response, status_code = lab_controller.get_lab_by_id(labId)
            print(response)
            return render(request, 'indolens_admin/labs/editLab.html', {"lab_data": response['lab_data']})
    return redirect('login')


def viewLab(request, labId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = lab_controller.get_lab_by_id(labId)
        # print(response)
        lab_job, status_cde = lab_controller.get_lab_job(labId)
        # print(lab_job)
        lab_stats, status_cde = lab_controller.get_lab_stats(labId)
        print(lab_stats)
        return render(request, 'indolens_admin/labs/viewLab.html',
                      {"lab_data": response['lab_data'], "lab_job": lab_job['orders_list'], "lab_stats": lab_stats})
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


def viewAllJobs(request, labId):
    lab_job, status_cde = lab_controller.get_lab_job(labId)
    return render(request, 'indolens_admin/labs/viewAllJobs.html')


def jobDetails(request, jobId):
    job_detail, status_code = orders_controller.get_order_details(jobId)
    print(job_detail)
    return render(request, 'indolens_admin/labs/jobDetails.html', {"order_detail": job_detail['orders_details']})


def viewJobItemDetails(request, saleId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get(
            'is_admin_logged_in') is True:
        job_detail, status_code = lab_controller.get_lab_job_authenticity_card(saleId)
        print(job_detail)
        return render(request, 'indolens_admin/labs/jobItemDetails.html',
                      {"job_item_detail": job_detail['orders_details'],
                       "frame_list": job_detail['frame_list']})
    else:
        return redirect('login')


def labcontactLensPowerCard(request, saleId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get(
            'is_admin_logged_in') is True:
        job_detail, status_code = lab_controller.get_lab_job_authenticity_card(saleId)
        print(job_detail)
        return render(request, 'indolens_admin/labs/contactLensPowerCard.html',
                      {"order_detail": job_detail['orders_details']})
    else:
        return redirect('login')


def manageAuthenticityCard(request, saleId, frame):
    if request.session.get('is_admin_logged_in') is not None and request.session.get(
            'is_admin_logged_in') is True:
        job_detail, status_code = lab_controller.get_lab_job_authenticity_card(saleId)
        print(job_detail)
        return render(request, 'Tasks/authenticityCar.html', {"order_detail": job_detail['orders_details'],
                                                              "frame": frame})
    else:
        return redirect('login')


def createAuthenticityCard(request):
    return render(request, 'indolens_admin/labs/createAuthenticityCard.html')


# =================================ADMIN LABS MANAGEMENT======================================

def manageMastersCategory(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = master_category_controller.get_all_central_inventory_category()
        print(response)
        return render(request, 'indolens_admin/masters/manageMastersCategory.html',
                      {"product_category": response['product_category']})
    else:
        return redirect('login')


def addProductCategory(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            product_cat_obj = product_category_model.product_category_model_from_dict(request.POST)
            response, status_code = master_category_controller.add_product_category(product_cat_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                return render(request, 'indolens_admin/masters/addProductCategory.html',
                              {"message": f"""Error Duplicate Entry: product category- {product_cat_obj.category_name} 
                              with prefix- {product_cat_obj.category_prefix} exist"""})
            else:
                return redirect('manage_central_inventory_category')
        else:
            return render(request, 'indolens_admin/masters/addProductCategory.html')
    else:
        return redirect('login')


def editProductCategory(request, categoryId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            product_cat_obj = product_category_model.product_category_model_from_dict(request.POST)
            response, status_code = master_category_controller.edit_product_category(product_cat_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                product_category, status_code = master_category_controller.get_central_inventory_category_by_id(
                    categoryId)
                return render(request, 'indolens_admin/masters/editProductCategory.html',
                              {"product_category": product_category['product_category'],
                               "message": f"""Error Duplicate Entry: product category- {product_cat_obj.category_name} 
                              with prefix- {product_cat_obj.category_prefix} exist"""})
            else:
                return redirect('manage_central_inventory_category')
        else:
            if categoryId == 1 or categoryId == 2 or categoryId == 3:
                return redirect('manage_central_inventory_category')
            else:
                response, status_code = master_category_controller.get_central_inventory_category_by_id(categoryId)
                print(response)
                return render(request, 'indolens_admin/masters/editProductCategory.html',
                              {"product_category": response['product_category']})
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
        print(response)
        return render(request, 'indolens_admin/masters/manageMastersBrands.html',
                      {"product_brand": response["product_brand"]})
    else:
        return redirect('login')


def addMastersBrands(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            master_brand_obj = master_brand_model.master_brand_model_from_dict(request.POST)
            response, status_code = master_brand_controller.add_product_brand(master_brand_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                return render(request, 'indolens_admin/masters/addMastersBrand.html',
                              {"message": f"""Error Duplicate Entry: Brand name- {master_brand_obj.brand_name} already 
                              exist"""})
            else:
                return redirect('manage_central_inventory_brands')
        else:
            return render(request, 'indolens_admin/masters/addMastersBrand.html')
    else:
        return redirect('login')


def editMastersBrands(request, brandId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            master_brand_obj = master_brand_model.master_brand_model_from_dict(request.POST)
            response, status_code = master_brand_controller.edit_product_brand(master_brand_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                product_brand, status_code = master_brand_controller.get_central_inventory_brand_by_id(brandId)
                return render(request, 'indolens_admin/masters/editMastersBrand.html',
                              {"product_brand": product_brand['product_brand'],
                               "message": f"""Error Duplicate Entry: Brand name- {master_brand_obj.brand_name} already 
                              exist"""})
            else:
                return redirect('manage_central_inventory_brands')
        else:
            response, status_code = master_brand_controller.get_central_inventory_brand_by_id(brandId)
            return render(request, 'indolens_admin/masters/editMastersBrand.html',
                          {"product_brand": response['product_brand']})
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
        print(response)
        return render(request, 'indolens_admin/masters/manageMastersShapes.html',
                      {"product_shape": response["product_shape"]})
    else:
        return redirect('login')


def addMastersShapes(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':

            master_shape_obj = master_shape_model.master_shape_model_from_dict(request.POST)
            response, status_code = master_shape_controller.add_frame_shape(master_shape_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                return render(request, 'indolens_admin/masters/addMastersShapes.html',
                              {"message": f"""Error Duplicate Entry: Frame Shape- {master_shape_obj.shape_name} already 
                              exist"""})
            else:
                return redirect('manage_central_inventory_shapes')
        else:
            return render(request, 'indolens_admin/masters/addMastersShapes.html')
    else:
        return redirect('login')


def editMastersShapes(request, shapeId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            master_shape_obj = master_shape_model.master_shape_model_from_dict(request.POST)
            response, status_code = master_shape_controller.edit_frame_shape(master_shape_obj)
            print(response)
            if not response['status'] and "Duplicate entry" in response['message']:
                product_shape, status_code = master_shape_controller.get_central_inventory_shapes_by_id(shapeId)
                return render(request, 'indolens_admin/masters/editMastersShapes.html',
                              {"product_shape": product_shape['product_shape'],
                               "message": f"""Error Duplicate Entry: Frame Shape- {master_shape_obj.shape_name} already 
                              exist"""})
            else:
                return redirect('manage_central_inventory_shapes')
        else:
            response, status_code = master_shape_controller.get_central_inventory_shapes_by_id(shapeId)
            print(response)
            return render(request, 'indolens_admin/masters/editMastersShapes.html',
                          {"product_shape": response['product_shape']})
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
        print(response)
        return render(request, 'indolens_admin/masters/manageMastersFrameType.html',
                      {"frame_type": response["frame_type"]})
    else:
        return redirect('login')


def addMastersFrameType(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            frame_type_obj = master_frame_type_model.master_frame_type_model_from_dict(request.POST)
            response, status_code = master_frame_type_controller.add_frame_type(frame_type_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                return render(request, 'indolens_admin/masters/addMastersFrameType.html',
                              {"message": f"""Error Duplicate Entry: Frame type- {frame_type_obj.frame_type_name} already 
                              exist"""})
            else:
                return redirect('manage_central_inventory_frame_types')
        else:
            return render(request, 'indolens_admin/masters/addMastersFrameType.html')
    else:
        return redirect('login')


def editMastersFrameType(request, frameId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':

            frame_type_obj = master_frame_type_model.master_frame_type_model_from_dict(request.POST)
            response, status_code = master_frame_type_controller.edit_frame_type(frame_type_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                frame_type, status_code = master_frame_type_controller.get_central_inventory_frame_types_by_id(frameId)
                return render(request, 'indolens_admin/masters/editMastersFrameType.html',
                              {"frame_type": frame_type['frame_type'],
                               "message": f"""Error Duplicate Entry: Frame type- {frame_type_obj.frame_type_name} already 
                              exist"""})
            else:
                return redirect('manage_central_inventory_frame_types')
        else:
            response, status_code = master_frame_type_controller.get_central_inventory_frame_types_by_id(frameId)
            return render(request, 'indolens_admin/masters/editMastersFrameType.html',
                          {"frame_type": response['frame_type']})
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
        print(response)
        return render(request, 'indolens_admin/masters/manageMastersColor.html',
                      {"frame_color": response["frame_color"]})
    else:
        return redirect('login')


def addMastersColor(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            color_obj = master_color_model.master_color_model_from_dict(request.POST)
            response, status_code = master_color_controller.add_master_color(color_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                return render(request, 'indolens_admin/masters/addMastersColor.html',
                              {"message": f"""Error Duplicate Entry: Colour with code- {color_obj.color_code} 
                              and name- {color_obj.color_name} already exist"""})
            else:
                return redirect('manage_central_inventory_color')
        else:
            return render(request, 'indolens_admin/masters/addMastersColor.html')
    else:
        return redirect('login')


def editMastersColor(request, colorId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            color_obj = master_color_model.master_color_model_from_dict(request.POST)
            response, status_code = master_color_controller.edit_master_color(color_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                frame_color, status_code = master_color_controller.get_central_inventory_color_by_id(colorId)
                return render(request, 'indolens_admin/masters/editMastersColor.html',
                              {"frame_color": frame_color['frame_color'],
                               "message": f"""Error Duplicate Entry: Colour with code- {color_obj.color_code} 
                              and name- {color_obj.color_name} already exist"""})
            else:
                return redirect('manage_central_inventory_color')
        else:
            response, status_code = master_color_controller.get_central_inventory_color_by_id(colorId)
            return render(request, 'indolens_admin/masters/editMastersColor.html',
                          {"frame_color": response['frame_color']})
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
        print(response)
        return render(request, 'indolens_admin/masters/manageMastersMaterials.html',
                      {"frame_material": response["frame_material"]})
    else:
        return redirect('login')


def addMastersMaterials(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            material_obj = master_material_model.master_material_model_from_dict(request.POST)
            response, status_code = master_material_controller.add_master_material(material_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                return render(request, 'indolens_admin/masters/addMastersMaterials.html',
                              {"message": f"""Error Duplicate Entry: Material- {material_obj.material_name} already 
                              exist"""})
            else:
                return redirect('manage_central_inventory_materials')
        else:
            return render(request, 'indolens_admin/masters/addMastersMaterials.html')
    else:
        return redirect('login')


def editMastersMaterials(request, materialId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            material_obj = master_material_model.master_material_model_from_dict(request.POST)
            response, status_code = master_material_controller.edit_master_material(material_obj)
            if not response['status'] and "Duplicate entry" in response['message']:
                product_material, status_code = master_material_controller.get_central_inventory_materials_by_id(
                    materialId)
                return render(request, 'indolens_admin/masters/editMastersMaterials.html',
                              {"product_material": product_material['product_material'],
                               "message": f"""Error Duplicate Entry: Material- {material_obj.material_name} already 
                              exist"""})
            else:
                return redirect('manage_central_inventory_materials')
        else:
            response, status_code = master_material_controller.get_central_inventory_materials_by_id(materialId)
            print(response)
            return render(request, 'indolens_admin/masters/editMastersMaterials.html',
                          {"product_material": response['product_material']})
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
        print(response)
        return render(request, 'indolens_admin/masters/manageMastersUnits.html',
                      {"units_list": response['units_list']})
    else:
        return redirect('login')


def addMastersUnits(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            data = request.POST
            response, status_code = master_units_controller.add_masters_units(data)
            if not response['status'] and "Duplicate entry" in response['message']:
                units_list, status_code = master_units_controller.get_all_units()
                return render(request, 'indolens_admin/masters/manageMastersUnits.html',
                              {"units_list": units_list['units_list'],
                               "message": f"""Error Duplicate Entry: Unit- {data['unit_name']} already exist"""})
            else:
                return redirect('manage_central_inventory_units')
        else:
            return redirect('manage_central_inventory_units')
    else:
        return redirect('login')


def editMastersUnits(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            data = request.POST
            response, status_code = master_units_controller.edit_master_units(data)
            if not response['status'] and "Duplicate entry" in response['message']:
                units_list, status_code = master_units_controller.get_all_units()
                return render(request, 'indolens_admin/masters/manageMastersUnits.html',
                              {"units_list": units_list['units_list'],
                               "message": f"""Error Duplicate Entry: Unit- {data['unit_name']} already exist"""})
            else:
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


def manageCentralInventoryProducts(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_central_inventory_products(status)
        return render(request, 'indolens_admin/centralInventory/manageCentralInventoryProducts.html',
                      {"product_list": response['product_list'], "categories_List": response['categoriesList'],
                       "status": status})
    else:
        return redirect('login')


def DownloadCentralInventoryProductsCatalog(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_central_inventory_products('All')
        return render(request, 'indolens_admin/centralInventory/downloadCentralInventoryProductsCatalog.html',
                      {"product_list": response['product_list'], "categories_List": response['categoriesList']})
    else:
        return redirect('login')


def restockProduct(request, status):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = central_inventory_controller.restock_central_inventory_products(
            request.POST['productId'], request.POST['productQty'], request.session.get('id'))
        url = reverse('manage_central_inventory_products', kwargs={'status': status})
        return redirect(url)
    else:
        return redirect('login')


def restockProductOutOfStock(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = central_inventory_controller.restock_central_inventory_products(
            request.POST['productId'], request.POST['productQty'], request.session.get('id'))
        return redirect('manage_out_of_stock')
    else:
        return redirect('login')


def centralInventoryUpdateProduct(request, productId):
    if request.method == 'POST':
        print(request.POST)
        power_attributes = lens_power_attribute_controller.get_power_attribute(request.POST)
        product_obj = central_inventory_products_model.inventory_add_products_from_dict(request.POST)
        print(vars(product_obj))
        response, status_code = central_inventory_controller.update_central_inventory_products(product_obj, productId,
                                                                                               power_attributes)
        url = reverse('view_products', kwargs={'productId': productId})
        return redirect(url)
    else:
        response, status_code = get_central_inventory_product_single(productId)
        print(response)
        types, status_code = central_inventory_controller.get_all_active_types()
        return render(request, 'indolens_admin/centralInventory/centralInventoryUpdateProduct.html',
                      {'product_data': response['product_data'], 'productId': productId, "response": types})


def centralInventoryUpdateProductStatus(request, filter, productId, status):
    response, status_code = central_inventory_controller.change_product_status(productId, status)
    url = reverse('manage_central_inventory_products', kwargs={'status': filter})
    return redirect(url)


def centralInventoryUpdateProductImages(request, productId):
    response, status_code = get_central_inventory_product_single(productId)
    # print(response)
    return render(request, 'indolens_admin/centralInventory/updateproductImages.html',
                  {'product_data': response['product_data'], 'productId': productId})


def centralInventoryViewProducts(request, productId):
    response, status_code = get_central_inventory_product_single(productId)
    print(response)
    return render(request, 'indolens_admin/centralInventory/centralInventoryViewProduct.html',
                  {'product_data': response['product_data'], 'productId': productId})


def centralInventoryViewProductRestockLogs(request, productId):
    response, status_code = get_central_inventory_product_restoc_log(productId)
    print(response)
    return render(request, 'indolens_admin/centralInventory/centralInventoryProductLogs.html',
                  {"restock_logs": response['restock_logs']})


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
            power_attributes = lens_power_attribute_controller.get_power_attribute(request.POST)
            response, status_code = central_inventory_controller.add_central_inventory_products(product_obj, file_data,
                                                                                                power_attributes)
            print(response)
            url = reverse('view_products', kwargs={'productId': response['productId']})
            return redirect(url)
        else:
            response, status_code = central_inventory_controller.get_all_active_types()
            # print(response)
            return render(request, 'indolens_admin/centralInventory/centralInventoryAddProducts.html', response)

    else:
        return redirect('login')


def manageCentralInventoryOutOfStock(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_out_of_stock_central_inventory_products(15)
        print(response)
        return render(request, 'indolens_admin/centralInventory/manageCentralInventoryOutOfStock.html',
                      {"stocks_list": response['stocks_list'], "categories_list": response['categories_list']})
    else:
        return redirect('login')


def manageMoveStocks(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            stock_obj = store_create_stock_request_model.store_create_stock_request_model_from_dict(request.POST)
            print(vars(stock_obj))
            if request.POST['own_store_id'] != '':
                store_id = request.POST['own_store_id']
            else:
                store_id = request.POST['franchise_store_id']
            response = central_inventory_controller.create_store_stock_request(stock_obj, store_id)
            print(response)
            return redirect('manageMoveStocks')
        else:
            moved_stocks, status_code = central_inventory_controller.get_all_moved_stocks_list('1')
            print(moved_stocks)
            own_store, status_code = own_store_controller.get_all_own_stores('Active')
            # print(own_store)
            franchise_store, status_code = franchise_store_controller.get_all_franchise_stores('Active')
            # print(franchise_store)
            products, status_code = central_inventory_controller.get_central_inventory_products_to_move('Active')
            # print(products)
            return render(request, 'indolens_admin/centralInventory/manageMoveStocks.html',
                          {"own_store_list": own_store['own_stores'], "products": products['product_list'],
                           "franchise_store_list": franchise_store['franchise_store'],
                           "moved_stocks": moved_stocks['stocks_request_list']})
    else:
        return redirect('login')


def manageMoveAStock(request):
    return render(request, 'indolens_admin/centralInventory/manageMoveAStock.html')


# =================================ADMIN STORE MANAGEMENT======================================


def viewAllStockRequests(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_stock_requests('%')
        print(response)
        return render(request, 'indolens_admin/stockRequests/viewAllStockRequests.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('login')


def viewStockRequestInvoice(request, requestId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = central_inventory_controller.get_stock_requests_by_id(requestId)
        print(response['stocks_request'])
        store_data = []
        if response['stocks_request'].get('pr_request_to_store_id') != 0:
            store, resp_status_code = own_store_controller.get_own_store_by_id(
                response['stocks_request']['pr_request_to_store_id'])
            store_data = store['own_stores']

        print(store_data)
        return render(request, 'indolens_admin/stockRequests/franchiseStockMovementInvoice.html',
                      {"stocks_request": response['stocks_request'], "store_data": store_data})
    else:
        return redirect('login')


def viewPendingStockRequests(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_stock_requests('0')
        return render(request, 'indolens_admin/stockRequests/viewPendingStockRequests.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('login')


def viewCompletedStockRequests(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_stock_requests('1')
        print(response)
        return render(request, 'indolens_admin/stockRequests/viewCompletedStockRequests.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('login')


def viewRejectedStockRequests(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = central_inventory_controller.get_all_stock_requests('2')
        return render(request, 'indolens_admin/stockRequests/viewrejectedStockRequests.html',
                      {"stocks_request_list": response['stocks_request_list']})
    else:
        return redirect('login')


def changeStockRequestStatus(request, route, requestId, status):
    print(route, requestId, status)
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.POST:
            print("Rejected")
            response, status_code = central_inventory_controller.change_stock_request_status_with_reason(requestId,
                                                                                                         status,
                                                                                                         request.session.get(
                                                                                                             'id'),
                                                                                                         request.POST[
                                                                                                             'reject_reason'])
            print(response)

        else:
            print("Accepted")
            response, status_code = central_inventory_controller.change_stock_request_status(requestId, status,
                                                                                             request.session.get('id'))
            print(response)

        if route == 'All':
            if response['status']:
                return redirect('all_stock_requests')
            else:
                request_list, status_code = central_inventory_controller.get_all_stock_requests('%')
                return render(request, 'indolens_admin/stockRequests/viewAllStockRequests.html',
                              {"stocks_request_list": request_list['stocks_request_list'],
                               "message": response['message']})
        else:
            if response['status']:
                return redirect('pending_stock_requests')
            else:
                request_list, status_code = central_inventory_controller.get_all_stock_requests('0')
                return render(request, 'indolens_admin/stockRequests/viewPendingStockRequests.html',
                              {"stocks_request_list": request_list['stocks_request_list'],
                               "message": response['message']})

    else:
        return redirect('login')


def assignManagerOwnStore(request, route):
    if request.method == 'POST':
        response, status_code = store_manager_controller.assignStore(request.POST['emp_id'], request.POST['store_id'],
                                                                     'Manager')
        url = reverse('manage_store_managers', kwargs={'status': route})
        return redirect(url)


def unAssignManagerOwnStore(request, route, empId, storeId):
    response, status_code = store_manager_controller.unAssignStore(empId, storeId, 'Manager')
    url = reverse('manage_store_managers', kwargs={'status': route})
    return redirect(url)


def assignOptimetryOwnStore(request, route):
    if request.method == 'POST':
        response, status_code = store_manager_controller.assignStore(request.POST['emp_id'], request.POST['store_id'], 'Optometry')
        url = reverse('manage_store_optimetry', kwargs={'status': route})
        return redirect(url)


def unAssignOptimetryOwnStore(request, route, empId, storeId):
    response, status_code = store_manager_controller.unAssignStore(empId, storeId, 'Optometry')
    url = reverse('manage_store_optimetry', kwargs={'status': route})
    return redirect(url)


def assignSalesExecutiveOwnStore(request, route):
    if request.method == 'POST':
        response, status_code = sales_executives_controller.assign_store_own_store_sales_executive(
            request.POST['emp_id'], request.POST['store_id'])
        url = reverse('manage_store_sales_executives', kwargs={'status': route})
        return redirect(url)


def unAssignSalesExecutiveOwnStore(request, route, salesExecutiveId, storeId):
    response, status_code = sales_executives_controller.unassign_store_own_store_sales_executive(salesExecutiveId,
                                                                                                 storeId)
    url = reverse('manage_store_sales_executives', kwargs={'status': route})
    return redirect(url)


def assignOtherEmployeeOwnStore(request, route):
    if request.method == 'POST':
        response, status_code = other_employee_controller.assign_store_own_store_other_employee(request.POST['emp_id'],
                                                                                                request.POST[
                                                                                                    'store_id'])
        url = reverse('manage_store_other_employees', kwargs={'status': route})
        return redirect(url)


def unAssignOtherEmployeeOwnStore(request, route, otherEmployeeId, storeId):
    response, status_code = other_employee_controller.unassign_store_own_store_other_employee(otherEmployeeId, storeId)
    url = reverse('manage_store_other_employees', kwargs={'status': route})
    return redirect(url)


def assignFranchiseStoreOwner(request, route):
    if request.method == 'POST':
        response, status_code = franchise_manager_controller.assign_store_franchise_owner(request.POST['emp_id'],
                                                                                          request.POST['store_id'],
                                                                                          'Franchise Owner')
        url = reverse('manage_franchise_owners', kwargs={'status': route})
        return redirect(url)


def unAssignFranchiseStoreOwner(request, route, FranchiseOwnerId, storeId):
    response, status_code = franchise_manager_controller.unassign_store_franchise_owner(FranchiseOwnerId, storeId,
                                                                                        'Franchise Owner')
    url = reverse('manage_franchise_owners', kwargs={'status': route})
    return redirect(url)


def assignFranchiseStoreOptimetry(request, route):
    if request.method == 'POST':
        response, status_code = franchise_manager_controller.assign_store_franchise_owner(request.POST['emp_id'],
                                                                                          request.POST['store_id'],
                                                                                          'Optometry')
        url = reverse('manage_franchise_optimetry', kwargs={'status': route})
        return redirect(url)


def unAssignFranchiseStoreOptimetry(request, route, FranchiseOptimetryId, storeId):
    response, status_code = franchise_manager_controller.unassign_store_franchise_owner(FranchiseOptimetryId, storeId,
                                                                                        'Optometry')
    url = reverse('manage_franchise_optimetry', kwargs={'status': route})
    return redirect(url)


def assignFranchiseStoreSalesExecutive(request, route):
    if request.method == 'POST':
        response, status_code = franchise_manager_controller.assign_store_franchise_owner(request.POST['emp_id'],
                                                                                          request.POST['store_id'],
                                                                                          'Sales Executive')
        url = reverse('manage_franchise_sales_executives', kwargs={'status': route})
        return redirect(url)


def unAssignFranchiseStoreSalesExecutive(request, route, FranchiseSalesExecutiveId, storeId):
    response, status_code = franchise_manager_controller.unassign_store_franchise_owner(FranchiseSalesExecutiveId,
                                                                                        storeId, 'Sales Executive')
    url = reverse('manage_franchise_sales_executives', kwargs={'status': route})
    return redirect(url)


def assignFranchiseStoreOtherEmployee(request, route):
    if request.method == 'POST':
        response, status_code = franchise_manager_controller.assign_store_franchise_owner(request.POST['emp_id'],
                                                                                          request.POST['store_id'],
                                                                                          'Store Employee')
        url = reverse('manage_franchise_other_employees', kwargs={'status': route})
        return redirect(url)


def unAssignFranchiseStoreOtherEmployee(request, route, FranchiseOtherEmployeeId, storeId):
    response, status_code = franchise_manager_controller.unassign_store_franchise_owner(FranchiseOtherEmployeeId,
                                                                                        storeId, 'Store Employee')
    url = reverse('manage_franchise_other_employees', kwargs={'status': route})
    return redirect(url)


def assignAreaHeadOwnStore(request):
    if request.method == 'POST':
        response, status_code = area_head_controller.assignStore(request.POST['emp_id'],
                                                                 ','.join(request.POST.getlist('store_id')))
    url = reverse('manage_area_head', kwargs={'status': 'All'})
    return redirect(url)


def unAssignAreaHeadOwnStore(request, empId, storeId):
    response, status_code = area_head_controller.unAssignStore(empId, storeId, 'Optometry')
    url = reverse('manage_area_head', kwargs={'status': 'All'})
    return redirect(url)


def assignLabTechnician(request, route):
    if request.method == 'POST':
        response, status_code = lab_technician_controller.assign_lab(request.POST['lab_technician_id'],
                                                                     request.POST['lab_id'])
        url = reverse('manage_lab_technician', kwargs={'status': route})
        return redirect(url)


def unAssignLabTechnician(request, route, LabTechnicianId, labId):
    response, status_code = lab_technician_controller.unassign_lab(LabTechnicianId, labId)
    url = reverse('manage_lab_technician', kwargs={'status': route})
    return redirect(url)


# =============================================== DELETE DOCUMENTS =============================================

def deleteSubAdminDocuments(request, subAdminId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_admin_document(documentURL, document_Type,
                                                                            'admin', 'admin_admin_id', subAdminId
                                                                            , request.session.get('id'))
        url = reverse('update_sub_admin_documents', kwargs={'subAdminId': subAdminId})
        return redirect(url)
    else:
        return redirect('login')


def deleteAreaHeadDocuments(request, areaHeadId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_ah_document(documentURL, document_Type,
                                                                            'area_head', 'ah_area_head_id', areaHeadId
                                                                            , request.session.get('id'))
        url = reverse('update_area_head_documents', kwargs={'areaHeadId': areaHeadId})
        return redirect(url)
    else:
        return redirect('login')


def deleteMarketingHeadDocuments(request, marketingHeadId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'marketing_head', 'marketing_head_id',
                                                                            marketingHeadId
                                                                            , request.session.get('id'))
        url = reverse('update_marketing_head_documents', kwargs={'marketingHeadId': marketingHeadId})
        return redirect(url)
    else:
        return redirect('login')


def deleteAccountantDocuments(request, accountantId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_accountant_document(documentURL, document_Type,
                                                                            'accountant', 'ac_accountant_id', accountantId
                                                                            , request.session.get('id'))
        url = reverse('update_accountant_documents', kwargs={'accountantId': accountantId})
        return redirect(url)
    else:
        return redirect('login')


def deleteLabTechnicianDocuments(request, labTechnicianId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_lt_document(documentURL, document_Type,
                                                                            'lab_technician', 'lt_lab_technician_id',
                                                                            labTechnicianId
                                                                            , request.session.get('id'))
        url = reverse('update_lab_technician_documents', kwargs={'labTechnicianId': labTechnicianId})
        return redirect(url)
    else:
        return redirect('login')


def deleteOwnStoreEmployeeDocuments(request, employeeId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_document(documentURL, document_Type,
                                                                            'own_store_employees', 'ose_employee_id',
                                                                            employeeId, request.session.get('id'))
        print(response)

        role = response['role']

        # Dictionary mapping roles to URLs and their respective keyword arguments
        role_urls = {
            1: ('update_store_manager_documents', 'storeManagerId'),
            2: ('update_optimetry_documents', 'ownOptimetryId'),
            3: ('update_sales_executives_documents', 'ownSaleExecutivesId'),
            4: ('update_other_employees_documents', 'ownEmployeeId')
        }

        if role in role_urls:
            url_name, id_key = role_urls[role]
            url = reverse(url_name, kwargs={id_key: employeeId})
            return redirect(url)
        else:
            return redirect('dashboard')
    else:
        return redirect('login')


def deleteFranchiseStoreEmployeeDocuments(request, employeeId, documentURL, document_Type):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_fse_document(documentURL, document_Type,
                                                                            'franchise_store_employees', 'fse_employee_id',
                                                                            employeeId, request.session.get('id'))
        print(response)
        role = response['role']

        # Dictionary mapping roles to URLs and their respective keyword arguments
        role_urls = {
            1: ('update_franchise_owner_documents', 'franchiseOwnersId'),
            2: ('update_franchise_optimetry_documents', 'franchiseOptimetryId'),
            3: ('update_franchise_sales_executives_documents', 'franchiseSaleExecutivesId'),
            4: ('update_franchise_other_employees_documents', 'franchiseEmployeeId')
        }

        if role in role_urls:
            url_name, id_key = role_urls[role]
            url = reverse(url_name, kwargs={id_key: employeeId})
            return redirect(url)
        else:
            return redirect('dashboard')
    else:
        return redirect('login')


def deleteProductImage(request, productId, imageURL):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = delete_documents_controller.delete_product_image(imageURL, productId)
        print(response)
        url = reverse('update_product_images', kwargs={'productId': productId})
        return redirect(url)
    else:
        return redirect('login')


def addProductImage(request, productId):
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
            response, status_code = add_documents_controller.add_products_image(file_data, productId,
                                                                                request.session.get('id'))
            print(response)
        url = reverse('update_product_images', kwargs={'productId': productId})
        return redirect(url)
    else:
        return redirect('login')


def print_qr_tag(request, qrUrl, price, pId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        print('hello')
        return render(request, 'indolens_admin/centralInventory/qr_tag_print.html',
                      {'qrUrl': qrUrl, "price": price, "pId": pId})
    else:
        return redirect('login')


def addOwnStoreEmployeeImage(request, employeeId):
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
                    file_name = f"{subdirectory}{file_key}_{int(time.time())}_{str(file_obj)}"
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
            emp_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = add_documents_controller.add_own_store_employee_image(file_data, employeeId,
                                                                                          emp_obj,
                                                                                          request.session.get('id'))
            print(response)
            role = response['role']

            # Dictionary mapping roles to URLs and their respective keyword arguments
            role_urls = {
                1: ('update_store_manager_documents', 'storeManagerId'),
                2: ('update_optimetry_documents', 'ownOptimetryId'),
                3: ('update_sales_executives_documents', 'ownSaleExecutivesId'),
                4: ('update_other_employees_documents', 'ownEmployeeId')
            }

            if role in role_urls:
                url_name, id_key = role_urls[role]
                url = reverse(url_name, kwargs={id_key: employeeId})
                return redirect(url)
            else:
                return redirect('dashboard')
    else:
        return redirect('login')


def addFranchiseStoreEmployeeImage(request, employeeId):
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
                    file_name = f"{subdirectory}{file_key}_{int(time.time())}_{str(file_obj)}"
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
            emp_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = add_documents_controller.add_franchise_store_employee_image(file_data, employeeId,
                                                                                                emp_obj,
                                                                                                request.session.get(
                                                                                                    'id'))
            print(response)
            role = response['role']

            # Dictionary mapping roles to URLs and their respective keyword arguments
            role_urls = {
                1: ('update_franchise_owner_documents', 'franchiseOwnersId'),
                2: ('update_franchise_optimetry_documents', 'franchiseOptimetryId'),
                3: ('update_franchise_sales_executives_documents', 'franchiseSaleExecutivesId'),
                4: ('update_franchise_other_employees_documents', 'franchiseEmployeeId')
            }

            if role in role_urls:
                url_name, id_key = role_urls[role]
                url = reverse(url_name, kwargs={id_key: employeeId})
                return redirect(url)
            else:
                return redirect('dashboard')
    else:
        return redirect('login')


def addSubAdminDocuments(request, subAdminId):
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
                    file_name = f"{subdirectory}{file_key}_{int(time.time())}_{str(file_obj)}"
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
            emp_obj = store_employee_model.store_employee_from_dict(request.POST)
            response, status_code = add_documents_controller.add_sub_admin_doc(file_data, subAdminId, emp_obj,
                                                                               request.session.get('id'))

            url = reverse('update_sub_admin_documents', kwargs={'subAdminId': subAdminId})
            return redirect(url)
    else:
        return redirect('login')


def addAreaHeadDocuments(request, areaHeadId):
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
                    file_name = f"{subdirectory}{file_key}_{int(time.time())}_{str(file_obj)}"
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
            print("+++++++++++++++++++++++++++")
            print(request.POST)
            print(vars(area_head))
            response, status_code = add_documents_controller.add_area_head_doc(file_data, areaHeadId, area_head,
                                                                               request.session.get('id'))

            url = reverse('update_area_head_documents', kwargs={'areaHeadId': areaHeadId})
            return redirect(url)
    else:
        return redirect('login')


def addAccountantDocuments(request, accountantId):
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
                    file_name = f"{subdirectory}{file_key}_{int(time.time())}_{str(file_obj)}"
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
            accountant = accountant_model.accountant_model_from_dict(request.POST)
            response, status_code = add_documents_controller.add_accountant_doc(file_data, accountantId, accountant,
                                                                                request.session.get('id'))

            url = reverse('update_accountant_documents', kwargs={'accountantId': accountantId})
            return redirect(url)
    else:
        return redirect('login')


def addLabTechnicianDocuments(request, LabTechnicianId):
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
                    file_name = f"{subdirectory}{file_key}_{int(time.time())}_{str(file_obj)}"
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
            lab_technician = lab_technician_model.lab_technician_model_from_dict(request.POST)
            response, status_code = add_documents_controller.add_lab_technician_doc(file_data, LabTechnicianId,
                                                                                    lab_technician,
                                                                                    request.session.get('id'))

            url = reverse('update_lab_technician_documents', kwargs={'labTechnicianId': LabTechnicianId})
            return redirect(url)
    else:
        return redirect('login')


def addMarketingHeadDocuments(request, marketingHeadId):
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
                    file_name = f"{subdirectory}{file_key}_{int(time.time())}_{str(file_obj)}"
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
            marketing_head = marketing_head_model.marketing_head_model_from_dict(request.POST)
            response, status_code = add_documents_controller.add_marketing_heads_doc(file_data, marketingHeadId,
                                                                                     marketing_head,
                                                                                     request.session.get('id'))

            url = reverse('update_marketing_head_documents', kwargs={'marketingHeadId': marketingHeadId})
            return redirect(url)
    else:
        return redirect('login')


def ViewAllEyeTest(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = eye_test_controller.get_eye_test()
        print(response)
        return render(request, 'indolens_admin/eyeTest/viewAllEyeTest.html',
                      {'eye_test_list': response['eye_test_list']})
    else:
        return redirect('login')


def getEyeTestById(request, testId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = eye_test_controller.get_eye_test_by_id(testId)
        return render(request, 'indolens_admin/eyeTest/viewAllEyeTest.html',
                      {'eye_test_list': response['eye_test']})

    else:
        return redirect('login')


def eyeTestPrint(request, testId):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        response, status_code = eye_test_controller.get_eye_test_by_id(testId)
        print(response)
        return render(request, 'indolens_admin/eyeTest/adminEyeTestPrint.html',
                      {'eye_test_list': response['eye_test']})

    else:
        return redirect('login')


def indolensAdminSetting(request):
    if request.session.get('is_admin_logged_in') is not None and request.session.get('is_admin_logged_in') is True:
        if request.method == 'POST':
            print(request.POST)
            response, status_code = admin_setting_controller.admin_setting(request.POST)
            print(response)
            return redirect('indolens_admin_setting')
        else:
            response, status_code = admin_setting_controller.get_admin_setting()
            print(response)
            return render(request, 'indolens_admin/settings/IndolensAdminSetting.html',
                          {"admin_setting": response['admin_setting']})

    else:
        return redirect('login')
