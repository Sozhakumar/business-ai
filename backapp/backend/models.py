from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

class Country(models.Model):
    Country_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return "Country:" + self.Country_name
    


class State(models.Model):
    State_name = models.CharField(max_length=100,unique=True)
    State_code = models.CharField(max_length=100)
    State_Country = models.ForeignKey(Country,related_name="State_Countries",on_delete=models.PROTECT) 

    def __str__(self):
        return "Country:" + self.State_Country.Country_name + "------------------------>" + "State_code:" + self.State_code + "--------------------------->" + "State:" +  self.State_name
    
class City(models.Model):
    City_name = models.CharField(max_length=100,unique=True)
    City_State = models.ForeignKey(State,related_name="City_states",on_delete=models.PROTECT)
    City_Country = models.ForeignKey(Country,related_name="City_countries",on_delete=models.PROTECT)

    def __str__(self):
        return "Country:" + self.City_Country.Country_name + "------------------------>" + "State:" +  self.City_State.State_name + "-------------------------->" + "City" + self.City_name
    
class Area(models.Model):
    Area_name = models.CharField(max_length=100,unique=True)
    Area_City = models.ForeignKey(City,related_name="Area_cities",on_delete=models.PROTECT)
    Area_State = models.ForeignKey(State,related_name="Area_states",on_delete=models.PROTECT)
    Area_Country = models.ForeignKey(Country,related_name="Area_countries",on_delete=models.PROTECT)    

    def __str__(self):
        return "Country:" + self.Area_Country.Country_name + "------------------------>" + "State:" +  self.Area_State.State_name + "-------------------------->" + "City"  + self.Area_City.City_name + "------------------->" + "Area:" + self.Area_name
    
class Department(models.Model):
    Department_name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('Department_name'),
                name='unique_department_name_case_insensitive'
            )
        ]

    def __str__(self):
        return "Department:" + self.Department_name  

class Designation(models.Model):
    Designation_name = models.CharField(max_length=100)
    
    def __str__(self):
        return "Designation:" + self.Designation_name  

class Employee(models.Model):
    Employee_Code = models.CharField(max_length=10, unique=True, blank=True, null=True)
    Employee_name = models.CharField(max_length=100)
    Date_of_Birth = models.DateField(blank=True,null=True)
    Gender = models.CharField(max_length=100)
    Blood_Group = models.CharField(max_length=50)
    Branch = models.CharField(max_length=100,blank=True,null=True)
    Department = models.ForeignKey(Department,blank=True, on_delete=models.PROTECT,null=True)
    Designation = models.ForeignKey(Designation, on_delete=models.PROTECT,blank=True,null=True)
    Personal_Admin = models.CharField(max_length=100,blank=True,null=True)
    Date_of_Joining = models.DateField(blank=True,null=True)
    Qualification = models.CharField(max_length=100,blank=True,null=True)
    Degree = models.CharField(max_length=100,blank=True,null=True)
    Email_Id =models.EmailField(max_length=200,unique=True,blank=True,null=True)
    Mobile_Number = models.IntegerField(unique=True,blank=True,null=True)
    Current_Address =models.CharField(max_length=500,blank=True,null=True)
    Permanent_Address = models.CharField(max_length=500,blank=True,null=True)
    Aadhaar_Number = models.IntegerField(unique=True,blank=True,null=True)
    Punching_Machine_Code = models.CharField(max_length=100,unique=True,blank=True,null=True)
    PAN_No = models.CharField(max_length=100,unique=True,blank=True,null=True)
    EPF_No = models.CharField(max_length=100,unique=True,blank=True,null=True)
    ESI_No = models.CharField(max_length=100,unique=True,blank=True,null=True)
    Target = models.IntegerField(blank=True,null=True)
    Employee_Image = models.ImageField(upload_to='Employee_Images/',blank=True,null=True)
    Employee_Signature = models.ImageField(upload_to='Employee_Signature/',blank=True,null=True)
    User_Menu_Permission = models.CharField(max_length=200,blank=True,null=True)
    Login_Name = models.CharField(max_length=100,unique=True,blank=True,null=True)
    Password = models.CharField(max_length=100,blank=True,null=True)
    Previous_Experience =  models.CharField(max_length=100,blank=True,null=True)
    Experience_In_Years = models.IntegerField(blank=True,null=True)
    Reference_Through = models.CharField(max_length=100,blank=True,null=True)
    Previous_Company_Name = models.CharField(max_length=100,blank=True,null=True)
    Reference_Name = models.CharField(max_length=100,blank=True,null=True)
    Account_Number = models.IntegerField(unique=True,blank=True,null=True)
    Account_Holder_Name = models.CharField(max_length=100,blank=True,null=True)
    IFSC_Code = models.CharField(max_length=100,blank=True,null=True)
    Bank_Name = models.CharField(max_length=100,blank=True,null=True)
    Branch_Name = models.CharField(max_length=100,blank=True,null=True)
    Salary_Type = models.CharField(max_length=100,blank=True,null=True)
    Permission_Amount_Per_Hour = models.IntegerField(blank=True,null=True)
    Professional_Tax = models.IntegerField(blank=True,null=True)
    Working_Hours = models.IntegerField(blank=True,null=True)
    Basic_Pay = models.FloatField(blank=True,null=True)
    RD = models.FloatField(blank=True,null=True)
    Casual_Leave_Per_Month = models.IntegerField(blank=True,null=True)
    HRA = models.FloatField(blank=True,null=True)
    PF = models.FloatField(blank=True,null=True)
    Sick_Leave_Per_Month = models.IntegerField(blank=True,null=True)
    Medical_Allowance = models.FloatField(blank=True,null=True)
    ESI = models.IntegerField(blank=True,null=True)
    Over_Time_Amount_Per_Hour = models.FloatField(blank=True,null=True)
    Conveyance_Allowance = models.FloatField(blank=True,null=True)
    Loss_of_Pay_Per_Day = models.FloatField(blank=True,null=True)
    General_Allowance = models.FloatField(blank=True,null=True)
    Net_Salary = models.FloatField(blank=True,null=True)    
    status = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.Employee_Code:  # Only generate code if it's not already set
            last_employee = Employee.objects.all().order_by('id').last()
            if last_employee:
                emp_code = int(last_employee.Employee_Code[3:]) + 1  # Extract the number and increment it
                self.Employee_Code = f'EMP{emp_code:04d}'  # Format it as EMP0001, EMP0002, etc.
            else:
                self.Employee_Code = 'EMP0001'  # Default to EMP0001 if no employees exist
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Employee_Code + "----------------->" + self.Employee_name
    
