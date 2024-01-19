from django.urls import path

from . import views
from .views import login, labDashboard, allTask, labJobDetails, jobStatusChange

urlpatterns = [
    path('', views.checkLogin, name='entry'),
    path('lab_login/', login, name='lab_login'),
    # Dashboard
    path('dashboard/', labDashboard, name='dashboard_lab'),
    path('all_task/', allTask, name='all_task'),
    path('lab_job_details/jobId=<str:jobId>', labJobDetails, name='lab_job_details'),
    path('lab_job_details/job_status_change/jobId=<str:jobId>/status=<str:status>', jobStatusChange,
         name='job_status_change'),

]
