from django.conf.urls import url
from employee_reg import views

urlpatterns = [
    url('pst/',views.post),
    url('view_emp_details/',views.view),
    url('profile/',views.view_prof),
    url('update_status/',views.update_status),
]