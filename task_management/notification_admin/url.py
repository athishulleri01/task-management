from django.conf.urls import url
from notification_admin import views

urlpatterns = [
    url('post_notification/',views.post_notification),
    url('view_notification',views.view_noti),
    url('delet_admin_notification',views.delete_admin_noti),
    url('dlt(?P<idd>\w+)', views.dell, name='dl'),
    url('delet_tsk_notification',views.delete_taskm_noti),
    url('dltt(?P<idd>\w+)', views.delll, name='dl')

]