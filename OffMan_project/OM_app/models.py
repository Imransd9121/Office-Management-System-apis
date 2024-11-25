from django.db import models
from django.utils import timezone
from django.db import IntegrityError


# Create your models here.


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)  # Automatically set the date when created

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position}'
    
class Asset(models.Model):
    ASSET_TYPES = [
        ('Laptop', 'Laptop'),
        ('Phone', 'Phone'),
        ('Monitor', 'Monitor'),
        ('Mouse','Mouse'),
        ('Other', 'Other'),

    ]

    asset_id = models.AutoField(primary_key=True)
    # employee = models.ForeignKey(Employee,related_name='assets', on_delete=models.CASCADE)  
    asset_type = models.CharField(max_length=50, choices=ASSET_TYPES)  
    serial_number = models.CharField(max_length=100, unique=True) 
    asset_image = models.ImageField(upload_to='assets/', blank=True, null=True) 
      

    def __str__(self):
        return f'{self.asset_type} {self.serial_number}'

class EmployeeAsset(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_assets')
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE, related_name='assigned_employee')
    assigned_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now=False,blank=True, null=True)

    def save(self, *args, **kwargs):
        if 'update_fields' in kwargs and 'return_date' in kwargs['update_fields']:
        # Skip the asset assignment check when only updating the return_date
            super(EmployeeAsset, self).save(*args, **kwargs)
        else:
        # Perform the normal integrity check
            if self.asset_is_already_assigned_to_another_employee():
                raise IntegrityError(f"Asset {self.asset} is already assigned to another employee.")
            super(EmployeeAsset, self).save(*args, **kwargs)

class EmployeePayroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payrolls')  
    ctc = models.DecimalField(max_digits=12, decimal_places=2)  # Cost to Company (Annual)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Basic Salary (Monthly)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Bonus
    pf = models.DecimalField(max_digits=10, decimal_places=2)  # Provident Fund (Monthly Deduction)
    esi = models.DecimalField(max_digits=10, decimal_places=2)  # Employee State Insurance (Monthly Deduction)
    payment_date = models.DateField(default=timezone.now)  # Payment date
    is_paid = models.BooleanField(default=False)  # Status if the payment is done

    def total_deductions(self):
        """Calculate the total deductions including PF and ESI."""
        return self.pf + self.esi

    def total_salary(self):
        """Calculate the total salary considering deductions and bonuses."""
        total = self.basic_salary + (self.bonus or 0) - self.total_deductions()
        return total

    def __str__(self):
        return f'Payroll for {self.employee.first_name} {self.employee.last_name} on {self.payment_date}'
