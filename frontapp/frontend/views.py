from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import requests
def home(request):
    return render(request,'home.html')

def master(request):
    return render(request,'master.html')

def index(request):
    return render(request, 'country.html')


def getcountries(request):
    countrylist = requests.get("http://127.0.0.1:8000/Country/").json()
    return countrylist


def createcountry(request):
    if request.method == "POST":
        country = request.POST.get('Country_Name')
        hiddencountryid = request.POST.get('hiddencountryid')
        countrylist = getcountries(request)
        message = ""
        
        if hiddencountryid: 
            data = {
                "Country_name": country
            }
            response = requests.put(f"http://127.0.0.1:8000/Country/{hiddencountryid}/", data=data)
            
            if response.status_code == 200:
                message = response.json().get('message', 'Successfully updated the country')
            else:
                message = response.json().get('message', 'An error occurred while updating the country')    
            
        else:  
            data = {
                "Country_name": country
            }
            response = requests.post("http://127.0.0.1:8000/Country/", data=data)
            
            if response.status_code == 201:
                message = response.json().get('message', 'Successfully created the country')
            else:
                message = response.json().get('message', 'An error occurred while creating the country') 
            

        messages.info(request, message)
        return redirect('countrypage')

    countrylist = getcountries(request)
    context = {
        "countrylist": countrylist,
    }
    return render(request, "country.html", context=context)


def editbutton(request):
    country_id = request.GET.get('countryid')
    
    if not country_id:
        return JsonResponse({'error': 'Country ID not provided'}, status=400)
    response = requests.get(f"http://127.0.0.1:8000/Country/{country_id}/")
    
    if response.status_code == 200:
        print(country_id,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        country_data = response.json()
        return JsonResponse(country_data)
    else:
        return JsonResponse({'error': 'Country not found'}, status=404)


def deleteButton(request):
    country_id = request.GET.get('countryid')
    if not country_id:
        return JsonResponse({'error': 'Country ID not provided'}, status=400)
    response = requests.delete(f"http://127.0.0.1:8000/Country/{country_id}/")
    
    if response.status_code == 200:
        return JsonResponse({'message': 'Country deleted successfully.'})
    else:
        return JsonResponse({'error': 'Country could not be deleted'}, status=response.status_code)
    

def getstates(request):
    statelist = requests.get("http://127.0.0.1:8000/state/").json()
    return statelist


def createstates(request):
    message= ""
    
    if request.method == "POST":
        state_code = request.POST.get('State_Code_in')
        state_name = request.POST.get('State_Name')
        country = request.POST.get('Select_Country_Name')
        hiddenstateid = request.POST.get('hiddenstateid')
        print(hiddenstateid,"bbbbbbbbbbbbbbbbbbbbbbbbbbb")
        if hiddenstateid:
            data = {
                "State_code": state_code,
                "State_name": state_name,
                "State_Country": country,
            }
            response = requests.put(url= f"http://127.0.0.1:8000/state/?hiddenID={hiddenstateid}", data=data)

            if response.status_code == 200:
                message = response.json().get('message', 'Successfully updated the State details')
            else:
                message = response.json().get('message', 'An error occurred while updating the State details') 
        
        else:  # Creating a new country
            data = {
                "State_code": state_code,
                "State_name": state_name,
                "State_Country": country,
            }
            response = requests.post("http://127.0.0.1:8000/state/", data=data)
            
            if response.status_code == 200:
                message = response.json().get('message', 'Successfully created the State')
            else:
                message = response.json().get('message', 'An error occurred while creating the State') 
        messages.info(request, message)
        return redirect('getstates')

    statelist = getstates(request)
    countrylist = getcountries(request)  
    print(countrylist,"111111111111111111")
    print(statelist,"222222222222222222")
    context = {
        "statelist": statelist,
        "countrylist": countrylist,
        "message": message,    
    }
    return render(request, "state.html", context=context)

def editstate(request):
    state_id = request.GET.get('stateid')
    if not state_id:
        return JsonResponse({'error': 'State ID not provided'}, status=400)
    response = requests.get(url = f"http://127.0.0.1:8000/state/?stateID={state_id}")
    
    if response.status_code == 200:
        state_data = response.json()
        return JsonResponse(state_data)
    else:
        return JsonResponse({'error': 'State not found'}, status=404)

def deletestate(request):
    state_id = request.GET.get('stateid')
    if not state_id:
        return JsonResponse({'error': 'State ID not provided'},status=400)
    response=requests.delete(url = f"http://127.0.0.1:8000/state/?stateID={state_id}")

    if response.status_code==200:
        return JsonResponse({'message': 'State deleted successfully.'})
    else:
        return JsonResponse({'error': 'State could not be deleted'}, status=response.status_code)
    


def getcities(request):
    statelist = requests.get("http://127.0.0.1:8000/city/").json()
    return statelist


def createcity(request):
    message = ""
    if request.method == "POST":
        city_name = request.POST.get('City_Name_in')  
        state = request.POST.get('Select_State_Name')
        country = request.POST.get('Select_Country_Name')
        hiddencityid = request.POST.get('hiddencityid')
        if hiddencityid:  
            data = {
            "City_name": city_name,
            "City_State": state,
            "City_Country": country,
        }
            response = requests.put(url=f"http://127.0.0.1:8000/city/?hiddenID={hiddencityid}", data=data)
            if response.status_code == 200:
                message = response.json().get('message', 'Successfully updated the City details')
            else:
                message = response.json().get('message', 'An error occurred while updating the City details')    
        else: 
            data = {
            "City_name": city_name,
            "City_State": state,
            "City_Country": country,
        }
            response = requests.post("http://127.0.0.1:8000/city/", data=data)
            if response.status_code in [200, 201]: 
                message = response.json().get('message', 'Successfully created the City')
            else:
                message = response.json().get('message', 'An error occurred while creating the City')
        
        messages.info(request, message)
        return redirect('getcities')

    statelist = getstates(request)
    countrylist = getcountries(request)
    citylist = getcities(request)  

    context = {
        "statelist": statelist,
        "countrylist": countrylist,
        "citylist": citylist,
        "message": message,    
    }
    return render(request, "city.html", context=context)



def editcity(request):
    city_id = request.GET.get('cityid')
    if not city_id:
        return JsonResponse({'error': 'City ID not provided'}, status=400)
    response = requests.get(url = f"http://127.0.0.1:8000/city/?cityID={city_id}")
    
    if response.status_code == 200:
        city_data = response.json()
        return JsonResponse(city_data)
    else:
        return JsonResponse({'error': 'City not found'}, status=404)


def deletecity(request):
    city_id = request.GET.get('cityid')
    if not city_id:
        return JsonResponse({'error': 'City ID not provided'}, status=400)
    response = requests.delete(url = f"http://127.0.0.1:8000/city/?cityID={city_id}")
    
    if response.status_code == 200:
        return JsonResponse({'message': 'City deleted successfully.'})
    else:
        return JsonResponse({'error': 'City could not be deleted'}, status=response.status_code)

def getareas(request):
    statelist = requests.get("http://127.0.0.1:8000/area/").json()
    return statelist


def createarea(request):
    message = ""
    if request.method == "POST":
        area_name = request.POST.get('Area_Name_in')
        city = request.POST.get('Select_City_Name')  
        state = request.POST.get('Select_State_Name')
        country = request.POST.get('Select_Country_Name')
        hiddenareaid = request.POST.get('hiddenareaid')
        if hiddenareaid:
            data = {
            "Area_name": area_name,
            "Area_City": city,
            "Area_State": state,
            "Area_Country": country,
        }
            response = requests.put(url=f"http://127.0.0.1:8000/area/?hiddenID={hiddenareaid}", data=data)
            if response.status_code == 200:
                message = response.json().get('message', 'Successfully updated the Area details')
            else:
                message = response.json().get('message', 'An error occurred while updating the Area details')    
        else: 
            data = {
            "Area_name": area_name,
            "Area_City": city,
            "Area_State": state,
            "Area_Country": country,
            }
            response = requests.post("http://127.0.0.1:8000/area/", data=data)
            if response.status_code in [200, 201]: 
                message = response.json().get('message', 'Successfully created the Area')
            else:
                message = response.json().get('message', 'An error occurred while creating the Area')
        
        messages.info(request, message)
        return redirect('getareas')

    statelist = getstates(request)
    countrylist = getcountries(request)
    citylist = getcities(request)
    arealist = getareas(request)  

    context = {
        "statelist": statelist,
        "countrylist": countrylist,
        "citylist": citylist,
        "arealist": arealist,
        "message": message,    
    }
    return render(request, "area.html", context=context)


def editarea(request):
    area_id = request.GET.get('areaid')
    if not area_id:
        return JsonResponse({'error': 'Area ID not provided'}, status=400)
    response = requests.get(url = f"http://127.0.0.1:8000/area/?areaID={area_id}")
    
    if response.status_code == 200:
        area_data = response.json()
        return JsonResponse(area_data)
    else:
        return JsonResponse({'error': 'Area not found'}, status=404)    
    

def deletearea(request):
    area_id = request.GET.get('areaid')
    if not area_id:
        return JsonResponse({'error': 'Area ID not provided'}, status=400)
    response = requests.delete(url = f"http://127.0.0.1:8000/area/?areaID={area_id}")
    
    if response.status_code == 200:
        return JsonResponse({'message': 'Area deleted successfully.'})
    else:
        return JsonResponse({'error': 'Area could not be deleted'}, status=response.status_code)



def getdepartments(request):
    departmentlist = requests.get("http://127.0.0.1:8000/Department/").json()
    return departmentlist

def createdepartment(request):
    if request.method == "POST":
        department = request.POST.get('Department_name_in')
        hiddendepartmentid = request.POST.get('hiddendepartmentid') 

        if hiddendepartmentid: 
            data = {'Department_name': department}
            response = requests.put(f"http://127.0.0.1:8000/Department/{hiddendepartmentid}/", data=data)
            
            if response.status_code == 200:
                message = response.json().get('message', 'Successfully updated the department')
            else:
                message = response.json().get('message', 'An error occurred while updating the department')    
            
        else: 
            data = {'Department_name': department}
            response = requests.post(url="http://127.0.0.1:8000/Department/", data=data)
            
            if response.status_code in [200, 201]: 
                message = response.json().get('message', 'Successfully created the Department')
            else:
                message = response.json().get('message', 'An error occurred while creating the Department')
        messages.info(request, message)
        return redirect('getdepartments')        
    

    departmentlist = getdepartments(request)
    context = {'departmentlist': departmentlist}
    return render(request, "department.html", context=context)

def editdepartment(request):
    department_id = request.GET.get('departmentid')
    if not department_id:
        return JsonResponse({'error': 'Department ID not provided'}, status=400)
    response = requests.get(url = f"http://127.0.0.1:8000/Department/{department_id}")
    
    if response.status_code == 200:
        department_data = response.json()
        return JsonResponse(department_data)
    else:
        return JsonResponse({'error': 'Department not found'}, status=404)

def deletedepartment(request):
    department_id = request.GET.get('departmentid')
    print(department_id,"bbbbbbbbbbbbbbbb")
    if not department_id:
        return JsonResponse({'error': 'department ID not provided'}, status=400)
    response = requests.delete(url = f"http://127.0.0.1:8000/Department/{department_id}/")
    
    if response.status_code == 204:
        return redirect('getdepartments') 
    else:
        return JsonResponse({'error': 'department could not be deleted'}, status=response.status_code)
    


def getdesignations(request):
    designationlist = requests.get("http://127.0.0.1:8000/Designation/").json()
    return designationlist


def createdesignation(request):
    if request.method == "POST":
        designation = request.POST.get('Designation_Name_in')
        hiddendesignationid = request.POST.get('hiddendesignationid')

        if hiddendesignationid: 
            data = {'Designation_name': designation}
            response = requests.put(f"http://127.0.0.1:8000/Designation/{hiddendesignationid}/", data=data)
            
            if response.status_code == 200:
                message = response.json().get('message', 'Successfully updated the designation')
            else:
                message = response.json().get('message', 'An error occurred while updating the designation')
            
        else:  # Creating a new designation
            data = {'Designation_name': designation}
            response = requests.post(url="http://127.0.0.1:8000/Designation/", data=data)
            
            if response.status_code in [200, 201]:
                message = response.json().get('message', 'Successfully created the Designation')
            else:
                message = response.json().get('message', 'An error occurred while creating the Designation')

        messages.info(request, message)
        return redirect('getdesignations')        

    designationlist = getdesignations(request)
    context = {'designationlist': designationlist}
    return render(request, "designation.html", context=context)

def editdesignation(request):
    designation_id = request.GET.get('designationid')
    if not designation_id:
        return JsonResponse({'error': 'Designation ID not provided'}, status=400)
    response = requests.get(url = f"http://127.0.0.1:8000/Designation/{designation_id}")
    
    if response.status_code == 200:
        designation_data = response.json()
        return JsonResponse(designation_data)
    else:
        return JsonResponse({'error': 'Designation not found'}, status=404)
    
def deletedesignation(request):
    designation_id = request.GET.get('designationid')
    print(designation_id,"bbbbbbbbbbbbbbbb")
    if not designation_id:
        return JsonResponse({'error': 'Designation ID not provided'}, status=400)
    response = requests.delete(url = f"http://127.0.0.1:8000/Designation/{designation_id}/")
    
    if response.status_code == 204:
        return JsonResponse({'message': 'Designation deleted successfully.'}) 
    else:
        return JsonResponse({'error': 'department could not be deleted'}, status=response.status_code)
    

def getemployees(request):
    try:
        response = requests.get("http://127.0.0.1:8000/Employee/")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        messages.error(request, f"Error fetching employee list: {e}")
    return []


def createemployees(request, employee_id=None):
    message = ""
    employee_code = ""
    employee_data = None

    def fetch_employee_data(employee_id):
        try:
            response = requests.get(f"http://127.0.0.1:8000/Employee/{employee_id}")
            if response.status_code == 200:
                return response.json().get('data')
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Error fetching employee data: {e}")
        return None

    
    def generate_employee_code():
        try:
            response = requests.get("http://127.0.0.1:8000/Employee/")
            if response.status_code == 200:
                employees = response.json()
                if employees:
                    last_employee = employees[-1]
                    last_code = last_employee['Employee_Code']
                    new_code = int(last_code.replace('EMP', '')) + 1
                    return f"EMP{new_code:04d}"
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Error generating employee code: {e}")
        return "EMP0001"
    
    if employee_id:
        employee_data = fetch_employee_data(employee_id)
        if employee_data:
            employee_code = employee_data.get('Employee_Code', '')
    else:
        employee_code = generate_employee_code()

    if request.method == "POST":
        hiddenemployeeid = request.POST.get('hiddenemployeeid')
        current_address = request.POST.get('Current_Address_in')
        permanent_address = request.POST.get('Permanent_Address_in')
        same_address = request.POST.get('Same_Address_in')

        Employee_name = request.POST.get('Employee_name_in')
        Date_of_Birth = request.POST.get('Date_of_Birth_in')
        Gender = request.POST.get('Gender_select_in')
        Blood_Group = request.POST.get('Blood_Group_select_in')
        Date_of_Joining = request.POST.get('Date_of_Joining_in')
        print(hiddenemployeeid,'ddddddddddddddddsss')
        if not Employee_name or not Date_of_Birth:
            messages.error(request, "Employee Name and Date of Birth are required.")
            return redirect('Employee')

        if same_address:
            permanent_address = current_address

        try:
            data = {
                "Employee_name": Employee_name,
                "Date_of_Birth": Date_of_Birth,
                "Gender": Gender,
                "Blood_Group": Blood_Group,
                "Date_of_Joining": Date_of_Joining,
                "Branch": request.POST.get('Branch_select_in'),
                "Department": request.POST.get('Department_select_in'),
                "Designation": request.POST.get('Designation_select_in'),
                "Personal_Admin": request.POST.get('Personal_Admin_in'),
                "Qualification": request.POST.get('Qualification_select_in'),
                "Degree": request.POST.get('Degree_in'),
                "Email_Id": request.POST.get('Email_Id_in'),
                "Mobile_Number": request.POST.get('Mobile_Number_in'),
                "Current_Address": current_address,
                "Permanent_Address": permanent_address,
                "Aadhaar_Number": request.POST.get('Aadhaar_Number_in'),
                "Punching_Machine_Code": request.POST.get('Punching_Machine_Code_in'),
                "PAN_No": request.POST.get('PAN_No_in'),
                "EPF_No": request.POST.get('EPF_No_in'),
                "ESI_No": request.POST.get('ESI_No_in'),
                "Target": request.POST.get('Target_in'),
                "User_Menu_Permission": request.POST.get('User_Menu_Permission_select_in'),
                "Login_Name": request.POST.get('Login_Name_in'),
                "Password": request.POST.get('Password_in'),
                "Previous_Experience": request.POST.get('Previous_Experience_in'),
                "Experience_In_Years": request.POST.get('Experience_In_Years_in'),
                "Reference_Through": request.POST.get('Reference_Through_in'),
                "Previous_Company_Name": request.POST.get('Previous_Company_Name_in'),
                "Reference_Name": request.POST.get('Reference_Name_in'),
                "Account_Number": request.POST.get('Account_Number_in'),
                "Account_Holder_Name": request.POST.get('Account_Holder_Name_in'),
                "IFSC_Code": request.POST.get('IFSC_Code_in'),
                "Bank_Name": request.POST.get('Bank_Name_in'),
                "Branch_Name": request.POST.get('Branch_Name_in'),
                "Salary_Type": request.POST.get('Salary_Type_select_in'),
                "Permission_Amount_Per_Hour": request.POST.get('Permission_Amount_Per_Hour_in'),
                "Professional_Tax": request.POST.get('Professional_Tax_in'),
                "Working_Hours": request.POST.get('Working_Hours_in'),
                "Basic_Pay": request.POST.get('Basic_Pay_in'),
                "RD": request.POST.get('RD_in'),
                "Casual_Leave_Per_Month": request.POST.get('Casual_Leave_Per_Month_in'),
                "HRA": request.POST.get('HRA_in'),
                "PF": request.POST.get('PF_in'),
                "Sick_Leave_Per_Month": request.POST.get('Sick_Leave_Per_Month_in'),
                "Medical_Allowance": request.POST.get('Medical_Allowance_in'),
                "ESI": request.POST.get('ESI_in'),
                "Over_Time_Amount_Per_Hour": request.POST.get('Over_Time_Amount_Per_Hour_in'),
                "Conveyance_Allowance": request.POST.get('Conveyance_Allowance_in'),
                "Loss_of_Pay_Per_Day": request.POST.get('Loss_of_Pay_Per_Day_in'),
                "General_Allowance": request.POST.get('General_Allowance_in'),
                "Net_Salary": request.POST.get('Net_Salary_in')
            }

            files = {}
            employee_image = request.FILES.get('Employee_Image_in')
            employee_signature = request.FILES.get('Employee_Signature_in')
            if employee_image:
                files["Employee_Image"] = employee_image
            if employee_signature:
                files["Employee_Signature"] = employee_signature

            if hiddenemployeeid:
                response = requests.put(f"http://127.0.0.1:8000/Employee/{hiddenemployeeid}/", data=data, files=files)
                message = response.json().get('message', 'Successfully updated the Employee')
            else:
                response = requests.post("http://127.0.0.1:8000/Employee/", data=data, files=files)
                message = response.json().get('message', 'Successfully added the Employee')
                
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Error saving employee: {e}")
            return redirect('Employee')

        messages.info(request, message)
        return redirect('Employee_list')

    departmentlist = getdepartments(request)
    designationlist = getdesignations(request)
    employeelist = getemployees(request)


    context = {
        'employeelist': employeelist,
        'designationlist': designationlist,
        'departmentlist': departmentlist,
        'employee_code': employee_code,
        'employee_data': employee_data,
    }

    return render(request, "employee.html", context=context)



def editEmployee(request):
    employee_id = request.GET.get('employeeid')
    if not employee_id:
        return JsonResponse({'error': 'Employee ID not provided'}, status=400)
    response = requests.get(f"http://127.0.0.1:8000/Employee/{employee_id}/")

    if response.status_code == 200:
        employee_data = response.json()
        return JsonResponse(employee_data)
    else:
        return JsonResponse({'error': 'Employee not found'}, status=404)
    

def deleteEmployee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employeeid')
        if not employee_id:
            return JsonResponse({'error': 'Employee ID not provided'}, status=400)

        response = requests.delete(f"http://127.0.0.1:8000/Employee/{employee_id}/")

        if response.status_code == 204:
            return JsonResponse({'message': 'Employee deleted successfully'})
        else:
            return JsonResponse({'error': 'Employee could not be deleted'}, status=response.status_code)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
    

def EmployeeFullList(request):
    employee_id = request.POST.get('employee_id')  
    if request.method == "POST":
        try:
            response = requests.post(f"http://127.0.0.1:8000/toggle-status/{employee_id}/", data={'status': request.POST.get('status')})
            if response.status_code == 200:
                employee_data = response.json()
                messages.success(request, 'Successfully updated the status.')
                return JsonResponse(employee_data)
            else:
                messages.error(request, 'Failed to update status.')
        except requests.RequestException as e:
            messages.error(request, f"Error fetching status: {e}")

    employeelist = getemployees(request) 
    departmentlist = getdepartments(request) 
    context = {
        "employeelist": employeelist,
        "departmentlist": departmentlist,
    }
    return render(request, 'employeelist.html', context=context)
