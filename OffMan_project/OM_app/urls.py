from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
   path('EmployeesList/',EmployeeList.as_view(),name='employees'),
   path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
   # path('employees/create/', EmployeeCreate.as_view(), name='employee-create'),
   path('assets/', AssetListCreate.as_view(), name='asset-list-create'),
   path('assets/update/<int:asset_id>/', AssetUpdateAPIView.as_view(), name='asset-update'),
   path('EmpPayRoll/', EmployeePayrollListCreate.as_view(), name='PayRoll'),
   path('Emp_Assets/',EmployeeAssetList.as_view(),name='emp_assets'),
   # path('Emp_Asset/update/<int:pk>',EmployeeAssetUpdateAPIView.as_view(),name='emp_asset_update')
   # path('employee-assets/<int:pk>/', EmployeeAssetUpdate.as_view(), name='employee-asset-update'),
   
]