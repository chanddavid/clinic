from urllib import response
from django.contrib import messages
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .hashing import get_salt,hash_string
from .serializers import RoleSerializer, UserSerializers,StaffRoleSerializer
from .models import User,Role,StaffRole
from rest_framework.response import Response
from .decorators import my_login_required
from .forms import UserForm
from rest_framework import status
from django.forms import model_to_dict

from app import serializers





# Create your views here.

class index(APIView):
    @my_login_required
    def get(self,request):
        return render(request,'index.html')


    def post(self,request):
        data=request.data
        print("login",data)
        return render(request,'index.html')


class Profile(APIView):
    @my_login_required
    def get(self,request):
        current_logged_in_user = request.session.get("user_name")
        print(current_logged_in_user)
        user = User.objects.get(user_name=current_logged_in_user)
        serializer=UserSerializers(user)
        data=serializer.data
        print(data)
        context={
            "datas":data
        }
        return render(request,'profile.html',context)


def login_user(request):
    if not request.session.has_key('username'):
        return render(request, 'login.html')
    else:
       return redirect('index')


def forgot_password(request):
    return render(request,'forgot-password.html')

#register mew user
class register_user(APIView): 
    def get(self,request):
        return render(request, 'register.html')

    def post(self,request):
        data=request.data
        salt=get_salt()
        hashed_password=hash_string(salt,data['password'])
        data = {
            'user_name': request.data['user_name'], 
            'full_name':request.data['full_name'], 
            'email':request.data['email'], 
            'password': request.data['password'], 
            'confirm_password':request.data['confirm_password'], 
            'phone_number': request.data['phone_number'],
            'specilist': request.data['specilist'],
            'role': request.data['role'],
            'district': request.data['district'],
            'city': request.data['city'],
            'ward': request.data['ward'],}
        serializer=UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save(salt=salt,hashed_password=hashed_password,is_active=False)
            username=serializer.validated_data['user_name']
            messages.success(request,f'{username} created.')
            return redirect('login')
        elif serializer.errors:
            print("errors",serializer.errors)
            return redirect('register')

class Check_Username(APIView):
    def post(self, request):
        username = request.POST.get("user_name")
        if not User.objects.filter(user_name=username).exclude().exists():
            return Response(True)
        else:
            return Response(False)

class Check_Email(APIView):
    def post(self, request):
        email = request.POST.get("email")
        if not User.objects.filter(email=email).exists():
            return Response(True)
        else:
            return Response(False)
        
# login
class Check_Login_Username(APIView):
    def post(self, request):
        username = request.POST.get("user_name")
        request.session['user_name']=username
        if User.objects.filter(user_name=username).exclude().exists():
            return Response(True)
        else:
            return Response(False)
   
class Check_Password(APIView):
     def post(self, request):
        print(request.POST)
        current_logged_in_user = request.session.get("user_name")
        user = User.objects.get(user_name=current_logged_in_user)
        current_password = request.POST.get('password')
        salt = user.salt
        hashed_password = user.hashed_password
        if hash_string(salt, current_password) == hashed_password:
            return Response(True)
        else:
            return Response(False)
        
        
# logout
def Logout_user(request):
    try:
        del request.session['user_name']
    except:
        pass
    return redirect('login')

class Alluser(APIView):
    @my_login_required
    def get(self, request):
        form=UserForm           
        context = {
            'form': form
        }
        return render(request,'User/user.html',context)

class user_view(APIView):
    """APIView of the user..."""
    def get(self, request):
        """Get request to list all the users..."""
        users = User.objects.all()
        user_serializer = UserSerializers(users, many=True)
        return Response({"data": user_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """Post request to create new users..."""
        data = request.data
        print(data)
        salt = get_salt()
        hashed_password = hash_string(salt, data["password"])
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save(salt=salt, hashed_password=hashed_password)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif serializer.errors:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class user_view_detail(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist as e:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        """Get request to retrieve user of specific user id..."""
        global edit_user
        instance = self.get_object(id=id)
        print(model_to_dict(instance))
        edit_user = instance
        serializer = UserSerializers(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id):
        """Put request to update the user of specific id...."""
        instance = self.get_object(id=id)
        data = request.data
        print(model_to_dict(instance))
        print(data)
        serializer = UserSerializers(data=data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif serializer.errors:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Delete request to remove the user of specific id..."""
        instance = self.get_object(id=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def opdaddpatient(request):
    return render(request,'Opd/opdaddpatient.html')

def opdcardtable(request):
    return render(request,'Opd/opdcardtable.html')

def newbill(request):
    return render(request,'Bill/newbill.html')

def allinvoices(request):
    return render(request,'Bill/allinvoices.html')

def generatelabreport(request):
    return render(request,'Lab/generatelabreport.html')


# add role
class addrole(APIView):
    @my_login_required
    def get(self,request):
        return render(request,'Role/addrole.html')

class listrole(APIView):
    def get(self,request):
        roles=Role.objects.all()
        roleserializer=RoleSerializer(roles,many=True)
        return Response({"data":roleserializer.data},status=status.HTTP_200_OK)

    def post(self,request):
        data=request.data
        roles_serializer=RoleSerializer(data=data)
        if roles_serializer.is_valid():
            roles_serializer.save()
            return Response(roles_serializer.data,status=status.HTTP_201_CREATED)
        elif roles_serializer.errors:
            return Response(roles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class role_view(APIView):
    def get_object(self, id):
        try:
            return Role.objects.get(id=id)
        except Role.DoesNotExist as e:
            return Response({'error': 'Role Does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):

        instance = self.get_object(id=id)
        role_serializer = RoleSerializer(instance)
        return Response(role_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):

        instance = self.get_object(id=id)
        data = request.data
        role_serializer = RoleSerializer(data=data, instance=instance, partial=True)
        if role_serializer.is_valid():
            role_serializer.save()
            return Response(role_serializer.data, status=status.HTTP_200_OK)
        elif role_serializer.errors:
            print(role_serializer.errors)
            return Response(role_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        instance = self.get_object(id=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# add staff role
class Addstaffrole(APIView):
    @my_login_required
    def get(self,request):
        user=User.objects.all()
        role=Role.objects.all()
        roleserializer=RoleSerializer(role,many=True)
        userserializer=UserSerializers(user,many=True)
        data=userserializer.data
        data1=roleserializer.data
        print(data1)
        context={
            "data":data,
            "data1":data1
        }
        return render(request,'StaffRole/addstaffrole.html',context)

class ListstaffRole(APIView):
    def get(self,request):
        staffrole=StaffRole.objects.all()
        serializer=StaffRoleSerializer(staffrole,many=True)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)

    def post(self,request):
        data=request.data
        print("posted data",data)
        serializers=StaffRoleSerializer(data=data)
        if serializers.is_valid():
            print("printed")
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        elif serializers.errors:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    


def addstaff(request):
    return render(request,'AddStaff/addstaff.html')
