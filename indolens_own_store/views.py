# =================================ADMIN START======================================
from django.shortcuts import redirect, render


def index(request):
    return redirect('own_store_login')


# ================================= OWN STORE AUTH ======================================

def login(request):
    if request.method == 'POST':
        return redirect('own_store_dashboard')
    return render(request, 'auth/sign_in.html')


def forgotPassword(request):
    return render(request, 'auth/forgot_password.html')


def resetPassword(request):
    return render(request, 'auth/reset_password.html')


# ================================= OWN STORE DASHBOARD ======================================
def dashboard(request):
    return render(request, 'dashboard.html')
