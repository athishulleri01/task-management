from django.conf.urls import url
from designation import views

urlpatterns = [
    url('add_desi/',views.post)
]