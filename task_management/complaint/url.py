from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('comp_manager/',views.cmp_mgr),
    url('view_complaint/',views.view_comp_admin),
    url('view_admin_replay_mang/',views.view_admin_replay),
    url('view_tskmng_replay_emp/',views.view_taskmanager_replay),
    url('view_manager_replay_tskmangr/',views.view_manager_replay),
    url('view_complaint_taskman/', views.view_comp_taskman),
    url('replay/(?P<idd>\w+)',views.replay,name="rp1"),
    url('replay_admin/(?P<idd>\w+)',views.admin_replay,name="rp"),
    url('replay_taskmanager/(?P<idd>\w+)',views.taskmanager_replay,name="rp2"),
    url('cp/', views.cmp_taskmng),
    url('cp_emp/', views.cmp_emp),
    url('vw_emp_comp/', views.view_comp_employee),
    # url('ompflut/',views.complaint_view.as_view)
]