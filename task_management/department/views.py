from django.shortcuts import render
from department.models import Department
# Create your views here.
def post(request):
    if request.method=='POST':
        ob=Department()
        ob.name=request.POST.get('dept')
        ob.description=request.POST.get('dept_dec')
        ob.status=''
        ob.save()
    return render(request,'department/create.html')

def view_dept(request):
    ob=Department.objects.all()
    context={
        'objval':ob
    }
    return render(request,'department/view_dpmt.html',context)

