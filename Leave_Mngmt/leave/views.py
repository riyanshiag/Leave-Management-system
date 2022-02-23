
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login,logout,  authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from . import models
from .models import employee


# Create your views here.
def leave_list(request):

    return render(request, 'C:/Users/rdrl123/Desktop/django/Leave_Mngmt/leave/templates/header.html', {})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("leave_list")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="C:/Users/rdrl123/Desktop/django/Leave_Mngmt/leave/templates/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('/dashboard')

			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="C:/Users/rdrl123/Desktop/django/Leave_Mngmt/leave/templates/login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return render(request=request, template_name="C:/Users/rdrl123/Desktop/django/Leave_Mngmt/leave/templates/header.html")

def dashboard(request):
	user = request.user
	if user.is_authenticated:
		E= employee.objects.filter(user=user)
		print(E)
	return render(request=request, template_name="C:/Users/rdrl123/Desktop/django/Leave_Mngmt/leave/templates/header.html",context={"past_leaves":E})


