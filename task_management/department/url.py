from django.conf.urls import url
from department import views

urlpatterns = [
    url('post_department/',views.post),
    url('view_department/', views.view_dept)

]