from django.shortcuts import render,redirect
from django.http import HttpRequest , HttpResponse
from .models import Employee

# Create your views here.





def hello(request):
    return render(request,'index.html')

def create(request):
    print("request = ", request.method)
    if(request.method=="GET"):
        print("We are inside get method")
        return render(request, "create.html")
    else : 
        print("we are inside post method")
        name = request.POST['ename']
        address = request.POST['eaddress']
        contact = request.POST['econtact']
        email = request.POST['email']
        msg = request.POST['emsg']
        m = Employee.objects.create(name=name,address=address,contact=contact,email=email,msg=msg)
        return redirect('/show')
    
def show(request):
    mm = Employee.objects.all()
    return render(request, "show.html", {"all":mm})


def delete(request):
    mm = Employee.objects.all()
    return render(request, "delete.html", {"all": mm})

def delete1(request,rid):
    print("delete id", rid)
    
    n=Employee.objects.filter(id=rid)
    n.delete()
    # return redirect("/show")
    return redirect('/delete')

def update(request):
    mm = Employee.objects.all()
    return render(request, "update.html", {"all": mm})


    

def edit(request,rid):
    if request.method=='GET':
        
        m=Employee.objects.filter(id=rid)
        context={}
        context["all"]=m
        return render(request,"edit.html",context)   
    
    else:
        print("we are inside post method")
        name = request.POST['ename']
        address = request.POST['eaddress']
        contact = request.POST['econtact']
        email = request.POST['email']
        msg = request.POST['emsg']
        m = Employee.objects.update(id=rid,name=name,address=address,contact=contact,email=email,msg=msg)
        return redirect('/show')


        
