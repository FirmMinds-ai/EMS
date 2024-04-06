from audioop import reverse
from django.shortcuts import render
from django.contrib import messages
# from datetime import date
from .models import *
# import requests
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib import auth
from Portal.module.employee.employee_management import *
from django.urls import reverse
from django.utils.dateparse import parse_datetime
import requests
import json

# Create your views here.
def Login(request):
    return render(request,'login.html')    
         

def dash(request):
    name=request.session['name']
    role=request.session['role']
    return render(request,'dashboard.html',{'role':role})
    
        
def loginsubmit(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['upassword']
        try:            
            roledata = LoginAuthentication.objects.get(username=uname,userpassword=passwd).role
            ename = LoginAuthentication.objects.get(username=uname,userpassword=passwd).name
            request.session['role'] = roledata
            role=request.session['role']
            request.session['name'] = ename
            name=request.session['name']    
            if role == "admin" or role =="employee":               
                return HttpResponseRedirect('/dashboard/')
            else:
                messages.error(request,'Invalid User name or Password')
                return HttpResponseRedirect('/')
        except:
            messages.error(request,'Invalid User name or Password')
            return HttpResponseRedirect('/')                        
    else:
        messages.error(request,'Invalid User name or Password')
        return HttpResponseRedirect('/')


def Dashboard(request):
    role=request.session['role']
    data= Employee_Profile.objects.all()
    # add_det= Address_detail.objects.all()
    return render(request, 'dashboard.html',{'data':data,'role':role})
    

def MainProfile(request):
    role=request.session['role']
    data= Employee_Profile.objects.all()
    return render(request, 'mainprofile.html',{'data':data,'role':role})


def EmpProfile(request):
    role=request.session['role']
    data= Employee_Profile.objects.all()
    add_det= Address_detail.objects.all()
    return render(request, 'pindex.html',{'data':data,'addr':add_det,'role':role})

def CreateProfile(request):
    if request.method == "POST":
        employee_CreateProfile(request) 
        messages.success(request, "Employee created succesfully")
        return HttpResponseRedirect('/mainprofile/')
    else:
        role=request.session['role']
        desig= Designation.objects.all()
        depart= Department.objects.all()
        return render(request,'createprofile.html',{'depart':depart,'desig':desig,'role':role})

# function for View Emp
def viewEmp(request,pk):
    role=request.session['role']
    emp = employeeview(pk,request)
    emp = emp['data']
    addr = employeeview(pk,request)
    addr=addr['add_det']
    perm_addr = employeeview(pk,request)
    perm_addr=perm_addr['perm_addrs']
    return render(request, 'viewEmp.html',{'emp':emp,'addr':addr,'perm_addr':perm_addr,'role':role})

#function for Delete Employee
def deleteEmp(request, pk):
    emp = Employee_Profile.objects.get(id = pk)
    addr = Address_detail.objects.get(id = pk)
    perm_addr = Permanent_Address.objects.get(id = pk)
    emp.delete()
    addr.delete()
    perm_addr.delete()
    messages.success(request, "Employee Deleted Successfully")
    return HttpResponseRedirect('/mainprofile/')

#function For Update Employee Profile
def Emp_updateView(request,pk):
    role=request.session['role']
    emp = Employee_Profile.objects.get(id = pk)
    desig= Designation.objects.all()
    depart= Department.objects.all()
    return render(request,'updateViewEmp.html',{'emp':emp,'depart':depart,'desig':desig,'role':role})

def Emp_update(request,pk):
    if request.method =="POST":
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
        Employee_Profile.objects.filter(id=pk).update(
        id =pk,
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
        messages.success(request, "Employee Updated Successfully")
        return HttpResponseRedirect('/mainprofile/')
    else:
        return HttpResponseRedirect('/mainprofile/')

def task_add(request):
    name=request.session['name']
    role=request.session['role']
    edata=Employee_Profile.objects.all()
    return render(request, 'createtask.html',{'edata':edata,'role':role,'name':name})

def task(request):
    if request.method == "POST":
        description = request.POST['description']
        assignedBy = request.POST['assignedBy']
        assignedTo = request.POST['assignedTo']
        assignedDate = request.POST['assignedDate']
        complitionDate = request.POST['complitionDate']
        status = request.POST['status']
        TASK=Task(task_description=description,assigned_by=assignedBy,assigned_to=assignedTo,assigned_date=assignedDate,complition_date=complitionDate,task_status=status)
        TASK.save()
        messages.success(request,"Task Created Successfully")
        return render(request, 'createtask.html')
    else:
        return render(request, 'createtask.html')


def Task_list(request):
    name=request.session['name']
    role=request.session['role']
    data=Task.objects.all()
    return render(request, 'tasklist.html',{'data':data,'role':role,'name':name})



def View_task_list(request,pk):
    name=request.session['name']
    role=request.session['role']
    TASK = Task.objects.get(id = pk)
    return render(request, 'viewtasklist.html',{'task':TASK,'role':role,'name':name})

def Update_task_list_view(request,pk):
    edata=Employee_Profile.objects.all()
    role=request.session['role']
    task = Task.objects.get(id = pk)
    return render(request,'updateTaskList.html',{'task':task,'role':role,'edata':edata})

def Update_task_list(request,id):
    if request.method =="POST":
        task_description = request.POST['task_description']
        # assigned_by = time.strptime(request.POST['assigned_by'], "%m/%d/%Y")
        # assigned_by = time.strptime(request.POST['assigned_to'], "%m/%d/%Y")
        assigned_by = request.POST['assigned_by']
        assigned_to = request.POST['assigned_to']
        assigned_date = parse_datetime(request.POST['assigned_date'])
        complition_date = request.POST['complition_date']
        status = request.POST['status']
        T_update = Task(
        id =id,
        task_description = task_description,
        assigned_by= assigned_by,
        assigned_to = assigned_to,
        assigned_date = assigned_date,
        complition_date = complition_date ,
        task_status =status
        )
        T_update.save()
        messages.success(request,"Task Updated Successfully")
        return HttpResponseRedirect('/taskstatus/')
    else:
        return HttpResponseRedirect('/taskstatus/')
        
    


def Task_status(request):
    name=request.session['name']
    role=request.session['role']
    status=Task.objects.all()
    return render(request, 'taskstatus.html',{'status':status,'role':role,'name':name})
    
    
def deleteTask(request, pk):
    delTask = Task.objects.get(id = pk)
    delTask.delete()
    messages.success(request, "Task Deleted Successfully")
    return HttpResponseRedirect('/taskstatus/')

def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

#Department_add_submit
def Department_list(request):
    role=request.session['role']
    data=Department.objects.all()
    return render(request, 'Department_list.html',{'Deprt':data,'role':role})

def Department_add(request):
    role=request.session['role']
    data=Department.objects.all()
    return render(request, 'Department_add.html',{'data':data,'role':role})
def Department_add_submit(request):
    if request.method == "POST":
        deptname = request.POST['dname']
        descp = request.POST['description'] 
        Dept=Department(description=descp,name=deptname)
        Dept.save()
        messages.success(request,"Department Created Successfully")
        return HttpResponseRedirect('/Department_list/')
    else:
        messages.error(request,"Department name allready added")
        return HttpResponseRedirect('/Department_list/')
    

def Department_update(request,pk):
    role=request.session['role']
    dept = Department.objects.get(id = pk)
    return render(request,'Department_update.html',{'dept':dept,'role':role})

def Department_update_submit(request,id):
    if request.method =="POST":
        deptname = request.POST['dname']
        descp = request.POST['description']
        Dep_update = Department(id =id,description=descp,name=deptname)
        Dep_update.save()
        messages.success(request,"Department Updated Successfully")
        return HttpResponseRedirect('/Department_list/')
    else:
        messages.error(request,"Invalid Credentials")
        return HttpResponseRedirect('/Department_list/')
def delete_department(request,id):
    d_details = Department.objects.get(id=id)
    # if rel_Subnet6_Name_server.objects.filter(name_server_id = ns_details.id).exists():
    #     messages.error(request, 'Name server "'+ns_details.name_servers+'" assigned to subnet')
    #     return HttpResponseRedirect('/name_server_list/')
    # else:
    d_details.delete()  
    messages.success(request, 'Department deleted successfully')
    return HttpResponseRedirect('/Department_list/')



#Designation
def Designation_list(request):
    role=request.session['role']
    data=Designation.objects.all()
    return render(request, 'Designation_list.html',{'data':data,'role':role})

def Designation_add(request):
    role=request.session['role']
    data=Designation.objects.all()
    return render(request, 'Designation_add.html',{'data':data,'role':role})
def Designation_add_submit(request):
    if request.method == "POST":
        deptname = request.POST['dname']
        descp = request.POST['description'] 
        Dept=Designation(name=deptname,description=descp)
        Dept.save()
        messages.success(request,"Designation Created Successfully")
        return HttpResponseRedirect('/Designation_list/')
    else:
        messages.error(request,"Designation name allready added")
        return HttpResponseRedirect('/Designation_list/')

def Designation_update(request,pk):
    role=request.session['role']
    desig = Designation.objects.get(id = pk)
    return render(request,'Designation_update.html',{'desig':desig,'role':role})

def Designation_update_submit(request,id):
    if request.method =="POST":
        designame = request.POST['dname']
        descp = request.POST['description']
        Dep_update = Designation(id =id,description=descp,name=designame)
        Dep_update.save()
        messages.success(request,"Designation Updated Successfully")
        return HttpResponseRedirect('/Designation_list/')
    else:
        messages.error(request,"Invalid Credentials")
        return HttpResponseRedirect('/Designation_list/')

def delete_designation(request,id):
    d_details = Designation.objects.get(id=id)
    # if rel_Subnet6_Name_server.objects.filter(name_server_id = ns_details.id).exists():
    #     messages.error(request, 'Name server "'+ns_details.name_servers+'" assigned to subnet')
    #     return HttpResponseRedirect('/name_server_list/')
    # else:
    d_details.delete()  
    messages.success(request, 'Designation deleted successfully')
    return HttpResponseRedirect('/Designation_list/')


def PassGenrator(request,pk):
    role=request.session['role']
    Empdt=Employee_Profile.objects.get(id = pk)
    #LoginAuthentication(username=,userpassword=,role="emp")
    return render(request,'PwdGen.html',{'Empdt':Empdt,'role':role})

def PassGenratorsubmit(request,pk):   
    if request.method == "POST":
        Username = request.POST['Username']
        Password = request.POST['Password']
        Name = request.POST['name']
        try:
            Employee_Profile.objects.filter(id = pk).update(username=Username,userpassword=Password) 
            LoginAuthentication(username=Username,userpassword=Password,name=Name,role="employee").save()
            messages.success(request,"Password Created Successfully")
            return HttpResponseRedirect('/mainprofile/')
        except:
            messages.error(request,"Username already taken please enter new username")
            return HttpResponseRedirect(reverse('PassGenrator',args=[pk]))
    else:
        messages.error(request,"Invalid credentials")
        return render(request, 'PwdGen.html')
    
def contactus_list(request):
    role=request.session['role']
    return render(request, 'contactus.html',{'role':role})

def contact_list(request):
    role=request.session['role']
    url="https://5rzr6jd8b8.execute-api.us-east-1.amazonaws.com/v1/contactform"
    headers = {'content-type':'application/json'}
    r = requests.get(url,headers=headers)
    api_request = json.loads(r.content)
    if r.status_code == 200:
        return render(request, 'contact_list.html',{'role':role,'data':api_request})
    else:
        return render(request, 'contact_list.html',{'role':role})

def contactus_view(request):
    role=request.session['role']
    return render(request, 'contactus.html',{'role':role})

def ContactSubmit(request):
    if request.method =='POST':
        name = request.POST['Name']
        email = request.POST['Email']      
        Mob = request.POST['Mobile']
        Sub = request.POST['Subject']
        Message = request.POST['Message']
        url = 'https://5rzr6jd8b8.execute-api.us-east-1.amazonaws.com/v1/contactform'
        headers = {'content-type':'application/json'}
        data = {
            'name':name,
            'email':email,
            'mobile':Mob,
            'subject':Sub,
            'message':Message
            }
        r = requests.post(url, data = json.dumps(data), headers=headers)
        if r.status_code ==200:
          messages.success(request, 'Your message sent successfully ')
          return HttpResponseRedirect('/dashboard/')
        #   return HttpResponseRedirect('/contactussuccess')
        else:
          messages.warning(request,'Invalid Credentials')
          return HttpResponseRedirect('/contactus_view/')
    else:
        messages.warning(request,'Method not found')
        return HttpResponseRedirect('/contactus_view/')