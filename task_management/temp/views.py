from django.shortcuts import render
from add_employee.models import AddEmployee

# Create your views here.
def admin(request):
    return  render(request,'temp/admin.html')

def manager(request):
    return  render(request,'temp/manager.html')

def employee(request):
    ss=request.session["u_id"]
    # aa=AddEmployee.objects.get(emp_id=ss)
    # bb=aa.emp_id
    context={
        'k':ss
    }
    return  render(request,'temp/employee.html',context)

def index(request):
    return  render(request,'temp/index.html')

def task(request):
    return render(request,'temp/taskmanager.html')