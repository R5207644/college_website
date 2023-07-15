from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def contact(request):
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