from django.shortcuts import render
from summary.models import Summary
from  main_task.models import MainTask
import datetime
# Create your views here.
def post_summary(request,idd):
    if request.method=='POST':
        obj=Summary()
        obj.m_id=1
        obj.mt_id=idd
        obj.summary=request.POST.get('summary')
        obj.date=datetime.datetime.now()
        obj.save()
    return render(request,'summary/post_summary.html')

def view_sum(request):
    ob=Summary.objects.all()
    context={
        'objval':ob,

    }
    return render(request,'summary/view_summary.html',context)