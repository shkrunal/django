from django.shortcuts import render , redirect
from .models import contect, feedback,cal
# Create your views here.
def contact(request):
    if request.POST:
        model=contect()
        model.name=request.POST['firstname']
        model.lname=request.POST['lastname']
        model.email=request.POST['email']
        model.phone=request.POST['number']
        model.coments=request.POST['text']
        model.save()
        return redirect('home')
    return render(request,'contact.html')

def fedback(request):
    if request.POST:
        model=feedback()
        model.fname=request.POST['firstname']
        model.lname=request.POST['lastname']
        model.email=request.POST['mailid']
        model.message=request.POST['text']
        model.save()
        return redirect('home')
    return render(request,'feedback.html')


# def calculator(request):
#     if request.POST:
#         val1=int(request.POST['val1'])
#         val2=int(request.POST['val2'])
#         opt=request.POST['opt']
        
#         if opt =='add':
#             ans=val1+val2
#             return render(request,'calculator.html',{'ans':ans,'val1':val1,'val2':val2,'o':opt})
#         elif opt =='sub':
#             ans=val1-val2
#             return render(request,'calculator.html',{'ans':ans,'val1':val1,'val2':val2,'o':opt})
#         elif opt =='mul':
#             ans=val1*val2
#             return render(request,'calculator.html',{'ans':ans,'val1':val1,'val2':val2})
#         elif opt =='div':
#             ans=val1/val2
#             return render(request,'calculator.html',{'ans':ans,'val1':val1,'val2':val2})

#     return render(request,'calculator.html')


def calculator(request):
    if request.POST:
        model=cal()
        model.val1=request.POST['val1']
        model.val2=request.POST['val2']
        opt=request.POST['opt']
        
        a=int(model.val1)
        b=int(model.val2)

        if opt =='add':
            total=a+b
            model.save()
            return render(request,'calculator.html',{'ans':total,'val1':model.val1,'val2':model.val2,'o':opt})
        elif opt =='sub':
            total=a-b
            total=(model.answer)
            model.save()
            return render(request,'calculator.html',{'ans':total,'val1':model.val1,'val2':model.val2,'o':opt})
        elif opt =='mul':
            total=a*b
            total=(model.answer)
            model.save()
            return render(request,'calculator.html',{'ans':total,'val1':model.val1,'val2':model.val2})
        elif opt =='div':
            total=a/b
            total=(model.answer)
            model.save()
            return render(request,'calculator.html',{'ans':total,'val1':model.val1,'val2':model.val2})

        
    return render(request,'calculator.html')


def cal_oper(request):
    pass

def add(request):
    pass
