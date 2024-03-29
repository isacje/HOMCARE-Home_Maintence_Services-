from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from .models import ServiceProvider,Client,NewUser
import uuid


def home(request):
    return render(request, 'general\home.html')

def user_signup(request):
    return render(request, 'general\signup.html')

def client_signUpPage(request):
    return render(request,'general\signupClient.html')

def serviceProvider_signUp(request):
    return render(request,'general\signupUser.html')
    
def user_signupUser(request):
    print("hellooww", request)
    if request.method == 'POST':
        userID=str(uuid.uuid4())
        print(userID)
        user_email = request.POST.get('user_email')
        username = request.POST.get('username')
        user_pswd = request.POST.get('user_pass')
        user_phNo=request.POST.get('user_phNo')
        user_adr=request.POST.get('user_adr')
        print(username,user_email,user_pswd)
        userType="User"
        if not username.strip():
            messages.error(request, 'Something is wrong.')
            return render(request, 'general\signupUser.html')
        user_obj = Client.objects.create(username=username,email=user_email,password=user_pswd,phoneNo=user_phNo,address=user_adr,userType=userType)
        user_obj.set_password(user_pswd)
        # user_obj.username = username
        user_obj.save()
        user_auth = authenticate(username=username, password=user_pswd)
        ##
        if user_auth:
            print("Hi 1")
            login(request, user_auth)
            return redirect('home')
        print("Hi 2")
        return render(request, 'general\signupUser.html')

def user_signupClient(request):
    print("hellooww", request)
    if request.method == 'POST':
        # clientID=str(uuid.uuid4())
        user_email = request.POST.get('user_email')
        username = request.POST.get('username')
        user_pswd = request.POST.get('user_pass')
        user_cmpName=request.POST.get('user_cmpName')
        user_ownName=request.POST.get('user_ownName')
        user_offAdr=request.POST.get('user_offAdr')
        user_phNo=request.POST.get('user_phNo')
        user_gst=request.POST.get('user_gst')
        userType="Service Provider"
        #files
        ##
        print(username,user_email,user_pswd)
        if not username.strip():
            messages.error(request, 'Something is wrong.')
            return render(request, 'general\signupClient.html')
        ##
        ##
        user_obj = ServiceProvider.objects.create(username=username,email=user_email,password=user_pswd,companyName=user_cmpName,officeAddress=user_offAdr,ownerName=user_ownName,gstNo=user_gst,phoneNo=user_phNo,userType=userType)
        user_obj.set_password(user_pswd)
        # user_obj.username = username
        user_obj.save()
        user_auth = authenticate(username=username, password=user_pswd)
        ##
        if user_auth:
            login(request, user_auth)
            return redirect('home')
    return render(request, 'general\signupClient.html')


def user_login(request):
    if request.method == 'POST':
        user_email = request.POST['user_email']
        user_pswd = request.POST['user_pass']
        try:
            user_auth = authenticate(username=user_email, password=user_pswd)
            login(request, user_auth)
            return redirect('home')
        except:
            messages.error(request, 'Something is wrong.')
            return render(request, 'general\login.html')
    else:
        return render(request, 'general\login.html')


def user_logout(request):
    try:
        logout(request)
    except:
        messages.error(request, 'Something is wrong.')
    return redirect('login')


def user_authenticate(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        user_pswd = request.POST.get('user_password')
        print("username :",user_email,"pass:",user_pswd)

        try:
            user_auth = authenticate(username=user_email, password=user_pswd)
            login(request, user_auth)
            return redirect('home')
        except:
            messages.error(request, 'Something is wrong.')
            return render(request, 'general\login.html')
