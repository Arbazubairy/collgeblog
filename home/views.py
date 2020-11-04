from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'home.html')

def contact(request):
    return HttpResponse('indeddx of contact')

def about(request):
    return HttpResponse('indeddx of about')

def handleSignup(request):
    if request.method=="POST":
        fname=request.POST["fname"]
        
        username=request.POST["username"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        print(username,email,pass1)
        if (len(username)>10):
            messages.error(request,"Username Inavlid")
            return redirect("/")
        if not username.isalnum():
            messages.error(request,"UserName should contain only letters or numbers")
            return redirect("/")
        if (pass1 != pass2):
            messages.error(request,"password dont match")
            return redirect("/")
        if (len(pass1)<7):
            messages.error(request,"password too short must be atleastb 7 characters")
            return redirect("/")

        creatUser = User.objects.create_user(username,email,pass1)
        creatUser.first_name=fname
        creatUser.save()
        messages.success(request,"SignUp Successful")
        return redirect('/')
    else:
        return HttpResponse("404 - Not Found")

def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user=authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request,"Successful login")
            return redirect('/')
        else:
            messages.error(request,"Login Error!! Please Try Again With Proper Credentials")
            return redirect('/')
    return HttpResponse("404 - Not Found")

def handleLogout(request):
    logout(request)
    return redirect('/')