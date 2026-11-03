from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.htm')

def login(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

def profile(request):
    return render(request,'profile.html')

def bookappointment(request):
    return render(request,'bookappointment.html')

