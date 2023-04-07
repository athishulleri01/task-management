from django.shortcuts import render
from manager.models import Manager
from add_employee.models import AddEmployee
from  department.models import  Department
from login.models import Login
# Create your views here.

def post(requset):
    obb=AddEmployee.objects.filter(usertype='employee')
    obj=Department.objects.all()
    context={
        'objval':obb,
        'objval1':obj
    }
    if requset.method=='POST':
        aa=requset.POST.get('mm')
        ob=Manager()
        ob.emp_id=requset.POST.get('mm')
        ob.dept_id=requset.POST.get('nn')
        ob.start_date=requset.POST.get('jj')
        ob.end_date = requset.POST.get('ee')
        ob.save()

        obk=Login.objects.get(u_id=aa,type='employee')
        obk.type='manager'
        obk.save()

        obj=AddEmployee.objects.get(emp_id=aa)
        obj.post='manager'
        obj.save()

    return render(requset,'manager/select.html',context)