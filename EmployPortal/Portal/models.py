from django.db import models


# Create your models here.
class LoginAuthentication(models.Model):
    name= models.CharField(max_length=50,default='',null=True)
    username= models.CharField(max_length=50,default='admin',unique=True)
    userpassword= models.CharField(max_length=50,default='admin')
    role= models.CharField(max_length=50, default='Admin')

class Employee_Profile(models.Model):
    username= models.CharField(max_length=200,default='',null=True)
    userpassword= models.CharField(max_length=200,default='',null=True)
    emp_id = models.IntegerField()
    emp_Fname = models.CharField(max_length=200,default='')
    emp_Lname = models.CharField(max_length=200,default='')    
    email = models.EmailField(max_length=200,default='')
    contact_no= models.CharField(max_length=200)
    pancard_no= models.CharField(max_length=200)
    adhaar_no= models.CharField(max_length=100) 
    blood_gruop = models.CharField(max_length=200) 
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=200,default='')
    
    

    
class Address_detail(models.Model):
    add_type=models.CharField(max_length=30,default='cuurent address')
    empid=models.CharField(max_length=30 ,default='empid')
    add_id=models.CharField(max_length=30)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    dist = models.CharField(max_length=100)
    state = models.CharField(max_length=100,default='uppp')
    country = models.CharField(max_length=30)
        

class Permanent_Address(models.Model):
    add_type=models.CharField(max_length=30,default='permanent address')
    empid=models.CharField(max_length=30,default='empid')
    add_id=models.CharField(max_length=30)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    dist = models.CharField(max_length=100)
    state = models.CharField(max_length=100,default='uppp')
    country = models.CharField(max_length=30)

class Task(models.Model):
    task_description = models.CharField(max_length=200)
    assigned_by = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=200)
    assigned_date =  models.CharField(max_length=200)
    complition_date =  models.CharField(max_length=200)
    task_status = models.CharField(max_length=100,default="Pending")

class Department(models.Model):
    name= models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=200)

class Designation(models.Model):
    name= models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=200)
    

class Rel_EmpProfile_Add_details(models.Model):
    emp_id=models.CharField(max_length=100)
    add_detail=models.CharField(max_length=100)
    

    
  
  
  
