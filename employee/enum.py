from enum import Enum

class leavetype (Enum):   # A subclass of Enum
	Sick = 'sick'
	Maternity = 'Maternity'
	Paternity = 'Paternity'
	bereavement = 'bereavement'
	Compassionate = 'bereavement'
	unpaid = 'unpaid'
	Annual= 'Annual'
	approved = 'approved'
	notapproved = 'notapproved'


class approvement(Enum):
	approved ='approved'
	notapproved ='notapproved'
