import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.mixins import LoginRequiredMixin
from employee.models import Employee, Leave, Disciplinary, Skills
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import graphql_jwt
# import users.schema
# import tracks.schema

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
    me = graphene.Field(UserType)
    users = graphene.List(UserType)
 
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
    def mutate(self,root, info, user_id,EmployeeNo,Nhif,DOE ,IDNO,Jobtitle ,PassportNo,Homecounty,Countyresidence,salary):
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
   

# class UpdateBook(graphene.Mutation):
#     class Arguments:
#         book_data = BookInput(required=True)

#     book = graphene.Field(BookType)

#     @staticmethod
#     def mutate(root, info, book_data=None):

#         book_instance = Book.objects.get(pk=book_data.id)

#         if book_instance:
#             book_instance.title = book_data.title
#             book_instance.author = book_data.author
#             book_instance.year_published = book_data.year_published
#             book_instance.review = book_data.review
#             book_instance.save()
#             return UpdateBook(book=book_instance)
#         return UpdateBook(book=None)
# class UpdateMovie(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         input = MovieInput(required=True)

#     ok = graphene.Boolean()
#     movie = graphene.Field(MovieType)

#     @staticmethod
#     def mutate(root, info, id, input=None):
#         ok = False
#         movie_instance = Movie.objects.get(pk=id)
#         if movie_instance:
#             ok = True
#             actors = []
#             for actor_input in input.actors:
#               actor = Actor.objects.get(pk=actor_input.id)
#               if actor is None:
#                 return UpdateMovie(ok=False, movie=None)
#               actors.append(actor)
#             movie_instance.title=input.title
#             movie_instance.year=input.year
#             movie_instance.save()
#             movie_instance.actors.set(actors)
#             return UpdateMovie(ok=ok, movie=movie_instance)
#         return UpdateMovie(ok=ok, movie=None)

class DeleteEmployee(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    employee = graphene.Field(EmployeeType)

    @staticmethod
    def mutate(root, info, id):
        employee_instance = Employee.objects.get(pk=id)
        employee_instance.delete()

        return None


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_employee = CreateEmployee.Field()
    create_user = CreateUser.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()

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

