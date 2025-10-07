
from django.contrib import admin
from django.urls import path
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('master/',views.master, name='master'),    
    path('index/',views.index, name='index'),
    path('countrypage/',views.createcountry,name='countrypage'),
    path('edit_country/',views.editbutton,name='edit_country'),
    path('delete_country/',views.deleteButton,name='delete_country'),
    path('state/',views.createstates,name='getstates'),
    path('edit_state/',views.editstate,name='edit_state'),
    path('delete_state/',views.deletestate,name='delete_state'),
    path('city/',views.createcity,name='getcities'),
    path('edit_city/',views.editcity,name='edit_city'),
    path('delete_city/',views.deletecity,name='delete_city'),
    path('area/',views.createarea,name='getareas'),
    path('edit_area/',views.editarea,name='edit_area'),
    path('delete_area/',views.deletearea,name='delete_area'),
    path('Department/',views.createdepartment,name='getdepartments'),
    path('edit_department/',views.editdepartment,name='edit_department'),
    path('delete_department/',views.deletedepartment,name='delete_department'),
    path('Designation/',views.createdesignation,name='getdesignations'),
    path('edit_designation/',views.editdesignation,name='edit_designation'),
    path('delete_designation/',views.deletedesignation,name='delete_department'),
    path('createemployee/',views.createemployees,name='Employee'),
    path('createemployee/<int:employee_id>/',views.createemployees,name='Employee_num'),
    path('edit_employee/',views.editEmployee,name='edit_employee'),
    path('delete_employee/',views.deleteEmployee,name='delete_employee'),
    path('Employee_List/',views.EmployeeFullList,name="Employee_list"),
]
