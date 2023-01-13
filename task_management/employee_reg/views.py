from django.shortcuts import render
from employee_reg.models import EmpRegister
from login.models import Login
# Create your views here.
def post(request):
    if request.method=='POST':
        ob=EmpRegister()
        ob.name=request.POST.get('uname')
        ob.password='12345'
        ob.age=request.POST.get('age')
        ob.address=request.POST.get('address')
        ob.email=request.POST.get('email')
        ob.qualification=request.POST.get('qualification')
        ob.experience=request.POST.get('exp')
        ob.department=request.POST.get('department')
        ob.status=' '
        ob.dob=request.POST.get('dob')
        ob.contact_no=request.POST.get('cont_no')
        ob.job_id=0
        ob.rating=0
        ob.save()

        obj = Login()
        obj.username=ob.name
        obj.password=ob.contact_no
        obj.u_id=ob.emp_id
        obj.type="employee"
        obj.save()

    return render(request,'employee_reg/registration.html')

def update_status(request,idd):
    if request.method=='POST':
        ob=EmpRegister.objects.get(emp_id=idd)
        ob.status=request.POST.get('noof')
        ob.save()
    return render(request,'employee_reg/update_status.html')

def view(request):
    ob=EmpRegister.objects.all()
    context={
        'objval':ob
    }
    return render(request,'employee_reg/view_emp_details.html',context)



def view_prof(request):
    ob=EmpRegister.objects.all()
    context={
        'objval':ob
    }
    return render(request,'employee_reg/profile.html',context)