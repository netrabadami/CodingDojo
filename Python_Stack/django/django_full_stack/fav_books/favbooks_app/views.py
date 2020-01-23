from django.shortcuts import render

# Create your views here.
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
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        createUser = User.objects.create(name=request.POST['name'],
                                    alias=request.POST['alias'],
                                    email=request.POST['email'],
                                    pw_hash=pw_hash)
    request.session['user_id'] = createUser.id
    return redirect('/books')

def login_process(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
            return redirect('/')
    else:
        user = User.objects.get(email=request.POST['login_email'])
        request.session['user_id'] = user.id
        return redirect('/books')