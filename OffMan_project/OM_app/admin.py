from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Employee)
admin.site.register(Asset)
admin.site.register(EmployeePayroll)
admin.site.register(EmployeeAsset)
