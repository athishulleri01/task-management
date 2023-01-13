from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('post_comp/',views.post_complaint),
    url('view_complaint/',views.view_comp),
    url('replay/(?P<idd>\w+)',views.replay,name="rp")
]