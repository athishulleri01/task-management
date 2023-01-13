from django.conf.urls import url
from call import views

urlpatterns=[
    url('post/',views.post)
]