from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, unique = True)
	EmployeeNo = models.PositiveIntegerField()
	Nhif = models.CharField(max_length =50)
	DOE = models.DateField()
	IDNO= models.IntegerField()
	Jobtitle = models.CharField(max_length =50)
	PassportNo=models.CharField(max_length =50)
	Homecounty=models.CharField(max_length =50)
	Countyresidence=models.CharField(max_length =50)
	salary = models.IntegerField()

	def __Str__(self):
		return self.user


class Department(models.Model):
	Name = models.CharField(max_length= 50)



class Leave(models.Model):

	Sick = 'sick'
	Maternity = 'Maternity'
	Paternity = 'Paternity'
	bereavement = 'bereavement'
	Compassionate = 'bereavement'
	unpaid = 'unpaid'
	Annual= 'Annual'
	approved = 'approved'
	notapproved = 'notapproved'

	leavetype =(
  		(Annual,'Annual'),
  		(Sick , 'sick'),
		(Maternity , 'Maternity'),
		(Paternity , 'Paternity'),
		(bereavement , 'bereavement'),
		(Compassionate , 'bereavement'),
		(unpaid , 'unpaid'),
	)

	approvement =(
		
		(approved, 'approved'),
  		(notapproved, 'notapproved'),
		)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	typeofleave = models.CharField(
		max_length=12,
		choices=leavetype,
		default=Annual,
		blank = True,
		null = True,
    )
	leavedatesapplied = models.PositiveIntegerField()
	Dateofleaveapplied =  models.DateField()
	approved = models.CharField(
		max_length=11,
		choices=approvement,
		default=notapproved,
		blank = True,
		null = True,
    )


	# def get_remainingday(self):

	# 	leavedays = self.leavedays
	# 	leavedatesapplied = self.leavedatesapplied
	# 	remaining = leavedays - leavedatesapplied
	# 	return remaining


	# def save(self, *args, **kwargs):
	# 	self.remainingdays = self.get_remainingday()
	# 	super(Leave, self).save(*args, **kwargs)


class Disciplinary(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()

	class Meta:
		verbose_name_plural = "Disciplinaries"

class Skills(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()

	class Meta:
		verbose_name_plural = "skills"

	
