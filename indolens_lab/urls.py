from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.checkLogin, name='entry'),
    path('lab_login/', login, name='lab_login'),
    path('lab_logout/', labLogout, name='lab_logout'),
    path('lab_forgot_password/', labForgotPassword, name='lab_forgot_password'),
    path('lab_reset_password/code=<str:code>', labResetPassword, name='lab_reset_password'),
    # Dashboard
    path('dashboard_lab/', labDashboard, name='dashboard_lab'),
    path('all_task/', allTask, name='all_task'),
    path('active_task_powers/', activeJobsPower, name='active_task_powers'),
    path('new_task/', newTask, name='new_task'),
    path('processing_task/', processingTask, name='processing_task'),
    path('ready_task/', readyTask, name='ready_task'),
    path('dispatched_task/', dispatchedTask, name='dispatched_task'),
    path('cancelled_task/', cancelledTask, name='cancelled_task'),
    path('lab_job_details/jobId=<str:jobId>', labJobDetails, name='lab_job_details'),
    path('lab_job_details/job_status_change/jobId=<str:jobId>/status=<str:status>', jobStatusChange,
         name='job_status_change'),
    path('my_profile/labTechnicianId=<int:labTechnicianId>', viewLabTechnician,
         name='my_profile'),

    path('view_products/productId=<int:productId>', viewLabCentralInventoryProducts,
         name='view_lab_central_inventory_products'),
    path('job_item_details/saleId=<str:saleId>', viewJobItemDetails,
         name='job_item_details'),
    path('job_authenticity_card/saleId=<str:saleId>/frame=<str:frame>', viewJobAuthenticityCard,
         name='job_authenticity_card'),
    path('contact_Lens_power_card/saleId=<str:saleId>', contactLensPowerCard,
         name='contact_Lens_power_card'),


]
