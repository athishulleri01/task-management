from django.conf.urls import url
from temp import views

urlpatterns = [
    url('admin/',views.admin),
    url('employee/',views.employee),
    url('manager/',views.manager),
    url('index/',views.index),
    url('taskm/',views.task)
]
