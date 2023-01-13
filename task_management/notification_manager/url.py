from django.conf.urls import url
from notification_manager import views

urlpatterns = [
    url('post_notificaton',views.post_notification)

]