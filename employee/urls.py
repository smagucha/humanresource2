from django.urls import path
from . import views
urlpatterns =[
	path('', views.home, name ='home'),
	path('addemployee', views.Addemployee, name='addemployee'),
	path('addDepartment', views.AddDepartment, name='addDepartment'),
	path('addleave', views.AddLeave, name ='addleave'),
	path('Adddisciplinary', views.AddDisciplinary, name='Adddisciplinary'),
	path('skills', views.Addskills, name ='addskills'),
	path('listemployee', views.listemployee, name='listemployee'),
	path('updateemployee/<int:id>', views.updateemployee, name='updateemployee'),
	path('detailsemployee/<int:id>', views.detailsemployee, name='detailsemployee'),
	path('deleteemployee/<int:id>', views.deleteemployee, name='deleteemployee'),
	path('deleteskills/<int:id>', views.deleteskills, name='deleteskill'),
	path('listdepart', views.listdepartment, name='listdepartment'),
	path('updatedepart/<int:id>', views.updatedepart, name='updatedepart'),
	path('deletedepart/<int:id>', views.deletedepart, name='deletedepart'),
	path('listleave', views.listleave, name='listleave'),
	path('updateleave/<int:id>', views.updateleave, name='updateleave'),
	path('deleteleave/<int:id>', views.deleteleave, name='deleteleave'),
	path('listskill', views.listSkills, name='listskill'),
	path('listdisciplinary', views.listdicplinary, name='listdisciplinary'),
	path('Useremployee', views.Useremployee, name='Useremployee'),
	path('employeepage', views.employeepage, name='employeepage')
	]

	