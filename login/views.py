from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
# Create your views here.
def dohome(request):
    c = {}
    c.update(csrf(request))
    return render(request,'home.html')

def dologin(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html')

def doauth(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)
    print(user)
    print("hi")
    if user is not None:
        auth.login(request, user)
        print("valid")
        return render(request,'dashboard.html')
    else:
        print("invalid")
        return  render(request,'login.html',{'message':'Invalid Credential'})
    

def dologout(request):
    auth.logout(request)
    return render(request,'home.html')
from login.models import Register
from login.forms import Registerform
from django.contrib.auth.models import User
def register(request):  
    if request.method == "POST":  
        form = Registerform(request.POST)  
        if form.is_valid():  
            try:  
                username=request.POST.get('username')
                password=request.POST.get('password')
                email=request.POST.get('email')
                my_user=User.objects.create_user(username=username,password=password,email=email)
                my_user.save()
                form.save()  
                return redirect('dohome')  
            except:
                pass
    else:  
        form = Registerform()  
    return render(request,'register.html',{'form':form})