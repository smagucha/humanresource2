from django.contrib import admin
from django.contrib import admin
from employee.models import Employee, Department, Leave, Disciplinary, Skills

class EmployeeAdmin(admin.ModelAdmin):
	
    list_display = ['user', 'EmployeeNo', 'Nhif','salary']
    search_fields=[ 'EmployeeNo', 'Nhif','salary']
admin.site.register(Employee, EmployeeAdmin)

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ['user', 'typeofleave','Dateofleaveapplied','leavedatesapplied','approved']
    search_fields= ['user', 'typeofleave','Dateofleaveapplied','leavedatesapplied','approved']
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display =['Name']
    search_fields = ['Name']
    
@admin.register(Disciplinary)
class DisciplinaryAdmin(admin.ModelAdmin):
    list_display =['user', 'description']
    search_fields = ['user', 'description']


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display =['user', 'description']
    search_fields = ['user', 'description']


     

