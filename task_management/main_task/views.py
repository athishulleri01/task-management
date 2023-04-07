from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from main_task.models import MainTask
from employee.models import AddEmployee
import datetime
# Create your views here.

def post(request):
    obk= AddEmployee.objects.filter(type='manager')
    context = {
        'ok':obk
    }

    if request.method=='POST':
        ob=MainTask()
        ob.emp_id=request.POST.get('stname')
        ob.title=request.POST.get('tname')
        ob.file_attach=request.POST.get('file')
        ob.description=request.POST.get('description')
        ob.department=request.POST.get('crs')
        ob.assign_date=datetime.datetime.today()
        ob.end_date=request.POST.get('e_date')
        ob.due_date=datetime.datetime.now() # formate not currect
        ob.m_status='Not Start'
        ob.status='selected'
        ob.feedback='No any feedbak'
        ob.task_mngr_nm=''
        ob.tskmgr_submit = ''
        # ob.status='none'
        ob.save()
    return render(request,'main_task/asign_task.html',context)

from django.http import JsonResponse

def selectemployee(request):
    cid=request.GET.get("cid")
    print('hello')
    print(cid)
    st=AddEmployee.objects.filter(department=cid,type='Manager')
    emplist=[]
    empid=[]
    print(len(st))
    for s in st:
        emplist.append(s.name)
        empid.append(str(s.emp_id))

    print(empid)
    context={
        'emplis':emplist,
        'emid':empid
    }
    return JsonResponse(context)

def post_feedback(request,idd):
    if request.method=='POST':
        ob=MainTask.objects.get(mt_id=idd)
        ob.feed_date=datetime.datetime.now()
        ob.feedback=request.POST.get('feed')
        ob.save()
    return render(request,'main_task/post_feedback.html')

def view(request):
    ss = request.session["u_id"]
    ob=MainTask.objects.filter(emp_id=ss)
    context={
        'objval':ob
    }
    return render(request,'main_task/view_task.html',context)


def viewd(request,idd):
    ob=MainTask.objects.filter(mt_id=idd)
    context={
        'x':ob
    }
    return render(request,'main_task/task_desription.html',context)

def vwad(request):
    ob = MainTask.objects.all()
    context = {
        'x': ob
    }
    return render(request, 'main_task/viewadmn.html', context)

def view_m_status(request):
    ob = MainTask.objects.all()
    context = {
        'x': ob
    }
    return render(request, 'main_task/view_m_task_status.html', context)

def delete(request,idd):
    ob=MainTask.objects.filter(mt_id=idd)
    ob.delete()
    ob1 = MainTask.objects.filter(mt_id=idd)
    ob1.delete()
    return view_m_status(request)


def view_task_to_mngr(request):
    ss=request.session["u_id"]
    # ab=AddEmployee.objects.get(emp_id=ss)
    ob = MainTask.objects.filter(emp_id=ss)

    context = {
        'p': ob
    }
    return render(request, 'main_task/view_tasks_to_manager.html', context)




def view_task_status_mngr(request):
    ss=request.session["u_id"]
    # ab=AddEmployee.objects.get(emp_id=ss)
    ob = MainTask.objects.filter(emp_id=ss)
    context = {
        'p': ob
    }
    return render(request, 'main_task/view_task_status_manager.html', context)


def view_task_admin(request):
    ob = MainTask.objects.all()
    context = {
        'x1': ob
    }
    return render(request, 'main_task/view_task_admin.html', context)
def viewm(request):
    ob=AddEmployee.objects.all()
    context={
        'x':ob
    }
    return render(request,'main_task/view_tasks_to_manager.html',context)

def view_submi_task_mngr(request):
    ss=request.session["u_id"]
    ob = MainTask.objects.filter(emp_id=ss)
    context = {
        'x1': ob
    }
    return render(request, 'main_task/view_submited_task_mngr.html', context)


# def post_summary(request,idd):
#     if request.method=='POST':
#         obj=MainTask()
#         obj.m_id=1
#         obj.mt_id=idd
#         obj.summary=request.POST.get('summary')
#         obj.sum_date=datetime.datetime.now()
#         obj.save()
#     return render(request,'summary/post_summary.html')



def view_feed_mngr(request):
    ss=request.session["u_id"]
    # ab=AddEmployee.objects.get(emp_id=ss)
    ob = MainTask.objects.filter(emp_id=ss)
    context = {
        'p': ob
    }
    return render(request, 'main_task/view_feed_mngr.html', context)

def tsmnr_submit(request):
    ss = request.session["u_id"]
    if request.method=='POST':
        ob=MainTask.objects.get(task_manager_id=ss)
        myfile = request.FILES['ff']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.tskmgr_submit = myfile.name
        ob.m_status='complete'
        ob.save()
    return render(request, 'main_task/tsmngr_submit_work.html')

def submit(request,idd):
    obj=MainTask.objects.get(mt_id=idd)
    obj.m_status="complete"
    obj.save()
    return view_submi_task_mngr(request)

def view_compltd_work_admin(request,idd):
    ob = MainTask.objects.filter(mt_id=idd)
    context = {
        'p': ob
    }
    return render(request, 'main_task/view_complte_task_admin.html', context)
