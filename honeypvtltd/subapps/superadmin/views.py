from django.shortcuts import render,HttpResponse,redirect
from .models import Superadmin_data,Manager_data
from .forms import ManagerForm



def animesh(req):
    if req.method=="POST":
        name=req.POST.get("nm")
        pasword=req.POST.get("pwd")
        data=Superadmin_data.objects.filter(username=name).exists()
        if(data):
            data1=Superadmin_data.objects.filter(password=pasword).exists()
            if(data1):
                req.session["data"]=data
                return redirect("super")
            else:
                return HttpResponse("password wrong")
            
        return HttpResponse("username wrong")
    return render(req,"superadmin.html")



def Super_dashboard(req):
    data=req.session.get("data")
    btn=req.GET.get("btn")
    # print(data)
    # print(btn)
    if data:
        if(btn=="addmanager"):
            if req.method=="POST":
                form=ManagerForm(req.POST)
                if form.is_valid():
                    form.save()
                    return redirect('super')
                else:
                    form=ManagerForm()
                    return render(req,'addmanager.html',{'form':form})
                
            return render(req,"addmanager.html")
        elif(btn=="edit"):
            manager_id=req.GET.get("id")
            print(manager_id)
            manager=Manager_data.objects.get(id=manager_id)
            if req.method=="POST":
                form=ManagerForm(req.POST,instance=manager)
                if form.is_valid():
                    form.save()
                    req.session['success']='manager data update sucsesfully'
                    return redirect('super')
            else:
                form=ManagerForm(instance=manager)
            return render(req,"editmanager.html",{'form':form})
        elif(btn=="delete"):
            manager_id=req.GET.get("id")
            try:
                manager=Manager_data.objects.get(id=manager_id)
                manager.delete()
                req.session['success']='manager data delete sucsesfully'
            except Manager_data.DoesNotExist:
                req.session['error']='manager not found'
                return redirect("super")   
            

            return HttpResponse("delete")
        mdata=Manager_data.objects.all()
        return render(req,'Superdashboard.html',{"data":mdata})
    return HttpResponse("admin panel")



def Manager_login(req):
    return HttpResponse("hii manager")

