from django.shortcuts import render,redirect
from login_app.models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def login(request):
    return render(request,"login.html")

def reg_process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    elif len(User.objects.filter(email=request.POST["email"])) > 0:
        errors["duplicated_email_error"] = "Email is already existed"
        messages.error(request, errors["duplicated_email_error"], extra_tags = "duplicated_email_error")
        return redirect("/")
    else:
        hash1 = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name=request.POST["fname"], last_name=request.POST["lname"],email=request.POST["email"],pw_hash=hash1.decode('utf-8'))
        request.session["userid"] = new_user.id
        messages.success(request, "Successfully registered!")
        return redirect("/success")

def login_process(request):
    msgs = User.objects.loginValidator(request.POST)
    if len(msgs):
        print(msgs)
    else:
        user = User.objects.get(email=request.POST["login_email"])
        request.session['logged_in'] = user.id
        return redirect('/success')
    return redirect('/')

def success(request):
	if User.objects.get(id=request.session['userid']) == User.objects.last():
		status = "registered"
	else:
		status = "logged in"

	context = {
        'user': User.objects.get(id=request.session['userid']),
        'status': status
        }
	return render(request, 'success.html', context)

def logoutprocess(request):
    del request.session["userid"]
    return redirect("/")