from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages


def home(request):
	return render(request, 'general\home.html')

def user_signup(request):
    return render(request, 'general\signup.html')
    
def user_signupUser(request):
        return render(request, 'general\signupUser.html')

def user_signupClient(request):
	if request.method == 'POST':
		user_email = request.POST.get('user_email')
		username = request.POST.get('username')
		user_pswd = request.POST.get('user_pass')
		user_model = get_user_model()
		##
		print(username,user_email,user_pswd)
		if not username.strip():
			messages.error(request, 'Something is wrong.')
			return render(request, 'general\signupClient.html')
		##
		if user_model.objects.filter(email=user_email).exists():
			messages.error(request, 'Something is wrong.')
			return render(request, 'general\signupClient.html')
		##
		user_obj = user_model.objects.create_user(email=user_email,username=username, password=user_pswd)
		user_obj.set_password(user_pswd)
		user_obj.username = username
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
