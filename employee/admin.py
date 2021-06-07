from django.contrib import admin
#from cookbook.ingredients.models import Category, Ingredient

from employee.models import Employee, Department, Leave, Disciplinary, Skills






admin.site.register(Department)
admin.site.register(Leave)
admin.site.register(Disciplinary)
admin.site.register(Skills)



class EmployeeAdmin(admin.ModelAdmin):
	
    list_display = ['user', 'EmployeeNo', 'Nhif','salary']
    search_fields=[ 'EmployeeNo', 'Nhif','salary']


admin.site.register(Employee, EmployeeAdmin)



