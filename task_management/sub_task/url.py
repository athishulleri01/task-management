from django.conf.urls import url
from sub_task import views

urlpatterns=[
    url('post/',views.post),
    url('view_s_feed/',views.view_s_feed),
    url('view_s_status/',views.vw_sub_status),
]