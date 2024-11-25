from django.shortcuts import render,HttpResponse
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date


# Create your views here.
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()  
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()  
    serializer_class = EmployeeSerializer  
    lookup_field = 'pk' 

class AssetListCreate(generics.ListCreateAPIView):
    queryset = Asset.objects.all()  
    serializer_class = AssetSerializer 

class AssetUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()  
    serializer_class = AssetSerializer  
    lookup_field = 'asset_id' 

class EmployeePayrollListCreate(generics.ListCreateAPIView):
    queryset = EmployeePayroll.objects.all()  
    serializer_class = PayrollSerializer 

class EmployeeAssetList(generics.ListCreateAPIView):
    queryset=EmployeeAsset.objects.all()
    serializer_class=EmployeeAssetSerializer

# class EmployeeAssetUpdate(generics.RetrieveUpdateAPIView):
#     queryset = EmployeeAsset.objects.all()
#     serializer_class = EmployeeAssetSerializer

#     def perform_update(self, serializer):
#         # Only update return_date without triggering any asset validation
#         serializer.save(update_fields=['return_date'])



