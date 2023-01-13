from django.shortcuts import render
from job.models import Job
# Create your views here.

def post(request):
    if request.method=='POST':
        obj=Job()
        obj.dep_id=1
        obj.desi_id=1
        obj.job_name=request.POST.get('jname')
        obj.noof_post=3
        obj.save()
    return render(request,'job/add_job.html')
