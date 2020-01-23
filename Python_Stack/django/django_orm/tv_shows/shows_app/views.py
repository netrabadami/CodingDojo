from django.shortcuts import render,redirect
from .models import *

def new_show(request):
    return render(request,'new_show.html')

def create(request):
    create = Shows.objects.create(title=request.POST['title'],
                                    network=request.POST['network'],
                                    release_date=request.POST['release_date'],
                                    description=request.POST['description'])

    show_id = create.id
    return redirect(f"/show/{show_id}")

def view_show(request,id):
    context = {
        "all_shows": Shows.objects.get(id=id)
    }
    return render(request,'view_show.html',context)