from django.conf.urls import url
from add_employee import views

urlpatterns = [
    url('pst/',views.post),
    url('view_emp_details/',views.view),
    url('profile/',views.view_prof),
    url('update_status/',views.update_status),
    url('prooooooooo/(?P<idd>\w+)', views.edu, name='po'),
    url('profile_t/',views.view_prof_t),
    url('edit_pro_t/(?P<idd>\w+)', views.edu_t, name='poo'),
    url('profile_m/',views.view_prof_m),
    url('edit_pro_m/(?P<idd>\w+)', views.edu_m, name='poo'),
]