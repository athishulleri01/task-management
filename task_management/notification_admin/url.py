from django.conf.urls import url
from notification_admin import views

urlpatterns = [
    url('post_notification/',views.post_notification),
    url('view_notification',views.view_noti)

]