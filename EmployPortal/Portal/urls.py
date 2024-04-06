from django.urls import path

from Portal import views
urlpatterns = [
    path('', views.Login,name='login'),
    path('login/', views.loginsubmit,name='login1'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('contact_list/', views.contact_list, name='contact_list'),
    

    path('pindex/', views.EmpProfile,name='pindex'),
    path('view/<int:pk>/',views.viewEmp,name='viewEmp'),
    path('update/<int:pk>/',views.Emp_updateView, name='updateEmp'),
    path('edit/<int:pk>/',views.Emp_update, name='edit'),
    path('delete/<int:pk>/',views.deleteEmp,name='deleteEmp'),
    path('mainprofile/', views.MainProfile,name='mainprofile'),
    path('createprofile/', views.CreateProfile,name='createprofile'),
    path('PassGenrator/<int:pk>/',views.PassGenrator,name='PassGenrator'),
    path('PassGenratorsubmit/<int:pk>/',views.PassGenratorsubmit,name='PassGenratorsubmit'),
#task_add
    path('task_add/', views.task_add,name='task_add'),
    path('taskstatus/', views.Task_status, name='taskstatus'),
    path('createtask/', views.task,name='createtask'),
    path('tasklist/', views.Task_list,name='tasklist'),
    path('viewtasklist/<int:pk>/',views.View_task_list,name='viewtasklist'),
    path('updatetaskview/<int:pk>/',views.Update_task_list_view, name='updatetaskview'),
    path('edittask/<int:id>/',views.Update_task_list, name='edittask'),
    path('deletetask/<int:pk>/',views.deleteTask,name='deletetask'),
    path('logout/', views.Logout, name='logout'),
    # path('update/', views.Update, name='update'),
    # path('updatetask/', views.UpdateTask, name='updatetask')

    #Department
    path('Department_list/', views.Department_list, name='Department_list'),
    path('Department_add/', views.Department_add, name='Department_add'),
    path('Department_add_submit/', views.Department_add_submit, name='Department_add_submit'),
    path('Department_update/<int:pk>/',views.Department_update, name='Department_update'),
    path('Department_update_submit/<int:id>/',views.Department_update_submit, name='Department_update_submit'),
    path('delete_department/<int:id>/',views.delete_department,name='delete_department'),

    #Designation
    path('Designation_list/', views.Designation_list, name='Designation_list'),
    path('Designation_add/', views.Designation_add, name='Designation_add'),
    path('Designation_add_submit/', views.Designation_add_submit, name='Designation_add_submit'),
    path('Designation_update/<int:pk>/',views.Designation_update, name='Designation_update'),
    path('Designation_update_submit/<int:id>/',views.Designation_update_submit, name='Designation_update_submit'),
    path('delete_designation/<int:id>/',views.delete_designation,name='delete_designation'),

    #contactus_view
    path('contactus_view/', views.contactus_view, name='contactus_view'),
    path('ContactSubmit/', views.ContactSubmit, name='ContactSubmit'),

]
