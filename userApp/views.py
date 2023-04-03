
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def Index(request):
    return render(request,'index.html')


def Register(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        
        return redirect('login')
        
    return render(request,'register.html')
    # return redirect('login')


def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        
        user=authenticate(username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            
        return redirect('home')    
            
            
    return render(request,'login.html')       