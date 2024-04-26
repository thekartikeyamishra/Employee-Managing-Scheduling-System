"""
URL configuration for employee_scheduler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from . import views  
from apps.employees import views as employee_views
from apps.shifts import views as shift_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('some_view/', views.some_view, name='some_view'),

    # Employee API endpoints
    path('employees/', employee_views.EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', employee_views.EmployeeDetail.as_view(), name='employee-detail'),

    # Shift API endpoints
    path('shifts/', shift_views.ShiftList.as_view(), name='shift-list'),
    path('shifts/<int:pk>/', shift_views.ShiftDetail.as_view(), name='shift-detail'),

    # Additional API endpoints for prediction or scheduling (to be implemented)
    path('predict/traffic/', YourPredictionView.as_view(), name='predict-traffic'),
    path('schedule/dynamic/', YourSchedulingView.as_view(), name='schedule-dynamic'),
]
