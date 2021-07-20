from django.shortcuts import render, redirect
from .forms import EmployeeForm, DepartmentForm, LeaveForm, DisciplinaryForm, SkillsForm, ProfileForm
from .models import Employee, Department, Leave, Skills, Disciplinary
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required(login_url='/accounts/login/')
def home(request):
	
	context ={
		'nav': 'home page',
		'title':'home page'
	}
	return render(request, 'employee/home.html', context)

@login_required(login_url='/accounts/login/')
def Addemployee(request):
	if request.method =='POST':
		form = EmployeeForm (request.POST)
		if form.is_valid():
			form.save()
			form = EmployeeForm()
			return redirect('listemployee')
	else:
		form = EmployeeForm ()
		context ={
			'nav': 'add employee',
			'title':'add employee',
			'form': form,
		}
		return render(request, 'employee/addemployee.html', context)

@login_required(login_url='/accounts/login/')
def AddDepartment(request):
	if request.method =='POST':
		form =  DepartmentForm (request.POST)
		if form.is_valid():
			form.save()
			form =  DepartmentForm()
			return redirect('listdepartment')
	else:
		form =  DepartmentForm ()
		context ={
			'nav': 'add department',
			'title':'add department',
			'form': form,
		}
	return render(request, 'employee/adddepartment.html', context)

@login_required(login_url='/accounts/login/')
def AddLeave(request):
	if request.method =='POST':
		form =  LeaveForm(request.POST)
		user = request.POST.get('user')
		if form.is_valid():
			form.save()
			form =  LeaveForm()
			return redirect('listleave')	
	else:
		form =  LeaveForm ()
		context ={
			'nav': 'add leave',
			'title':'add leave',
			'form': form,
		}
		return render(request, 'employee/addleave.html', context)

@login_required(login_url='/accounts/login/')
def AddDisciplinary(request):
	if request.method =='POST':
		form =   DisciplinaryForm (request.POST)
		if form.is_valid():
			form.save()
			form =   DisciplinaryForm()
			return redirect('listdisciplinary')	
	else:
		form =   DisciplinaryForm ()
		context ={
			'nav':'add disciplinary',
			'title':'add disciplinary',
			'form': form,
		}
		return render(request, 'employee/disciplinary.html', context)

@login_required(login_url='/accounts/login/')
def Addskills(request):
	if request.method =='POST':
		form =  SkillsForm (request.POST)
		if form.is_valid():
			form.save()
			form =  SkillsForm()
			return redirect('listskill')	
	else:
		form =  SkillsForm ()
		context ={
			'nav': 'add skill',
			'title':'add skills',
			'form': form,
		}
		return render(request, 'employee/skills.html', context)

@login_required(login_url='/accounts/login/')
def listemployee(request):
	allemployee =Employee.objects.all()
	context ={
		'nav': 'list of employee',
		'title':'list of employees',
		'allemployee': allemployee,
	}
	return render(request, 'employee/listemployee.html', context)


@login_required(login_url='/accounts/login/')
def updateemployee(request, id):
	obj = Employee.objects.get(id = id)
	if request.method =='POST':
		form =  EmployeeForm(request.POST or None, instance = obj)
		if form.is_valid:
			form.save()
			return redirect('listemployee')
	else:
		form =  EmployeeForm(request.POST or None, instance = obj)
		context ={
			'nav': 'update employee',
			'title':'update employee',
			'form': form,
			'obj': obj,
		}
	return render(request, 'employee/updateemployee.html', context)

@login_required(login_url='/accounts/login/')
def detailsemployee(request, id):
	obj = Employee.objects.get(id = id)
	context ={
		'nav': 'detail of employee',
		'title':'details of employee',
		'obj': obj,
	}
	return render(request, 'employee/detailsemployee.html', context)

@login_required(login_url='/accounts/login/')
def deleteemployee(request, id):
	obj = Employee.objects.get(id = id)
	if request.method =='POST':
		obj.delete()
		return redirect('listemployee')
	context ={
		'title':'delete employee',
		'obj': obj,
	}
	return render(request, 'employee/deleteemployee.html', context)

@login_required(login_url='/accounts/login/')
def listdepartment(request):
	listdepart = Department.objects.all()
	context ={
		'nav': 'list of departents',
		'title':'list of department',
		'listdepart': listdepart,
	}
	return render(request, 'employee/listdepartment.html', context)


@login_required(login_url='/accounts/login/')
def updatedepart(request, id):
	obj = Department.objects.get(id = id)
	if request.method == 'POST':
		form =DepartmentForm(request.POST or None, instance= obj)
		if form.is_valid:
			form.save()
			return redirect('listdepartment')
	else:
		form =DepartmentForm(request.POST or None, instance= obj)
		context ={
			'nav': 'update department',
			'title':'update department',
			'form':form,
			'obj':obj
		}
	return render(request, 'employee/updatedepart.html', context)

@login_required(login_url='/accounts/login/')
def deletedepart(request, id):
	obj = Department.objects.get(id = id)
	if request.method =='POST':
		obj.delete()
		return redirect('listdepartment')
	context ={
		'nav': 'delete department',
		'title':'delete department',
		'obj': obj,
	}
	return render(request, 'employee/deletedepartment.html', context)
	
@login_required(login_url='/accounts/login/')
def listleave(request):
	allleave = Leave.objects.all()
	context ={
	'nav': 'list of leave',
	'allleave': allleave,
	'title': 'list of leave',
	}
	return render(request, 'employee/listleave.html', context)


@login_required(login_url='/accounts/login/')
def updateleave(request, id):
	obj = Leave.objects.get(id = id)
	if request.method == 'POST':
		form = LeaveForm(request.POST or None, instance = obj)
		if form.is_valid():
			form.save()
			return redirect('listleave')
	else:
		form = LeaveForm(request.POST or None, instance = obj)
		context ={
			'nav': 'update leave',
			'title':'update leave',
			'form': form,
			'obj':obj,
		}
		return render(request, 'employee/updateleave.html', context)

@login_required(login_url='/accounts/login/')
def deleteleave(request, id):
	obj = Leave.objects.get(id = id)
	if request.method == 'POST':
		obj.delete()
		return redirect('listleave')
	context ={
		'nav': 'delete leave',
		'title':'delete leave',
		'obj':obj,
	}
	return render(request, 'employee/deleteleave.html', context)

@login_required(login_url='/accounts/login/')
def deleteskills(request, id):
	obj = Skills.objects.get(id = id)
	if request.method == 'POST':
		obj.delete()
		return redirect('listskill')
	context ={
		'nav': 'delete skills',
		'title':'delete skills',
		'obj':obj,
	}
	return render(request, 'employee/deleteskills.html', context)


@login_required(login_url='/accounts/login/')
def listSkills(request):
	listdis =Skills.objects.all()
	context={
		'nav': 'list of skills',
		'title': 'list of skills',
		'listdis': listdis,
	}
	return render(request, 'employee/listdis.html', context)

@login_required(login_url='/accounts/login/')
def listdicplinary(request):
	lisdisc = Disciplinary.objects.all()
	context ={
		'nav': 'list of discplinary',
		'title':'list discplinary',
		'lis': lisdisc
	}
	return render(request, 'employee/listdisciplinary.html', context)


@login_required(login_url='/accounts/login/')
def Useremployee(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			form = ProfileForm()
			return redirect('home')
	else:
		form = ProfileForm(instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'employee/editprofile.html', {'form': form})


@login_required(login_url='/accounts/login/')
def employeepage(request):
	x = Employee.objects.filter(user = request.user )
	y = Leave.objects.filter(user = request.user )
	z = Disciplinary.objects.filter(user = request.user )
	a = Skills.objects.filter(user = request.user )


	context ={
		'x':x,
		'y': y,
		'z' : z,
		'a': a,
	}
	return render(request, 'employee/employeepage.html', context)