from django.shortcuts import render,redirect

data = {
    'count' : 1, 
    'randomWord': get_random_string()
    }
def index(request):
    return render(request,"index.html",data)
        
def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    print(name_from_form)
    print(email_from_form)
    context = {
        "name": name_from_form,
        "email": email_from_form
    }
    return redirect('/success')
    # return render(request,"show.html",context)
def success(request):
    return render(request,"success.html")