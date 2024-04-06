from django.shortcuts import render
from Portal.models import *
#import requests
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib import auth



def employee_CreateProfile(request):
    r_empId = request.POST['empId']
    r_empFname = request.POST['empFname']
    r_empLname = request.POST['empLname']
    r_email = request.POST['email1']
    r_contact = request.POST['contact']
    r_pan = request.POST['pan']
    r_addhar = request.POST['addhar']
    r_blood = request.POST['blood']
    r_designamtion = request.POST['designation']
    r_department = request.POST['department']
    emp=Employee_Profile(emp_id=r_empId,emp_Fname=r_empFname,emp_Lname=r_empLname,email=r_email,contact_no=r_contact,pancard_no=r_pan,
    adhaar_no=r_addhar,blood_gruop=r_blood,designation=r_designamtion,department=r_department)
    emp.save()
    id=emp.id

    r_addType = request.POST['addType']
    r_addid = request.POST['addid']
    r_addline1 = request.POST['addline1']
    r_addline2 = request.POST['addline2']
    r_city = request.POST['city']
    r_district = request.POST['district']
    r_state = request.POST['state']
    r_pincode = request.POST['pincode']
    r_country = request.POST['country']
    add_det=Address_detail(empid=id,add_type=r_addType,add_id=r_addid,address1=r_addline1,address2=r_addline2,
    zip_code=r_pincode,city=r_city,dist=r_district,country=r_country,state=r_state)
    add_det.save()
#permanent Adress..........
    perm_addType = request.POST['perm_addType']
    perm_addid = request.POST['perm_addid']
    perm_addline1 = request.POST['perm_addline1']
    perm_addline2 = request.POST['perm_addline2']
    perm_city = request.POST['perm_city']
    perm_district = request.POST['perm_district']
    perm_state = request.POST['perm_state']
    perm_pincode = request.POST['perm_pincode']
    perm_country = request.POST['perm_country']
    perm_addr=Permanent_Address(empid=id,add_type=perm_addType,add_id=perm_addid,address1=perm_addline1,address2=perm_addline2,
    zip_code=perm_pincode,city=perm_city,dist=perm_district,country=perm_country,state=perm_state)
    perm_addr.save()
 
    return render(request,'createprofile.html',)
    

# function for View Emp
def employeeview(pk,request):
    try:
        emp = Employee_Profile.objects.get(id = pk)
        addr = Address_detail.objects.get(id = pk)
        perm_addr = Permanent_Address.objects.get(id = pk)
        return {'data':emp,'add_det':addr,'perm_addrs':perm_addr}
    except :
        messages.error(request,'Address_detail.DoesNotExist:')

        

#function for Delete Employee
def deleteEmp(request, pk):
    emp = Employee_Profile.objects.get(id = pk)
    emp.delete()
    messages.success(request, "Employee Deleted Successfully")
    return render(request, 'mainprofile.html')

#function For Update Employee Profile
def updateView(request,pk):
    emp = Employee_Profile.objects.filter(id = pk)
    return render(request,'updateViewEmp.html',{'emp':emp})

def employee_update(request,id):
    emp_id = request.POST['emp_id']
    emp_pro = request.POST['profile']
    emp_first_name = request.POST['emp_first_name']
    emp_last_name = request.POST['emp_last_name']
    email_add = request.POST['email_add']
    contact_no = request.POST['contact_no']
    pancard_no = request.POST['pancard_no']
    adhaar_no = request.POST['adhaar_no']
    blood_group = request.POST['blood_group']
    designation = request.POST['designation']
    r_department = request.POST['department']
    Employee_Profile.get(id = id).update(
        id =id,
        profile_img=emp_pro,
        emp_id = emp_id,
        emp_Fname=emp_first_name,
        emp_Lname= emp_last_name,
        email=email_add,
        contact_no=contact_no,
        pancard_no=pancard_no,
        adhaar_no=adhaar_no,
        blood_gruop=blood_group,
        designation=designation,
        department=r_department
        )
    
    return HttpResponse (status=201)
    



