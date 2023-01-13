from django.conf.urls import url
from video_conference import views

urlpatterns=[
    url('video/',views.video)
]
