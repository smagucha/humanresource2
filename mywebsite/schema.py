import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.mixins import LoginRequiredMixin
from employee.models import Employee, Leave, Disciplinary, Skills
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import graphql_jwt

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = '__all__'


class LeaveType(DjangoObjectType):
    class Meta:
        model = Leave
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
    all_displinary = graphene.List(DisciplinaryType)
    all_skills = graphene.List(SkillsType)
    employee = graphene.Field(EmployeeType, employee_id =graphene.Int())
    user=graphene.List(UserType)
 
    def resolve_all_employee(root, info):
        # We can easily optimize query count in the resolve method
        return Employee.objects.all()

    def resolve_employee(self, info, employee_id):
        return Employee.objects.get(pk=employee_id)

    def resolve_Leave(root, info):
        # We can easily optimize query count in the resolve method
        return Leave.objects.all()

    def resolve_all_discplinary(root, info):
        # We can easily optimize query count in the resolve method
        return Disciplinary.objects.all()

    def resolve_all_skills(root, info):
        # We can easily optimize query count in the resolve method
        return Skills.objects.all()

    def resolve_users(root, info):
        return User.objects.all()

    # def resolve_me(self, info):
    #     user = info.context.user
    #     if user.is_anonymous:
    #         raise Exception('Authentication Failure!')
    #     return user




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

# class LeaveMutation(graphene.Mutation) :
# 	class Arguments:
# 		name = graphene.String(required = True)

# 	leave = graphene.Field(LeaveType)

# 	@classmethod
# 	def mutate(root, info, name):
# 		leave =Leave(name = name)
# 		leave.save()
# 		return LeaveMutation(leave = leave)

# class Mutation(graphene.ObjectType):
# 	update_leave = LeaveMutation.Field()


# class EmployeeInput(graphene.InputObjectType):
#     user =graphene.ID()
#     EmployeeNo = graphene.Int()
#     Nhif = graphene.String()
#     DOE = graphene.Date()
#     IDNO= graphene.Int()
#     Jobtitle = graphene.String()
#     PassportNo=graphene.String()
#     Homecounty=graphene.String()
#     Countyresidence=graphene.String()
#     salary = graphene.Int()

# class CreateEmployee(graphene.Mutation):
#     class Arguments:
#         employee_data = EmployeeInput(required=True)

#     employee = graphene.Field(EmployeeType)

#     @staticmethod
#     def mutate(root, info, employee_data=None):
#         employee_instance = Employee( 
#             user_id =User.objects.get(id = employee_data.user),
#             user = employee_data.user_id,
#             EmployeeNo = employee_data.EmployeeNo,
#             Nhif = employee_data.Nhif,
#             DOE = employee_data.DOE,
#             IDNO= employee_data.IDNO,
#             Jobtitle = employee_data.Jobtitle,
#             PassportNo=employee_data.PassportNo,
#             Homecounty=employee_data.Homecounty,
#             Countyresidence=employee_data.Countyresidence,
#             salary = employee_data.salary
#         )
#         employee_instance.save()
#         return CreateEmployee(employee=employee_instance)

# class UpdateEmployee(graphene.Mutation):
#     class Arguments:
#         employee_data = EmployeeInput(required=True)

#     employee = graphene.Field(EmployeeType)

#     @staticmethod
#     def mutate(root, info, employee_data=None):

#         employee_instance = Employee.objects.get(pk=employee_data.id)

#         if employee_instance:
#             user = employee_data.user,
#             EmployeeNo = employee_data.EmployeeNo,
#             Nhif = employee_data.Nhif,
#             DOE = employee_data.DOE,
#             IDNO= employee_data.IDNO,
#             Jobtitle = employee_data.Jobtitle,
#             PassportNo=employee_data.PassportNo,
#             Homecounty=employee_data.Homecounty,
#             Countyresidence=employee_data.Countyresidence,
#             salary = employee_data.salary
#             employee_instance.save()

#             return UpdateEmployee(employee=employee_instance)
#         return UpdateEmployee(employee=None)


# class DeleteEmployee(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()

#     employee = graphene.Field(EmployeeType)

#     @staticmethod
#     def mutate(root, info, id):
#         employee_instance = Employee.objects.get(pk=id)
#         employee_instance.delete()

#         return None

class UserInput(graphene.InputObjectType):
    username = graphene.String()
  

class EmployeeInput(graphene.InputObjectType):
    user=graphene.String()
    EmployeeNo = graphene.Int()
    Nhif = graphene.String()
    DOE = graphene.Date()
    IDNO= graphene.Int()
    Jobtitle = graphene.String()
    PassportNo=graphene.String()
    Homecounty=graphene.String()
    Countyresidence=graphene.String()
    salary = graphene.Int()

class CreateEmployee(graphene.Mutation):

    class Arguments:
        employee_data = EmployeeInput(required=True)

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(self,root, info, employee_data=None):
        employee_instance= Employee( 
            user =employee_data.user,
            EmployeeNo = employee_data.EmployeeNo,
            Nhif = employee_data.Nhif,
            DOE =employee_data.DOE,
            IDNO= employee_data.IDNO,
            Jobtitle =employee_data.Jobtitle,
            PassportNo=employee_data.PassportNo,
            Homecounty=employee_data.Homecounty,
            Countyresidence=employee_data.Countyresidence,
            salary =employee_data.salary
        )
        employee_instance.save()
        return CreateEmployee(employee=employee_instance)






class Mutation(graphene.ObjectType):
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()
    create_employee = CreateEmployee.Field()
    create_user = CreateUser.Field()
    #update_employee = UpdateEmployee.Field()
    #delete_employee = DeleteEmployee.Field()

schema = graphene.Schema(query=Query, mutation = Mutation)




# mutation createMutation {
#   createEmployee(
#     employeeData: {
#       user : "4",
#       EmployeeNo: 45446,
#       Nhif : "bvn1231",
#       DOE : "1992-01-02",
#       IDNO: 45646,
#       Jobtitle : "web designer",
#       PassportNo: "fcgvbk",
#       Homecounty: "kisumu",
#       Countyresidence: "Mombasa",
#       salary : 120000,
#     }) {
#     employee {
#       user,
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

# mutation createMutation {
#   createEmployee(
#     id: 5,
#     EmployeeNo: 4474798, 
#     Nhif: "svdvjk", 
#     DOE: "1992-05-05",
#     IDNO: 5631, 
#     Jobtitle: "hello world", 
#     PassportNo: "sdfl",
#     Homecounty: "Kisii", 
#     Countyresidence: "Nairobi",
#     salary: 12000
#    ) {
#     employee {
#       id
#       EmployeeNo
#       Nhif
#       DOE
#       IDNO
#       Jobtitle
#       PassportNo
#       Homecounty
#       Countyresidence
#       salary
#     }
#   }
# }
