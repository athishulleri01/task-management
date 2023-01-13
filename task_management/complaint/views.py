from django.shortcuts import render
from complaint.models import Complaint
import datetime
from django.http import HttpResponse
#import datetime.datetime
# Create your views here.

#manager post complait to admin
def post_complaint(request):
    if request.method=='POST':
        obj=Complaint()
        obj.emp_id=1
        obj.complaint=request.POST.get('post_comp')
        obj.reply='NULL'
        obj.date=datetime.datetime.today()
        obj.status='pending'
        obj.save()
    return render(request,'complaint/post_complaint.html')


def replay(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('rplay')
        obj.status="viwed"
        obj.save()
    return render(request,'complaint/replay_complaint.html')

def view_comp(request):
    ob=Complaint.objects.all()
    context={
        'objval':ob
    }
    return render(request,'complaint/view_complaint.html',context)




from rest_framework.views import APIView,Response
from complaint.serializers import android_serializers

class complaint_view(APIView):
    def get(self, request):
        ob = Complaint.objects.all()
        ser= android_serializers(ob,many=True)
        return Response(ser.data)


    def post(self,request):
        ob = Complaint()
        ob.emp_id='1'
        ob.complaint=request.data['complaint']
        ob.date=request.data['date']
        ob.status=request.data['status']
        ob.save()
        return HttpResponse("yess")





