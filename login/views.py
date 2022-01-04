from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Member
from .forms import memberform

# Create your views here.

def singin(request):
    if request.method=="POST":
        try:
            m = Member.objects.get(username=request.POST['username'])
            print(m)
            
            if m.password == request.POST['password']:
                print(m.password)
                return HttpResponseRedirect('/app2/home')

            else:
                return HttpResponse("<h2><a href=''>You have entered wrong password </a></h2>")
        except:
            return HttpResponse("<h2><a href=''>no username found.</a></h2>")
    return render(request,'login.html')


def registernew(request):
    a=memberform(request.POST)
    if a.is_valid():
        a.save()
    return render(request, 'registernew.html',{'form':a})


def register(request):
    if request.method=="POST":
        obj=Member()
        obj.username=request.POST['name']
        print(obj.username)
        obj.email=request.POST['email']
        print(obj.email)

        obj.phone=request.POST['phone']
        print(obj.phone)
        obj.password=request.POST['password']
        print(obj.password)
        obj.cpassword=request.POST['cpassword']
        print(obj.cpassword)
        obj.save()
        return redirect('singin')
    return render(request,'register.html')