from django.urls import path
from .views import *

urlpatterns = [
    # start
    path('', index, name='own_store_index'),
    # auth
    path('login/', login, name='own_store_login'),
    path('forgot_password/', forgotPassword, name='own_store_forgot_password'),
    path('reset_password/', resetPassword, name='own_store_reset_password'),
    # Dashboard
    path('dashboard/', dashboard, name='own_store_dashboard'),
]
