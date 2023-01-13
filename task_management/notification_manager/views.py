from django.shortcuts import render
from notification_manager.models import NotificationManager
import datetime
# Create your views here.

def post_notification(request):
    if request.method=='POST':
        obj=NotificationManager()
        obj.emp_id=1
        obj.title=request.POST.get('title')
        obj.description=request.POST.get('description')
        obj.date=datetime.datetime.now()
        obj.fille_attach=request.POST.get('file')
        obj.save()
    return render(request,'notification_manager/manager_post_notification.html')

def view_comp(request):
    ob=NotificationManager.objects.all()
    context={
        'objval':ob
    }
    return render(request,'notification_manager/view_manager_notification.html',context)