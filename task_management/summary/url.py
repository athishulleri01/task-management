from django.conf.urls import url
from summary import views

urlpatterns = [
    url('post_summary/(?P<idd>\w+)',views.post_summary,name='vs'),
    url('view_summary/',views.view_sum)
]