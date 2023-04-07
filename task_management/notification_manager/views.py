from django.shortcuts import render
from notification_manager.models import NotificationManager
from notification_admin.models import NotificationAdmin
import datetime
from django.db.models import Q
# Create your views here.

def post_notification(request):
    sd = request.session["u_id"]
    if request.method=='POST':
        obj=NotificationAdmin()
        obj.tile=request.POST.get('title')
        obj.description=request.POST.get('description')
        obj.date=datetime.datetime.now()
        obj.file_attach=request.POST.get('file')
        obj.type=request.POST.get('post')
        obj.who=sd
        obj.save()
    return render(request,'notification_manager/manager_post_notification.html')

def view_all_noti(request):
    ob=NotificationAdmin.objects.filter(Q(type='taskmanager') | Q(type='all') | Q(type='all1'))
    context={
        'objval':ob
    }
    return render(request,'notification_admin/admin_view_notification.html',context)


def post_taskmngr_noti(request):
    sd = request.session["u_id"]
    if request.method=='POST':
        obj=NotificationAdmin()
        obj.tile=request.POST.get('title')
        obj.description=request.POST.get('description')
        obj.date=datetime.datetime.now()
        obj.file_attach=request.POST.get('file')
        obj.type='employee'
        obj.who=sd
        obj.save()
    return render(request,'notification_manager/taskmanager_post_notification.html')

def view_emplo_noti(request):
    ob=NotificationAdmin.objects.filter(Q(type='employee') | Q(type='all') | Q(type='all1'))
    context={
        'objval':ob
    }
    return render(request,'notification_admin/admin_view_notification.html',context)





def delete_mngr_noti(request):
    ob=NotificationAdmin.objects.filter(Q(type='taskmanager') | Q(type='all1'))
    context={
        'objval':ob
    }
    return render(request,'notification_manager/delete_mngr_notification.html',context)

def dell(request,idd):
    obj=NotificationAdmin.objects.get(na_id=idd)
    obj.delete()
    return delete_mngr_noti(request)