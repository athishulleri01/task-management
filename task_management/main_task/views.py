from django.shortcuts import render
from main_task.models import MainTask
import datetime
# Create your views here.

def post(request):
    if request.method=='POST':
        ob=MainTask()
        ob.m_id=1
        ob.title=request.POST.get('title')
        ob.file_attach=request.POST.get('file')
        ob.description=request.POST.get('description')
        ob.current_date=datetime.datetime.today()
        ob.start_date=request.POST.get('s_date')
        ob.end_date=request.POST.get('e_date')
        ob.due_date=datetime.datetime.now() # formate not currect
        ob.m_status='pending'
        ob.feedback='pending'
        ob.save()
    return render(request,'main_task/asign_task.html')


def post_feedback(request,idd):
    if request.method=='POST':
        ob=MainTask.objects.get(mt_id=idd)
        ob.feed_date=datetime.datetime.now()
        ob.feedback=request.POST.get('feed')
        ob.save()
    return render(request,'main_task/post_feedback.html')

def view(request):
    ob=MainTask.objects.all()
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


def view_task_to_mngr(request):
    ob = MainTask.objects.all()
    context = {
        'x': ob
    }
    return render(request, 'main_task/view_tasks_to_manager.html', context)