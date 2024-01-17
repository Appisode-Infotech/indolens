from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.reverse import reverse

from indolens_lab.lab_controllers import lab_auth_controller, lab_task_controller
from indolens_lab.lab_models.request_model import lab_tech_model


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
    if request.session.get('is_store_logged_in') is not None and request.session.get('is_store_logged_in') is True:
        print(request.session.get('id'))
        assigned_lab = lab_auth_controller.get_assigned_lab(request.session.get('id'))
        print(assigned_lab)
        print("++++++++++++++++++++++++++++++++++++++++++")
        if assigned_lab == 0:
            request.session.clear()
            return assigned_lab
        else:
            return assigned_lab
    else:
        return redirect('login')


def labDashboard(request):
    return render(request, 'lab_dashboard.html')


def allTask(request):
    assigned_lab = getAssignedLab(request)
    print(assigned_lab)
    print("================================================")
    all_task, task_status_code = lab_task_controller.get_all_lab_task(assigned_lab)
    print(all_task)
    return render(request, 'Tasks/viewAllTask.html', {"all_task": all_task['task_list']})
