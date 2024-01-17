from django.urls import path

from . import views
from .views import login, labDashboard, allTask

urlpatterns = [
    path('', views.checkLogin, name='entry'),
    path('login/', login, name='lab_login'),
    # Dashboard
    path('dashboard/', labDashboard, name='dashboard_lab'),
    path('all_task/', allTask, name='all_task'),

]
