from django.conf.urls import url
from employee import views

urlpatterns = [
    url('slct_emplo/',views.post),
    url('vw_mid_emp/', views.vw_mid_emp),
    url('vw_emplo_status_manager/', views.vw_emlpo_status_mangr),
    url('vw_emplo_sts_mangr/', views.vw_emp_stus_mnggr),
    url('vw_emplo_sts_tskmangr/', views.vw_emp_stus_tskmngr)
]