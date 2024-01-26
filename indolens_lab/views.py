from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.reverse import reverse

from indolens_admin.admin_controllers import orders_controller
from indolens_lab.lab_controllers import lab_auth_controller, lab_task_controller
from indolens_lab.lab_models.request_model import lab_tech_model
from indolens_own_store.own_store_controller import store_orders_controller


def checkLogin(request):  # new
    return HttpResponse('<h1>WELCOME INDOLENS LAB</h1>')


def login(request):
    if request.method == 'POST':
        lab_obj = lab_tech_model.lab_technician_model_from_dict(request.POST)
        response, status_code = lab_auth_controller.lab_login(lab_obj)
        if response['status']:
            request.session.clear()
            for data in response['lab_tech']:
                request.session.update({
                    'is_lab_tech_logged_in': True,
                    'id': data['lab_technician_id'],
                    'name': data['name'],
                    'email': data['email'],
                    'lab_name': data['lab_name'],
                    'profile_pic': data['profile_pic'],
                })
            return redirect('dashboard_lab')
        else:
            return render(request, 'auth/lab_sign_in.html', {"message": response['message']})
    else:
        return render(request, 'auth/lab_sign_in.html')


def getAssignedLab(request):
    if request.session.get('is_lab_tech_logged_in') is not None and request.session.get('is_lab_tech_logged_in') is True:
        assigned_lab = lab_auth_controller.get_assigned_lab(request.session.get('id'))
        if assigned_lab == 0:
            request.session.clear()
            return assigned_lab
        else:
            return assigned_lab
    else:
        return redirect('lab_login')


def labDashboard(request):
    return render(request, 'lab_dashboard.html')


def allTask(request):
    assigned_lab = getAssignedLab(request)
    if request.session.get('is_lab_tech_logged_in') is not None and request.session.get(
            'is_lab_tech_logged_in') is True:
        all_task, task_status_code = lab_task_controller.get_lab_jobs(assigned_lab, "All")
        return render(request, 'Tasks/viewAllTask.html', {"all_task": all_task['task_list']})
    else:
        return redirect('lab_login')

def newTask(request):
    assigned_lab = getAssignedLab(request)
    if request.session.get('is_lab_tech_logged_in') is not None and request.session.get(
            'is_lab_tech_logged_in') is True:
        all_task, task_status_code = lab_task_controller.get_lab_jobs(assigned_lab, "New")
        return render(request, 'Tasks/viewNewTask.html', {"all_task": all_task['task_list']})
    else:
        return redirect('lab_login')

def processingTask(request):
    assigned_lab = getAssignedLab(request)
    if request.session.get('is_lab_tech_logged_in') is not None and request.session.get(
            'is_lab_tech_logged_in') is True:
        all_task, task_status_code = lab_task_controller.get_lab_jobs(assigned_lab, "Processing")
        return render(request, 'Tasks/viewProcessingTask.html', {"all_task": all_task['task_list']})
    else:
        return redirect('lab_login')

def readyTask(request):
    assigned_lab = getAssignedLab(request)
    if request.session.get('is_lab_tech_logged_in') is not None and request.session.get(
            'is_lab_tech_logged_in') is True:
        all_task, task_status_code = lab_task_controller.get_lab_jobs(assigned_lab, "Ready")
        return render(request, 'Tasks/viewReadyTask.html', {"all_task": all_task['task_list']})
    else:
        return redirect('lab_login')
def dispatchedTask(request):
    assigned_lab = getAssignedLab(request)
    if request.session.get('is_lab_tech_logged_in') is not None and request.session.get(
            'is_lab_tech_logged_in') is True:
        all_task, task_status_code = lab_task_controller.get_lab_jobs(assigned_lab, "Dispatched")
        return render(request, 'Tasks/viewDispatchedTask.html', {"all_task": all_task['task_list']})
    else:
        return redirect('lab_login')

def labJobDetails(request, jobId):
    assigned_lab = getAssignedLab(request)
    if request.session.get('is_lab_tech_logged_in') is not None and request.session.get(
            'is_lab_tech_logged_in') is True:
        job_detail, status_code = lab_task_controller.get_lab_job_details(jobId, assigned_lab)
        return render(request, 'Tasks/jobDetails.html', {"order_detail": job_detail['orders_details']})
    else:
        return redirect('lab_login')


def jobStatusChange(request, jobId, status):
    assigned_lab = getAssignedLab(request)
    if request.session.get('is_lab_tech_logged_in') is not None and request.session.get(
            'is_lab_tech_logged_in') is True:
        order_update, status_code = store_orders_controller.order_status_change(jobId, status)
        url = reverse('lab_job_details', kwargs={'jobId': jobId})
        return redirect(url)
    else:
        return redirect('lab_login')
