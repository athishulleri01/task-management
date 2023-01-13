from django.shortcuts import render
from employee.models import Employee
from employee_reg.models import EmpRegister
from  department.models import  Department
# Create your views here.

def post(requset):
    obb=EmpRegister.objects.all()
    obj=Department.objects.all()
    context={
        'objval':obb,
        'objval1':obj
    }
    if requset.method=='POST':
        ob=Employee()
        ob.emp_id=requset.POST.get('mm')
        ob.dept_id=requset.POST.get('nn')
        ob.start_date=requset.POST.get('jj')
        ob.save()
    return render(requset,'employee/add_employee.html',context)