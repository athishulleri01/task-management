from django.conf.urls import url
from notification_manager import views

urlpatterns = [
    url('post_notificaton',views.post_notification),
    url('view_tasmng_noti',views.view_all_noti),
    url('post_taskmngr_noti', views.post_taskmngr_noti),
    url('view_empl_notii', views.view_emplo_noti),
    url('delet_mngrr_notification',views.delete_mngr_noti),
    url('dlt(?P<idd>\w+)', views.dell, name='dl')

]