from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','gender','role']
    search_fields = ['name','phone','email']
    list_filter = ['gender','role']
    list_per_page = 10

admin.site.register(Employee,EmployeeAdmin)
