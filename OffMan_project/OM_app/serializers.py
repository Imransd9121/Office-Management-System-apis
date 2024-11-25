from rest_framework import serializers
from .models import *

class AssetSerializer(serializers.ModelSerializer):
    
    class Meta():
        model=Asset
        fields='__all__'


class PayrollSerializer(serializers.ModelSerializer):
    total_deductions = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    class Meta:
        model = EmployeePayroll
        fields = ['employee', 'ctc', 'basic_salary', 'bonus', 'pf', 'esi', 'payment_date', 'is_paid', 'total_deductions', 'total_salary']

    def get_total_deductions(self, obj):
        
        return obj.total_deductions()

    def get_total_salary(self, obj):
        
        return obj.total_salary()
    


class EmployeeAssetSerializer(serializers.ModelSerializer):
    
    class Meta():
        model=EmployeeAsset
        fields = ['id', 'return_date', 'employee', 'asset', 'assigned_date']  # Full fields
        
        # Set employee and asset as read-only to prevent updates
        extra_kwargs = {
            'employee': {'read_only': True},
            'asset': {'read_only': True},
            'assigned_date': {'read_only': True},
            'return_date': {'required': False},
        }

    # def update(self, instance, validated_data):
    #     # Only update the return_date if it's provided
    #     return_date = validated_data.get('return_date', None)

    #     if return_date:
    #         instance.return_date = return_date
    #         instance.save()

    #     return instance

class EmployeeSerializer(serializers.ModelSerializer):
    # assets = AssetSerializer(many=True, read_only=True)
    employee_assets=EmployeeAssetSerializer(many=True,read_only=True)
    assigned_employee = EmployeeAssetSerializer(many=True, read_only=True)
    payrolls=PayrollSerializer(many=True,read_only=True)
    class Meta():
        model=Employee
        # fields = ['emp_id', 'first_name', 'last_name', 'email', 'position', 'assets'] 
        fields='__all__'




