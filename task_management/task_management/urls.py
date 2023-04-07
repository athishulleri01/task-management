"""task_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url('call/',include('call.url')),
    url('video_conference/',include('video_conference.url')),
    url('job/',include('job.url')),
    url('chat/',include('chat.url')),
    url('complaint/',include('complaint.url')),
    url('department/',include('department.url')),
    url('designation/',include('designation.url')),
    url('add_employee/', include('add_employee.url')),
    url('login/',include('login.url')),
    url('main_task/',include('main_task.url')),
    url('manager/',include('manager.url')),
    url('notification_admin/',include('notification_admin.url')),
    url('notification_manager/',include('notification_manager.url')),
    url('maintask2/',include('sub_task.url')),
    url('subtask/',include('sub_task.url')),
    url('summary/',include('summary.url')),
    url('employee/',include('employee.url')),
    url('temp/',include('temp.url')),
    url('$',views.log)
    ]