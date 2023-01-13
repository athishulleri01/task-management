from django.shortcuts import render
from designation.models import Designation
# Create your views here.
def post(request):
    if request.method=='POST':
        obj=Designation()
        obj.id=1
        obj.name=request.POST.get('dname')
        obj.rank=request.POST.get('rank')
        obj.save()
    return render(request,'designation/add.html')