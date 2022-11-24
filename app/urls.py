
from django.urls import include, path
from . import views
from .views import Alluser,user_view,user_view_detail

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('profile/', views.Profile.as_view(), name='profile'),
   
   
    # opd
    path('opdcardtable/', views.opdcardtable, name='opdcardtable'),
    path('opdaddpatient/', views.opdaddpatient, name='opdaddpatient'),

    # BILL
    path('newbill/', views.newbill, name='newbill'),
    path('allinvoices/', views.allinvoices, name='allinvoices'),

    # Role
    path('addrole/', views.addrole.as_view(), name='addrole'),
    path('addrole/list/', views.listrole.as_view(), name='list_role'),
    path('addrole/create/', views.listrole.as_view(), name='create_role'),
    path('addrole/delete/<int:id>', views.role_view.as_view(), name='delete_role'),
    path('addrole/edit/<int:id>', views.role_view.as_view(), name='edit_role'),



    # staff Role
    path('addstaffrole/', views.Addstaffrole.as_view(), name='addstaffrole'),
    path('addstaffrole/list/', views.ListstaffRole.as_view(), name='liststaffrole'),
    path('addstaffrole/create/', views.ListstaffRole.as_view(), name='createstaffrole'),

    #add Staff
    path('addstaff/', views.addstaff, name='addstaff'),

    # lab
    path('generatelabreport/', views.generatelabreport, name='generatelabreport'),

    # register
    path('register/', views.register_user.as_view(), name='register'),
    path('check_username/', views.Check_Username.as_view(), name='check_username'), 
    path('check_email/', views.Check_Email.as_view(), name='check_email'),
    # login
    path('login/', views.login_user, name='login'),
    path('logout/', views.Logout_user, name='logout'),
    path('check_login_username/', views.Check_Login_Username.as_view(), name='check_login_username'),
    path('check_password/', views.Check_Password.as_view(), name='check_user_password'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),


    # all user
    path('alluser/', Alluser.as_view(), name='alluser'),
    path('alluser/list/',user_view.as_view(), name="list_users"),
    path('alluser/create/', user_view.as_view(), name="create_users"),
    path('alluser/delete/<int:id>', user_view_detail.as_view(), name="delete_user"),
    path('alluser/edit/<int:id>', user_view_detail.as_view(), name="edit_user"),




]
