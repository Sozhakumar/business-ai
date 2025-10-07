import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .Serializers import *

# Create your views here.
class CountryAPIView(APIView):
    message =""
    def post(self, request):
        data = request.data
        country_name = data.get('Country_name')

        # Check for duplicates
        if Country.objects.filter(Country_name__iexact=country_name).exists():
            return Response({"message": f"Country '{country_name}' already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Pass data to the serializer
        serializer = CountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"Country '{country_name}' added successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            instance = Country.objects.get(id=pk)
            serializer = CountrySerializer(instance)
        else:
            countries = Country.objects.all()
            serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = Country.objects.get(id=pk) 
        serializer = CountrySerializer(instance, data=request.data) 
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully updated the country', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(Self,request,*args, **kwargs):
        pk = kwargs.get('pk')
        instance = Country.objects.get(id = pk)
        instance.delete()
        return Response({'message': 'The message is deleted'},status=status.HTTP_200_OK)
    




class StateAPIView(APIView):
    message =""
    def post(self, request):
        data = request.data
        state_code = data.get('State_code')
        state_name = data.get('State_name')
        country_name = data.get('State_Country')


        if State.objects.filter(State_name__iexact=state_name, State_Country__Country_name__iexact=country_name).exists():
            return Response({"message": f"State '{state_name}' already exists in Country '{country_name}'"}, status=status.HTTP_400_BAD_REQUEST)
        

        
        serializer = StateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"State '{state_name}' added successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
    def get(self,request):
        stateID = request.query_params.get('stateID')
        if stateID:
            instance = State.objects.get(id=stateID)
            serializer=StateSerializer(instance)
        else:    
            states = State.objects.all()
            serializer = StateSerializer(states,many=True)

        return Response(serializer.data)
        
    def put(self,request):
        updateID = request.query_params.get("hiddenID")
        print(updateID,"ksksksksksk")
        instance = State.objects.get(id=updateID) 
        serializer = StateSerializer(instance, partial = True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":f" State is Updated Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':serializer._errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(Self,request):
        stateID = request.query_params.get('stateID')
        instance = State.objects.get(id = stateID)
        instance.delete()
        return Response({'message': 'The message is deleted'},status=status.HTTP_200_OK)
    



class CityAPIView(APIView):
    def post(self, request):
        data = request.data
        Country_name = data.get('City_Country')
        State_name = data.get('City_State')
        City_name = data.get('City_name')

        if City.objects.filter(City_Country__Country_name__iexact=Country_name, City_State__State_name__iexact=State_name, City_name__iexact=City_name).exists():
            return Response({"message": f"In this Country '{Country_name}', the state '{State_name}' and the city '{City_name}' already exist."}, status=status.HTTP_400_BAD_REQUEST)
    
        
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"State '{City_name}' added successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
    def get(self,request):
        cityID = request.query_params.get('cityID')
        if cityID:
            instance = City.objects.get(id=cityID)
            serializer=CitySerializer(instance)
        else:    
            cities = City.objects.all()
            serializer = CitySerializer(cities,many=True)

        return Response(serializer.data) 
        
    def put(self,request):
        updateID = request.query_params.get('hiddenID')
        instance = City.objects.get(id = updateID)
        serializer = CitySerializer(instance, partial=True ,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data,"message":f" City'{instance.City_name}' is Updated Successfully"},status=status.HTTP_200_OK)
        else:
            return Response({},status=status.HTTP_400_BAD_REQUEST) 

    def delete(self,request,):
        cityID = request.query_params.get('cityID')
        instance = City.objects.get(id = cityID)
        instance.delete()
        return Response({'message': "City is Successfully deleted"},status=status.HTTP_200_OK)



class AreaAPIView(APIView):
    def post(self,request):
        data = request.data
        Country_name = data.get('Area_Country')
        State_name = data.get('Area_State')
        City_name = data.get('Area_City')
        Area_name = data.get('Area_name')

        if Area.objects.filter(Area_Country__Country_name__iexact=Country_name, Area_State__State_name__iexact=State_name, Area_City__City_name__iexact=City_name, Area_name__iexact = Area_name).exists():
            return Response({"message": f"In this Country '{Country_name}',in the state '{State_name}'in this city '{City_name}'  and the Area is '{Area_name}' already exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = AreaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"City '{Area_name}' added successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def get(self,request):
        areaID = request.query_params.get('areaID')
        if areaID:
            instance = Area.objects.get(id = areaID)
            serializer = AreaSerializer(instance)
        else:
            Areas = Area.objects.all()
            serializer = AreaSerializer(Areas,many = True)
        return Response(serializer.data)    

    def put(self,request):
        updateID = request.query_params.get('hiddenID')
        instance = Area.objects.get(id = updateID)
        serializer = AreaSerializer(instance, partial = True ,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":f"Area is Updated Successfully"},status=status.HTTP_200_OK)
        else:
            return Response({},status=status.HTTP_400_BAD_REQUEST) 


    def delete(self,request):
        areaID = request.query_params.get('areaID')
        instance = Area.objects.get(id = areaID)
        instance.delete()
        return Response({'message': "Area is Successfully deleted"},status=status.HTTP_200_OK)
    
class DepartmentListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk'  



class DesignationAPIView(APIView):
    message =""
    def post(self, request):
        data = request.data
        designation_name = data.get('Designation_name')

        # Check for duplicates
        if Designation.objects.filter(Designation_name__iexact=designation_name).exists():
            return Response({"message": f"Designation '{designation_name}' already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Pass data to the serializer
        serializer = DesignationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"Designation '{designation_name}' added successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            instance = Designation.objects.get(id=pk)
            serializer = DesignationSerializer(instance)
        else:
            designations = Designation.objects.all()
            serializer = DesignationSerializer(designations, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = Designation.objects.get(id=pk) 
        serializer = DesignationSerializer(instance, data=request.data) 
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully updated the designation', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(Self,request,*args, **kwargs):
        pk = kwargs.get('pk')
        instance = Designation.objects.get(id = pk)
        instance.delete()
        return Response({'message': 'The message is deleted'},status=status.HTTP_200_OK)
    

class EmployeeAPIView(APIView):
    
    def generate_employee_code(self):
        last_employee = Employee.objects.order_by('id').last()
        if not last_employee:
            return "EMP0001"

        last_code = last_employee.Employee_Code
        new_code = int(last_code.replace('EMP', '')) + 1
        new_employee_code = f"EMP{new_code:04d}"
        return new_employee_code

    def post(self, request):
        status_filter = request.GET.get('status')
        if status_filter:
            if status_filter == 'active':
                employees = Employee.objects.filter(status=True)
            elif status_filter == 'inactive':
                employees = Employee.objects.filter(status=False)
            else:
                employees = Employee.objects.all()
            employee_serializer = EmployeeSerializer(employees, many=True)
            return Response(employee_serializer.data, status=status.HTTP_200_OK)

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request,*args, **kwargs):
        employeeID = kwargs.get('employeeID')
        if employeeID:
            try:
                instance = Employee.objects.get(id=employeeID)
                serializer = EmployeeSerializer(instance)
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            except Employee.DoesNotExist:
                return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request,*args, **kwargs):
        employeeID = kwargs.get('employeeID')
        try:
            instance = Employee.objects.get(id=employeeID)
            status_value = request.data.get('status')

            if status_value is not None:
                instance.status = status_value
                instance.save()
                return Response({"message": "Employee status updated successfully."}, status=status.HTTP_200_OK)


            serializer = EmployeeSerializer(instance, partial=True, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Employee updated successfully."}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Employee.DoesNotExist:
            return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request,*args, **kwargs):
        employeeID = kwargs.get('employeeID')
        if not employeeID:
            return Response({'message': 'Employee ID is required for deletion.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = Employee.objects.get(id=employeeID)
            instance.delete()
            return Response({'message': "Employee deleted successfully"}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        

@csrf_exempt
def toggle_employee_status(request, employee_id):
    if request.method == "POST":
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.status = not employee.status 
            employee.save()
            return JsonResponse({'status': employee.status}, status=200)
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

