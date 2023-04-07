from django.conf.urls import url
from sub_task import views

urlpatterns=[
    # url('post/',views.post),
    url('post/(?P<idd>\w+)',views.post),
    url('view_s_feed/',views.view_s_feed),
    url('view_s_status/',views.vw_sub_status),
    url('view_task_to_tskmngr/', views.vw_subtask_tsmngr),
    url('assign_emp/(?P<idd>\w+)',views.assignemp),
    url('view_task_emplo/', views.view_task_to_employee),
    url('submit_task_emp/(?P<idd>\w+)', views.post_emp_work),
    url('view_taskstatus_tskmngr/', views.view_taskstatus_taskmanager),
    url('work_submit/(?P<idd>\w+)',views.submit_work,name='cmp'),
    url('emp_submit_worrk',views.view_emp_submit_workss),
    url('rettu/(?P<idd>\w+)',views.rjct, name='rt'),
]