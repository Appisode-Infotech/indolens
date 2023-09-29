"""indolens URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls.static import static

from indolens import settings

urlpatterns = [
    path('', include('front_end_website.urls')),
    path('accountant/', include('indolens_accountant.urls')),
    # admin ui done
    path('admin/', include('indolens_admin.urls')),
    path('area_head/', include('indolens_area_head.urls')),
    path('employee/', include('indolens_employee.urls')),
    # franchise store ui done
    path('franchise_store/', include('indolens_franchise_store.urls')),
    path('lab/', include('indolens_lab.urls')),
    path('marketing_head/', include('indolens_marketing_head.urls')),
    # own store ui done
    path('own_store/', include('indolens_own_store.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

