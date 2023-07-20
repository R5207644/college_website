from django.shortcuts import render
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        sem=request.POST.get('sem')
        email=request.POST.get('email')
        review=request.POST.get('review')
        contact=Contact(name=name,date=datetime.today(),sem=sem,email=email,review=review)
        contact.save()

    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def sarvesh(request):
    return render(request,'sarvesh.html')

def front_end(request):
    return render(request,'front_end.html')

def full_stack(request):
    return render(request,'full_stack.html')

def security(request):
    return render(request,'security.html')

def data_scientist(request):
    return render(request,'data_scientist.html')