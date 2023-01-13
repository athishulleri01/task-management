from  django.conf.urls import url
from main_task import views

urlpatterns=[
    url('pst/',views.post),
    url('vw/',views.view),
    url('vwdt/(?P<idd>\w+)',views.viewd,name="vdts"),
    url('pfeed/(?P<idd>\w+)', views.post_feedback, name="pfeed"),
    url('vwadm/', views.vwad),
    url('vw_m_status/', views.view_m_status),
    url('vw_tasks_to_mngr/', views.view_task_to_mngr),
]