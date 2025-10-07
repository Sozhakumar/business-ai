from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'Country_name']


class StateSerializer(serializers.ModelSerializer):
    country_name = serializers.StringRelatedField(source='State_Country.Country_name')

    class Meta:
        model = State
        fields = ['id', 'State_name', 'State_code', 'State_Country', 'country_name']

class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.StringRelatedField(source='City_Country.Country_name')
    state_name = serializers.StringRelatedField(source='City_State.State_name')
    
    class Meta:
        model = City
        fields = ['id', 'City_name', 'City_State', 'City_Country', 'country_name', 'state_name']

class AreaSerializer(serializers.ModelSerializer):
    country_name = serializers.StringRelatedField(source='Area_Country.Country_name')
    state_name = serializers.StringRelatedField(source='Area_State.State_name')
    city_name = serializers.StringRelatedField(source='Area_City.City_name')  

    class Meta:
        model = Area
        fields = ['id', 'Area_name', 'Area_City', 'Area_State', 'Area_Country', 'country_name', 'state_name', 'city_name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'Department_name']
    
    def validate_Department_name(self, value):
        if Department.objects.filter(Department_name__iexact=value).exists():
            raise serializers.ValidationError("This department name already exists.")
        return value
    
    
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['id', 'Designation_name']



class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.StringRelatedField(source="Department.Department_name")
    class Meta:
        model = Employee 
        fields = "__all__"
        
        def validate(self, data):
            employee_code = data.get('Employee_Code')
            email = data.get('Email_Id')
            mobile_number = data.get('Mobile_Number')
            aadhaar_number = data.get('Aadhaar_Number')
            pan_no = data.get('PAN_No')
            punching_machine_code = data.get('Punching_Machine_Code')
            epf_no = data.get('EPF_No')
            esi_no = data.get('ESI_No')
            login_name = data.get('Login_Name')
            account_number = data.get('Account_Number')

            if Employee.objects.filter(Employee_Code__iexact=employee_code).exists():
                raise serializers.ValidationError({'Employee_Code': "Employee with this code already exists."})
            
            if Employee.objects.filter(Email_Id__iexact=email).exists():
                raise serializers.ValidationError({'Email_Id': "Employee with this email already exists."})

            if Employee.objects.filter(Mobile_Number=mobile_number).exists():
                raise serializers.ValidationError({'Mobile_Number': "Employee with this mobile number already exists."})

            if Employee.objects.filter(Aadhaar_Number=aadhaar_number).exists():
                raise serializers.ValidationError({'Aadhaar_Number': "Employee with this Aadhaar number already exists."})

            if Employee.objects.filter(PAN_No__iexact=pan_no).exists():
                raise serializers.ValidationError({'PAN_No': "Employee with this PAN number already exists."})

            if Employee.objects.filter(Punching_Machine_Code__iexact=punching_machine_code).exists():
                raise serializers.ValidationError({'Punching_Machine_Code': "Employee with this Punching Machine Code already exists."})

            if Employee.objects.filter(EPF_No__iexact=epf_no).exists():
                raise serializers.ValidationError({'EPF_No': "Employee with this EPF number already exists."})

            if Employee.objects.filter(ESI_No__iexact=esi_no).exists():
                raise serializers.ValidationError({'ESI_No': "Employee with this ESI number already exists."})

            if Employee.objects.filter(Login_Name__iexact=login_name).exists():
                raise serializers.ValidationError({'Login_Name': "Employee with this login name already exists."})

            if Employee.objects.filter(Account_Number=account_number).exists():
                raise serializers.ValidationError({'Account_Number': "Employee with this account number already exists."})

            return data
