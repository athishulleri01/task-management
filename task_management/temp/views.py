from django.shortcuts import render


# Create your views here.
def admin(request):
    return  render(request,'temp/admin.html')

def manager(request):
    return  render(request,'temp/manager.html')

def employee(request):
    return  render(request,'temp/employee.html')

def index(request):
    return  render(request,'temp/index.html')