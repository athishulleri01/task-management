from django.shortcuts import render
from sub_task.models import SubTask
from main_task.models import MainTask
from employee.models import Employee
from employee_reg.models import EmpRegister
from django.http import HttpResponse
import datetime
# Create your views here.

def post(request):
    obj = MainTask.objects.all()
    obj1 = Employee.objects.all()
    obj2 = EmpRegister.objects.all()
    context = {
        'objva': obj,
        'objval1': obj1,
        'objval2': obj2
    }

    if request.method=='POST':
        ob=SubTask()
        ob.m_task=request.POST.get('main_task_name')
        ob.subtitle=request.POST.get('subtitle')
        ob.file_attach=request.POST.get('file')
        ob.description=request.POST.get('dec')
        ob.current_date=datetime.datetime.today()
        ob.start_date=request.POST.get('s_date')
        ob.end_date=request.POST.get('e_date')
        ob.due_date=datetime.datetime.now() # formate not currect
        ob.st_status='pending'
        ob.feedback='pending'
        ob.feed_date=datetime.datetime.now()
        ob.save()
    return render(request,'sub_task/sub_asign.html',context)




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



from rest_framework.views import APIView,Response
from sub_task.serializers import android_serializers

class feedback_post_emp(APIView):



    def post_feed(self,request):
        ob = SubTask()
        ob.emp_id='1'
        ob.m_id=request.data['m_id']
        ob.st_id=request.data['st_id']
        ob.m_task = request.data['m_task']
        ob.subtitle = request.data['subtitle']
        ob.feedback=request.data['feedback']
        ob.feed_date = request.data['feed_date']
        ob.save()
        return HttpResponse("yess")

    def get(self, request):
        ob = SubTask.objects.all()
        ser = android_serializers(ob, many=True)
        return Response(ser.data)


    def submit_task(self, request):
        ob = SubTask()
        ob.emp_id = '1'
        ob.m_id = request.data['m_id']
        ob.st_id = request.data['st_id']
        ob.m_task = request.data['m_task']
        ob.subtitle = request.data['subtitle']
        ob.file_attach = request.data['file_attach']
        ob.feed_date = request.data['feed_date']
        ob.save()
        return HttpResponse("yess")




