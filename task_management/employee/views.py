from django.shortcuts import render
from employee.models import Employee
from add_employee.models import AddEmployee
from main_task.models import MainTask
from department.models import  Department
from sub_task.models import SubTask
# Create your views here.

def post(request):
    obb = AddEmployee.objects.filter(usertype='employee')
    ss=request.session["u_id"]
    obj=Department.objects.all()
    context={
        'objval':obb,
        'objval1':obj
    }
    if request.method=='POST':
        ob=Employee()
        ob.emp_id=request.POST.get('mm')
        ob.dept_id=request.POST.get('nn')
        ob.start_date=request.POST.get('jj')
        ob.m_id=ss
        ob.mt_id=1
        ob.save()
    return render(request,'employee/add_employee.html',context)

def vw_mid_emp(request):
    # ss = request.session["u_id"]
    # ob = Employee.objects.filter(m_id=ss)
    ob = AddEmployee.objects.all()
    context = {
        'x': ob
    }
    return render(request, 'employee/view_mid_emp.html', context)



def vw_emlpo_status_mangr(request):
    ss = request.session["u_id"]
    ob1 = Employee.objects.filter(m_id=ss)
    ob = MainTask.objects.filter(emp_id=ss)
    context = {
        'x': ob,
        'y':ob1
    }
    return render(request, 'employee/view_employee_status_manager.html', context)


def vw_manager_profile(request):
    ss = request.session["u_id"]
    ob1 = Employee.objects.filter(m_id=ss)
    context = {
        'x': ob1
    }
    return render(request, 'employee/manager_profile.html', context)


def vw_tasmanager_profile(request):
    ss = request.session["u_id"]
    ob1 = Employee.objects.filter(m_id=ss)
    context = {
        'x': ob1
    }
    return render(request, 'employee/taskmanager_profile.html', context)

def vw_employee_profile(request):
    ss = request.session["u_id"]
    ob1 = Employee.objects.filter(m_id=ss)
    context = {
        'x': ob1
    }
    return render(request, 'employee/employee_profile.html', context)


def vw_emp_stus_mnggr(request):
    ss = request.session["u_id"]
    ob = MainTask.objects.filter(emp_id=ss)
    context = {
        'x': ob
    }
    return render(request, 'employee/view_employee_status_manager.html', context)


def vw_emp_stus_tskmngr(request):
    ss = request.session["u_id"]
    ob = SubTask.objects.filter(tm_id=ss)
    context = {
        'x': ob
    }
    return render(request, 'employee/view_emp_sts_tsmngr.html', context)
