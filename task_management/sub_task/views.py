from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from sub_task.models import SubTask
from main_task.models import MainTask
from employee.models import Employee
from add_employee.models import AddEmployee
from django.http import HttpResponse
import datetime
from django.db.models import Q
# Create your views here.

def post(request,idd):
    sd=request.session["u_id"]
    obbs = MainTask.objects.get(mt_id=idd)
    b=obbs.title
    obj1 = AddEmployee.objects.filter(type='taskmanager')
    context = {
        'b': obbs,
        'objval1': obj1,
    }

    if request.method=='POST':
        ob=SubTask()
        # ob.m_id=request.POST.get('main')
        # ob.emp_id=request.POST.get('taskmanager')
        # myfile = request.FILES['file']
        # fs = FileSystemStorage()
        # myname = fs.save(myfile.name, myfile)
        # ob.file_attach = myfile.name
        # ob.file_attach=request.POST.get('file')
        # ob.description=request.POST.get('dec')
        # ob.mt_id=sd
        # ob.current_date=datetime.datetime.today()
        # ob.start_date=request.POST.get('s_date')
        # ob.end_date=request.POST.get('e_date')
        # ob.due_date=datetime.datetime.now() # formate not currect
        # ob.st_status='pending'
        # ob.feedback='pending'
        # ob.feed_date=datetime.datetime.now()
        ob.save()
        obk=MainTask.objects.get(mt_id=idd)
        obk.task_manager_id=request.POST.get('employee')
        obk.task_asign_tm_date=datetime.datetime.now()

        obk.task_mng_desc=request.POST.get('dec')
        obk.task_due_tm_date=request.POST.get('d_date')
        obk.task_deadline_tm_date=request.POST.get('dd_date')
        obj=AddEmployee.objects.get(emp_id=obk.task_manager_id)
        obk.task_mngr_nm=obj.name
        obk.save()
    return render(request,'sub_task/sub_asign.html',context)




# def post_subtask(request):




def view_s_feed(request):
    ob = SubTask.objects.all()
    context = {
        'x': ob
    }
    return render(request, 'sub_task/view_feedback.html', context)

def vw_sub_status(request):
    ob = SubTask.objects.all()
    context = {
        'x': ob
    }
    return render(request, 'sub_task/view_subtask_status.html', context)

#
# def view_subtask_tskmngr(request):
#     ss = request.session["u_id"]
#     # ab=AddEmployee.objects.get(emp_id=ss)
#     ob = MainTask.objects.all()
#     context = {
#         'x': ob
#     }
#     return render(request, 'sub_task/view_subtask.html', context)


def vw_subtask_tsmngr(request):
    ss= request.session["u_id"]
    ob = MainTask.objects.filter(task_manager_id=ss)
    obb=SubTask.objects.filter(tm_id=ss)
    count=0
    for i in obb:
        if (i.status =='complete'):
            count=count+1
            # print(count)
    a=len(obb)
    context = {
        'x': ob,
        'k':str(count),
        'o':str(a)
    }
    return render(request, 'sub_task/view_subtask.html', context)


def submit_work(request,idd):
    ob=MainTask.objects.get(mt_id=idd)
    ob.status='complete'
    ob.save()
    return vw_subtask_tsmngr(request)


def assignemp(request,idd):
    sd = request.session["u_id"]
    obbs = MainTask.objects.get(mt_id=idd)
    b = obbs.title
    obj1 = AddEmployee.objects.filter(type='employee')
    context = {
        'b': obbs,
        'objval1': obj1,
    }
    if request.method == 'POST':
        ob = SubTask()
        # ob.m_id=request.POST.get('main')
        ob.emp_id = request.POST.get('employee')
        ob.file_attach = request.POST.get('file')
        ob.description = request.POST.get('dec')
        ob.tm_id=obbs.task_manager_id
        ob.subtitle=request.POST.get('s_title')
        ob.mt_id=obbs.mt_id
        ob.assign_date=datetime.datetime.now()
        ob.deadline=request.POST.get('dd_date')
        ob.due_date=request.POST.get('d_date')
        ob.status='not started'
        ob.save()
    return render(request,'sub_task/sub_asign_to_emp.html',context)



def view_task_to_employee(request):
    ss=request.session["u_id"]
    # ab=AddEmployee.objects.get(emp_id=ss)

    # ob = SubTask.objects.filter(emp_id=ss)
    ob = SubTask.objects.filter(Q(emp_id=ss) & (Q(status='not started') | Q(status='reject')))
    context = {
        'p': ob
    }
    return render(request, 'sub_task/view_tasks_emplo.html', context)



def post_emp_work(request,idd):
    ob = SubTask.objects.get(st_id=idd)
    context = {
        'x': ob
    }
    if request.method=='POST':
        ob=SubTask.objects.get(st_id=idd)
        ob.s_description=request.POST.get('s_dec')
        # ob.s_file_attach1=request.POST.get('file1')
        myfile = request.FILES['file1']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.s_file_attach1 = myfile.name

        # ob.s_file_attach2 = request.POST.get('file2')
        myfile = request.FILES['file2']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.s_file_attach2=myfile.name
        ob.s_file_attach1 = myfile.name
        ob.s_submit_date=datetime.datetime.today()
        ob.s_submit_time=datetime.datetime.now()
        ob.status='complete'
        ob.save()

    return render(request, 'sub_task/submit_task_emp.html', context)



def view_taskstatus_taskmanager(request):
    # ss=request.session["u_id"]
    ob = SubTask.objects.filter(status='complete')
    context = {
        'p': ob
    }
    return render(request, 'sub_task/view_subtask_taskmanager.html', context)

def view_emp_submit_workss(request):
    # ss=request.session["u_id"]
    ob = SubTask.objects.filter(status='complete')
    context = {
        'p': ob
    }
    return render(request, 'sub_task/view_emp_submit_work.html', context)

def rjct(request,idd):
    obj=SubTask.objects.get(st_id=idd)
    obj.status='reject'
    obj.save()
    return view_emp_submit_workss(request)