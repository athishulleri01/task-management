from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
# Create your views here.
def log(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        ps=request.POST.get('pass')
        if Login.objects.filter(username=un,password=ps):
            obj=Login.objects.filter(username=un,password=ps)
            for l in obj:
                tp=l.type
                uid=l.u_id
                if tp=="admin":
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/admin/')
                elif tp=="Manager":
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/manager/')
                elif tp=="employee":
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/employee/')
                elif tp=="taskmanager":
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/taskm/')
        else:
            obje="incorrect username or password"
            context={
                'msg':obje
            }
            return render(request,'login/login_screen.html',context)
    return render(request,'login/login_screen.html')
