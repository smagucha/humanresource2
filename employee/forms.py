from .models import  Employee, Department, Leave, Disciplinary, Skills
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
	class Meta:
		model =User
		fields= ['username', 'email', 'first_name' ,'last_name']


class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields ='__all__'
		widgets = {
	            'DOE': DateInput(),
	        }

class DepartmentForm(ModelForm):
	class Meta:
		model = Department
		fields ='__all__'


class LeaveForm(ModelForm):
	class Meta:
		model = Leave
		exclude =['approved', 'leavedays', 'remainingdays']

		widgets = {
            'Dateofleaveapplied': DateInput(),
        }
        
class DisciplinaryForm(ModelForm):
	class Meta:
		model = Disciplinary
		fields ='__all__'

class SkillsForm(ModelForm):
	class Meta:
		model = Skills
		fields ='__all__'

