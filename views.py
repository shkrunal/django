from django.shortcuts import render , redirect
from .models import contect, feedback
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
