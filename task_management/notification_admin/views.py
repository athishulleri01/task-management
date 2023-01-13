from django.shortcuts import render
from notification_admin.models import NotificationAdmin
import datetime
# Create your views here.

def post_notification(request):
    if request.method=='POST':
        obj=NotificationAdmin()
        obj.emp_id=1
        obj.m_id=1
        obj.date=datetime.datetime.now()
        obj.tile=request.POST.get('n_title')
        obj.description=request.POST.get('description')
        obj.file_attach=request.POST.get('n_file')
        obj.save()
    return render(request,'notification_admin/admin_post_notification.html')

def view_noti(request):
    ob=NotificationAdmin.objects.all()
    context={
        'objval':ob
    }
    return render(request,'notification_admin/admin_view_notification.html',context)



from rest_framework.views import APIView,Response
from complaint.serializers import android_serializers

class admin_notification_view(APIView):
    def get(self, request):
        ob = NotificationAdmin.objects.all()
        ser= android_serializers(ob,many=True)
        return Response(ser.data)








