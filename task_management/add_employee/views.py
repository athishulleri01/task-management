from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from add_employee.models import AddEmployee
from department.models import Department
from login.models import Login
from django.db.models import Q
# Create your views here.
def post(request):
    obc=""
    obk = Department.objects.all()

    if request.method=='POST':
        a=request.POST.get('pass')
        b=request.POST.get('email')
        obv=AddEmployee.objects.filter(Q(password=a)&Q(email=b)|Q(password=a)&Q(email=b)| Q(email=b))
        if len(obv)>0:
            obc="User"

        else:
            ob=AddEmployee()
            # ob.photo=request.POST.get('img')
            myfile=request.FILES['img']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            ob.photo=myfile.name
            # myfile=request.FILES['photo']
            # fs=FileSystemStorage()
            # filename=fs.save(myfile.name,myfile)
            # ob.photo=myfile.name
            ob.name=request.POST.get('uname')
            ob.password=request.POST.get('pass')
            ob.address=request.POST.get('address')
            ob.email=request.POST.get('email')
            ob.qualification=request.POST.get('qualification')
            ob.experience=request.POST.get('exp')
            ob.department=request.POST.get('dpt')
            ob.dob=request.POST.get('dob')
            ob.contact_no=request.POST.get('cont_no')
            ob.type=request.POST.get('post')
            ob.join_date=request.POST.get('jdate')
            ob.employee_id=request.POST.get('empid')
            ob.save()
            obj = Login()
            obj.username=ob.email
            obj.password=ob.password
            obj.u_id=ob.emp_id
            obj.type=ob.type

            # obvs=AddEmployee.objects.filter(Q(department=ob.department) & Q(type='Manager'))
            # if len(obvs)!=0:
            #     obj.type=''
            #     print('already exist')
            # else:
            obj.save()
            # obj1 =Department()
            # obj1.status='exist'
            # obj1.save()
            obc="succ"
    context = {
        'ok': obk,
        'msg':obc
        }

    return render(request, 'add_employee/registration.html',context)

def update_status(request,idd):
    if request.method=='POST':
        ob=AddEmployee.objects.get(emp_id=idd)
        ob.status=request.POST.get('noof')
        ob.save()
    return render(request, 'add_employee/update_status.html')

def view(request):
    ob=AddEmployee.objects.all()
    context={
        'objval':ob
    }
    return render(request, 'add_employee/view_emp_details.html', context)



def view_prof(request):
    ss=request.session["u_id"]
    ob=AddEmployee.objects.filter(emp_id=ss)
    context={
        'objval':ob
    }
    return render(request, 'add_employee/profile.html', context)


def edu(request, idd):
    ob1 = AddEmployee.objects.get(emp_id=idd)
    context = {
        'x': ob1
    }
    if request.method=='POST':
        ob=AddEmployee.objects.get(emp_id=idd)
        ob.photo=request.POST.get('img')
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        ob.photo=myfile.name
        ob.password=request.POST.get('pass')
        ob.email=request.POST.get('email')
        ob.contact_no=request.POST.get('cont_no')
        ob.save()
        return view_prof(request)
    return render(request, 'add_employee/edit_profile.html',context)



def view_prof_t(request):
    ss=request.session["u_id"]
    ob=AddEmployee.objects.filter(emp_id=ss)
    context={
        'objval':ob
    }
    return render(request, 'add_employee/profile_t.html', context)


def edu_t(request, idd):
    ss = request.session["u_id"]
    ob1 = AddEmployee.objects.get(emp_id=idd)
    context = {
        'x': ob1
    }
    if request.method=='POST':
        ob=AddEmployee.objects.get(emp_id=idd)
        ob.photo=request.POST.get('img')
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        ob.photo=myfile.name
        ob.password=request.POST.get('pass')
        ob.email=request.POST.get('email')
        ob.contact_no=request.POST.get('cont_no')
        ob.save()

        obk=Login.objects.get(u_id=ss,type="taskmanager")
        obk.password=request.POST.get('pass')
        obk.save()
        return view_prof(request)
    return render(request, 'add_employee/edit_profile_t.html',context)


def view_prof_m(request):
    ss=request.session["u_id"]
    ob=AddEmployee.objects.filter(emp_id=ss)
    context={
        'objval':ob
    }
    return render(request, 'add_employee/profile_m.html', context)


def edu_m(request, idd):
    ss=request.session["u_id"]
    ob1 = AddEmployee.objects.get(emp_id=idd)
    context = {
        'x': ob1
    }
    if request.method=='POST':
        ob=AddEmployee.objects.get(emp_id=idd)
        ob.photo=request.POST.get('img')
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        ob.photo=myfile.name
        ob.password=request.POST.get('pass')
        ob.email=request.POST.get('email')
        ob.contact_no=request.POST.get('cont_no')
        ob.save()

        obk=Login.objects.get(u_id=ss,type="Manager")
        obk.password=request.POST.get('pass')
        obk.save()
        return view_prof(request)
    return render(request, 'add_employee/edit_profile_m.html',context)