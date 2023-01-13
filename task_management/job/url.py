from django.conf.urls import url
from job import views

urlpatterns = [
    url('add_job/',views.post)
]