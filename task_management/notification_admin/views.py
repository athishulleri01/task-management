from django.shortcuts import render
from notification_admin.models import NotificationAdmin
import datetime
from django.db.models import Q
# Create your views here.

def post_notification(request):
    sd = request.session["u_id"]
    if request.method=='POST':
        obj=NotificationAdmin()
        obj.date=datetime.datetime.now()
        obj.tile=request.POST.get('n_title')
        obj.description=request.POST.get('description')
        obj.file_attach=request.POST.get('n_file')
        obj.type=request.POST.get('post')
        obj.who=sd
        obj.save()
    return render(request,'notification_admin/admin_post_notification.html')

def view_noti(request):
    ob=NotificationAdmin.objects.filter(Q(type='manager') | Q(type='all'))
    context={
        'objval':ob
    }
    return render(request,'notification_admin/admin_view_notification.html',context)



# from rest_framework.views import APIView,Response
# from complaint.serializers import android_serializers
#
# class admin_notification_view(APIView):
#     def get(self, request):
#         ob = NotificationAdmin.objects.all()
#         ser= android_serializers(ob,many=True)
#         return Response(ser.data)




def delete_admin_noti(request):
    ob=NotificationAdmin.objects.filter(Q(type='manager') | Q(type='all'))
    context={
        'objval':ob
    }
    return render(request,'notification_admin/delete_admin_notification.html',context)

def dell(request,idd):
    obj=NotificationAdmin.objects.get(na_id=idd)
    obj.delete()
    return delete_admin_noti(request)



def delete_taskm_noti(request):
    ob=NotificationAdmin.objects.filter(Q(type='employee') | Q(type='all') | Q(type='all1'))
    context={
        'objval':ob
    }
    return render(request,'notification_admin/delete_taskmngr_notification.html',context)

def delll(request,idd):
    obj=NotificationAdmin.objects.get(na_id=idd)
    obj.delete()
    return delete_taskm_noti(request)
