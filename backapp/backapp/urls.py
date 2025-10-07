
from django.contrib import admin
from django.urls import path
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Country/',views.CountryAPIView.as_view()),  
    path('Country/<int:pk>/',views.CountryAPIView.as_view()),
    path('state/', views.StateAPIView.as_view(),name='State_api'),
    path('city/', views.CityAPIView.as_view(),name='City_api'),
    path('area/', views.AreaAPIView.as_view(),name='Area_api'),
    path('Department/', views.DepartmentListCreate.as_view(),name='Department_api'),
    path('Department/<int:pk>/', views.DepartmentRetrieveUpdateDelete.as_view(),name='Department_api_num'),
    path('Designation/', views.DesignationAPIView.as_view(),name='Designation_api'),
    path('Designation/<int:pk>/', views.DesignationAPIView.as_view(),name='Designation_api_num'),
    path('Employee/', views.EmployeeAPIView.as_view(),name='Employee_api'),
    path('Employee/<int:employeeID>/', views.EmployeeAPIView.as_view(),name='Employee_api_num'),
    path('toggle-status/<int:employee_id>/', views.toggle_employee_status, name='toggle_status'),
]