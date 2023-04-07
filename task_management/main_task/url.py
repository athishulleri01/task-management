from  django.conf.urls import url
from main_task import views

urlpatterns=[
    url('pst/',views.post),
    url('vw/',views.view),
    url('vwdt/(?P<idd>\w+)',views.viewd,name="vdts"),
    url('pfeed/(?P<idd>\w+)', views.post_feedback, name="pfeed"),
    url('vwadm/', views.vwad),
    url('vw_fee_mngr/', views.view_feed_mngr),
    url('vw_m_status/', views.view_m_status),
    url('delete/(?P<idd>\w+)',views.delete,name='del'),
    url('vw_tasks_to_mngr/', views.view_task_to_mngr),
    url('submit/(?P<idd>\w+)',views.submit,name='sub1'),
    url('vw_tasks_admin/', views.view_task_admin),
    url('drop/',views.selectemployee),
    url('vw_tsk_status_mngr/', views.view_task_status_mngr),
    # url('post_summary/(?P<idd>\w+)',views.post_summary,name='vs'),
    url('tskmng_submit/', views.tsmnr_submit),
    url('vw_sumbit_task_mngrr/', views.view_submi_task_mngr),
    url('vw_sumbit_task_admin/(?P<idd>\w+)', views.view_compltd_work_admin)

]