from django.conf.urls import url
from employee import views

urlpatterns = [
    url('slct_emplo/',views.post)
]