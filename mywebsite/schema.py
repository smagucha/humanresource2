import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.mixins import LoginRequiredMixin
from employee.models import Employee, Leave, Disciplinary, Skills, Department
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import graphql_jwt
#from employee.enum import leavetype, approvement
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

SomeEnumSchema = graphene.Enum.from_enum(leavetype)
SomeEnumSchema2 = graphene.Enum.from_enum(approvement)

class UserType(DjangoObjectType):
    class Meta:
        model = User
        only_fields = ('id','username', 'first_name', 'last_name','email')

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = '__all__'


class LeaveType(DjangoObjectType):
    class Meta:
        model = Leave
        fields = '__all__'
        convert_choices_to_enum = True

class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department
        fields = '__all__'

class  DisciplinaryType(DjangoObjectType):
    class Meta:
        model = Disciplinary
        fields = '__all__'



class SkillsType(DjangoObjectType):
    class Meta:
        model = Skills
        fields = '__all__'

class Query(graphene.ObjectType):
    all_employee = graphene.List(EmployeeType)
    all_Leave = graphene.List(LeaveType)
    leave = graphene.Field(LeaveType, leave_id =graphene.Int())
    all_displinary = graphene.List(DisciplinaryType)
    all_skills = graphene.List(SkillsType)
    employee = graphene.Field(EmployeeType, employee_id =graphene.Int())
    me = graphene.Field(UserType)
    users = graphene.List(UserType)
    all_department = graphene.List(DepartmentType)
    department= graphene.Field(DepartmentType, department_id = graphene.Int())
    
    def resolve_all_department(root, info):
        return Department.objects.all()

    def resolve_department(self, info, department_id):
        return Department.objects.get(pk=department_id)

    def resolve_all_employee(root, info):
        # We can easily optimize query count in the resolve method
        return Employee.objects.all()

    def resolve_employee(self, info, employee_id):
        return Employee.objects.get(pk=employee_id)

    def resolve_all_Leave(root, info):
        # We can easily optimize query count in the resolve method
        return Leave.objects.all()

    def resolve_leave(self, info, leave_id):
        return Leave.objects.get(pk=leave_id)

    def resolve_all_discplinary(root, info):
        # We can easily optimize query count in the resolve method
        return Disciplinary.objects.all()

    def resolve_all_skills(root, info):
        # We can easily optimize query count in the resolve method
        return Skills.objects.all()

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure!')
        return user


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,

        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class UpdateUser(graphene.Mutation):

    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.ID()
        username = graphene.String(required=True)
        first_name =graphene.String(required=True)
        last_name =graphene.String(required=True)
        email = graphene.String(required=True)

    @staticmethod
    def mutate(self, root, id, username, first_name,last_name, email):
        user_instance = User.objects.get(pk=id)
        if user_instance:
            user_instance.id = id
            user_instance.username = username
            user_instance.first_name = first_name
            user_instance.last_name = last_name
            user_instance.email =email
            user_instance.save()
            return UpdateUser(user=user_instance)
        return UpdateUser(user=None)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    users = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id):
        user_instance = User.objects.get(pk=id)
        user_instance.delete()
        return None



class CreateEmployee(graphene.Mutation):

    class Arguments:
        user_id =graphene.Int()
        EmployeeNo = graphene.Int()
        Nhif = graphene.String()
        DOE = graphene.Date()
        IDNO= graphene.Int()
        Jobtitle = graphene.String()
        PassportNo=graphene.String()
        Homecounty=graphene.String()
        Countyresidence=graphene.String()
        salary = graphene.Int()

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(self, root, info, user_id,EmployeeNo,Nhif,DOE ,IDNO,Jobtitle ,PassportNo,Homecounty,Countyresidence,salary):
        employee_instance= Employee( 
            user_id = user_id,
            EmployeeNo = EmployeeNo,
            Nhif = Nhif,
            DOE =DOE,
            IDNO= IDNO,
            Jobtitle =Jobtitle,
            PassportNo=PassportNo,
            Homecounty=Homecounty,
            Countyresidence=Countyresidence,
            salary =salary,
        )
        employee_instance.save()
        return CreateEmployee(employee=employee_instance)

class UpdateEmployee(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        user_id =graphene.ID()
        EmployeeNo = graphene.Int()
        Nhif = graphene.String()
        DOE = graphene.Date()
        IDNO= graphene.Int()
        Jobtitle = graphene.String()
        PassportNo=graphene.String()
        Homecounty=graphene.String()
        Countyresidence=graphene.String()
        salary = graphene.Int()

    employee = graphene.Field(EmployeeType)

    @staticmethod
    def mutate(root, info, id,user_id,EmployeeNo,Nhif,DOE ,IDNO,Jobtitle ,PassportNo,Homecounty,Countyresidence,salary):
        employee_instance = Employee.objects.get(pk=id)
        if employee_instance:
            employee_instance.user_id = user_id
            employee_instance.EmployeeNo = EmployeeNo
            employee_instance.Nhif = Nhif
            employee_instance.DOE =DOE
            employee_instance.IDNO= IDNO
            employee_instance.Jobtitle =Jobtitle
            employee_instance.PassportNo=PassportNo
            employee_instance.Homecounty=Homecounty
            employee_instance.Countyresidence=Countyresidence
            employee_instance.salary =salary
            employee_instance.save()
            return UpdateEmployee(employee=employee_instance)
        return UpdateEmployee(employee=None)

class DeleteEmployee(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    employee = graphene.Field(EmployeeType)

    @staticmethod
    def mutate(root, info, id):
        employee_instance = Employee.objects.get(pk=id)
        employee_instance.delete()
        return None


class CreateSkills(graphene.Mutation):
    class Arguments:
        user_id =graphene.Int()
        description = graphene.String()

    skills = graphene.Field(SkillsType)

    def mutate(self, root, user_id, description):
        skills_instance = Skills(
            user_id = user_id,
            description = description
            )
        skills_instance.save()
        return CreateSkills(skills = skills_instance)

class UpdateSkills(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        user_id =graphene.Int()
        description = graphene.String()

    skills = graphene.Field(SkillsType)

    def mutate(self, root, id, user_id, description):
        skills_instance = Skills.objects.get(pk=id)
        if skills_instance:
            skills_instance.id = id
            skills_instance.user_id = user_id
            skills_instance.description = description
            skills_instance.save()
            return UpdateSkills(skills=skills_instance)
        return UpdateSkills(skills=None)

class DeleteSkills(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    skills = graphene.Field(SkillsType)

    @staticmethod
    def mutate(root, info, id):
        skills_instance = Skills.objects.get(pk=id)
        skills_instance.delete()
        return None

class Createdepartment(graphene.Mutation):

    class Arguments:
        name = graphene.String()

    deparment = graphene.Field(DepartmentType)

    def mutate(self, root, name):
        department_instance = Department(
            name = name,
            )
        department_instance.save()
        return Createdepartment(department = department_instance)

class UpdateDepartment(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        Name = graphene.String()

    department = graphene.Field(DepartmentType)

    def mutate(self, root, id, Name):
        department_instance = Department.objects.get(pk=id)
        if department_instance:
            department_instance.id = id
            department_instance.Name = Name
            department_instance.save()
            return UpdateDepartment(department=department_instance)
        return UpdateDepartment(department=None)

class DeleteDepartment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    department = graphene.Field(SkillsType)

    @staticmethod
    def mutate(root, info, id):
        department_instance = Department.objects.get(pk=id)
        department_instance.delete()
        return None

class CreateDisciplinary(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int()
        description = graphene.String()

    disciplinary = graphene.Field(DisciplinaryType)

    def mutate(self, info, user_id, description):
        disciplinary_instance = Disciplinary(
            user_id = user_id,
            description = description
            )
        disciplinary_instance.save()
        return CreateDisciplinary(disciplinary=disciplinary_instance)
class UpdateDisciplinary(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        user_id = graphene.Int()
        description = graphene.String()

    disciplinary = graphene.Field(DisciplinaryType)

    def mutate(self, root,id, user_id, description):
        disciplinary_instance = Disciplinary.objects.get(pk=id)
        if disciplinary_instance:
            disciplinary_instance.id = id
            disciplinary_instance.user_id = user_id
            disciplinary_instance.description = description
            disciplinary_instance.save()
            return UpdateDisciplinary(disciplinary=disciplinary_instance)
        return UpdateDisciplinary(disciplinary=None)


class DeleteDisciplinary(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    disciplinary = graphene.Field(DisciplinaryType)

    @staticmethod
    def mutate(root, info, id):
        disciplinary_instance = Disciplinary.objects.get(pk=id)
        disciplinary_instance.delete()
        return None

class CreateLeave(graphene.Mutation):

    class Arguments:
        user_id = graphene.Int()
        typeofleave = graphene.String(required = True)
        leavedatesapplied = graphene.Int()
        Dateofleaveapplied = graphene.Date()
        approved = graphene.String(required = True)

    leave = graphene.Field(LeaveType)

    def mutate(self, info, user_id,typeofleave,leavedatesapplied, Dateofleaveapplied,approved):
        leave_instance = Leave(
        user_id = user_id,
        typeofleave = typeofleave,
        leavedatesapplied = leavedatesapplied,
        Dateofleaveapplied =Dateofleaveapplied,
        approved = approved,
            )
        leave_instance.save()
        return CreateLeave(leave=leave_instance)
class DeleteLeave(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    leave = graphene.Field(LeaveType)

    @staticmethod
    def mutate(root, info, id):
        leave_instance = Leave.objects.get(pk=id)
        leave_instance.delete()
        return None

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()
    create_department = Createdepartment.Field()
    update_department = UpdateDepartment.Field()
    delete_department = DeleteDepartment.Field()
    create_skills = CreateSkills.Field()
    update_skills = UpdateSkills.Field()
    delete_skills = DeleteSkills.Field()
    create_disciplinary = CreateDisciplinary.Field()
    update_disciplinary = UpdateDisciplinary.Field()
    delete_disciplinary = DeleteDisciplinary.Field()
    create_leave = CreateLeave.Field()
    delete_leave =DeleteLeave.Field()

schema = graphene.Schema(query=Query, mutation = Mutation)



# mutation createMutation {
#   createEmployee(
#         userId: 8,
#       EmployeeNo: 12345,
#       Nhif : "jgdsf546",
#       DOE : "1971-11-30",
#       IDNO: 45646,
#       Jobtitle : "financial officer",
#       PassportNo: "passport01",
#       Homecounty: "lodwar",
#       Countyresidence: "london",
#       salary : 305878947,
#     ) {
#     employee {
#       user{
#         username
#       },
#       EmployeeNo ,
#       Nhif, 
#       DOE,
#       IDNO,
#       Jobtitle,
#       PassportNo,
#       Homecounty,
#       Countyresidence,
#       salary,
#     }
#   }
# }

#   }
# }


# mutation updateMutation {
#   updateEmployee(
#       id: 2,
#             userId:2,
#         EmployeeNo: 12345,
#       Nhif : "Nhif001",
#       DOE : "1971-11-30",
#       IDNO: 45646,
#       Jobtitle : "financial officer",
#       PassportNo: "passport01",
#       Homecounty: "lodwar",
#       Countyresidence: "london",
#       salary : 10000,
      
#   ){
#    employee{
#         id,
#         user{
#         id,
#         username,
#       }
#       EmployeeNo ,
#       Nhif, 
#       DOE,
#       IDNO,
#       Jobtitle,
#       PassportNo,
#       Homecounty,
#       Countyresidence,
#       salary,
#     }
#   }
    
# }
# mutation{
#   deleteSkills(id:5){
#     skills{
#       id
#     }
#   }
# }