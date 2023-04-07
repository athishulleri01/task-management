from django.shortcuts import render
from complaint.models import Complaint
import datetime
from django.http import HttpResponse
#import datetime.datetime
# Create your views here.

#manager post complait to admin
def cmp_mgr(request):
    ss = request.session["u_id"]
    ob=Complaint.objects.filter(emp_id=ss)
    if request.method=='POST':
        obj=Complaint()
        obj.emp_id=ss
        obj.complaint=request.POST.get('cmpm')
        obj.reply='NULL'
        obj.date=datetime.datetime.today()
        obj.status='pending'
        obj.title=request.POST.get('nm')
        obj.type='manager'
        obj.save()
    return render(request, 'complaint/post_complaint_manager_to_admin.html')

def cmp_taskmng(request):
    if request.method=='POST':
        obj=Complaint()
        # obj.emp_id=1
        obj.complaint=request.POST.get('post')
        obj.reply='NULL'
        obj.date=datetime.datetime.today()
        obj.status='pending'
        obj.title = request.POST.get('nm')
        obj.type='taskmanager'
        obj.save()
    return render(request,'complaint/cmp_taskmanager.html')

def cmp_emp(request):
    if request.method=='POST':
        obj=Complaint()
        obj.emp_id=1
        obj.complaint=request.POST.get('cmpm')
        obj.reply='NULL'
        obj.date=datetime.datetime.today()
        obj.status='pending'
        obj.title=request.POST.get('nm')
        obj.type='employee'
        obj.save()
    return render(request, 'complaint/cmp_empoyee.html')


def replay(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('rplay')
        obj.status="viwed"
        obj.save()
    return render(request, 'complaint/replay_complaint_manager.html')

def taskmanager_replay(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('rplay')
        obj.status="viwed"
        obj.save()
    return render(request, 'complaint/replay_complaint_taskmanager.html')


def admin_replay(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('rplay')
        obj.status="viwed"
        obj.replay_date=datetime.datetime.today()
        obj.save()
    return render(request, 'complaint/replay_complaint_admin.html')


def view_comp_admin(request):
    ob=Complaint.objects.filter(type='manager')
    context={
        'objval':ob
    }
    return render(request,'complaint/view_complaint.html',context)

def view_comp_taskman(request):
    ob=Complaint.objects.filter(type='taskmanager')
    context={
        'objval':ob
    }
    return render(request,'complaint/view_complaint.html',context)




# from rest_framework.views import APIView,Response
# from complaint.serializers import android_serializers
#
# class complaint_view(APIView):
#     def get(self, request):
#         ob = Complaint.objects.all()
#         ser= android_serializers(ob,many=True)
#         return Response(ser.data)
#
#
#     def post(self,request):
#         ob = Complaint()
#         ob.emp_id='1'
#         ob.complaint=request.data['complaint']
#         ob.date=datetime.datetime.now()
#         ob.status='pending'
#         ob.save()
#         return HttpResponse("yess")





def view_admin_replay(request):
    ss = request.session["u_id"]
    ob=Complaint.objects.filter(emp_id=ss)
    context={
        'objval':ob
    }
    return render(request,'complaint/view_admin_replay_managert.html',context)

def view_taskmanager_replay(request):
    ss = request.session["u_id"]
    ob=Complaint.objects.filter(emp_id=ss)
    context={
        'objval':ob
    }
    return render(request,'complaint/view_taskmng_replay_employe.html',context)


def view_manager_replay(request):
    ss = request.session["u_id"]
    ob=Complaint.objects.filter(emp_id=ss)
    context={
        'objval':ob
    }
    return render(request,'complaint/view_manager_replay_tskmanager.html',context)


def view_comp_employee(request):
    ob=Complaint.objects.filter(type='employee')
    context={
        'objval':ob
    }
    return render(request,'complaint/view_complaint_employee.html',context)