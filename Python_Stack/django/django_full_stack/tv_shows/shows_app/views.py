from django.shortcuts import render,redirect
from .models import *
from time import strftime, strptime
from django.contrib import messages

def index(request):
    return redirect('/shows')

def new_show(request):
    return render(request,'new_show.html')

def create(request):
    error = Shows.objects.basic_validation(request.POST)
    if len(error) > 0:
        for key,value in error.items():
            messages.error(request,value)
        return redirect('/shows/new')
    else:
        create = Shows.objects.create(title=request.POST['title'],
                                    network=request.POST['network'],
                                    release_date=request.POST['release_date'],
                                    description=request.POST['description'])

    show_id = create.id
    messages.success(request, "Show successfully added.")
    return redirect(f"/show/{show_id}")

def view_show(request,id):
    context = {
        "all_shows": Shows.objects.get(id=id)
    }
    return render(request,'view_show.html',context)

def view_all_shows(request):
    context = {
        "all_shows": Shows.objects.all()

    }
    return render(request,'view_all_shows.html',context)

def edit_show(request,id):
    allShows = Shows.objects.get(id=id)
    date = allShows.release_date
    context = {
        "edit_show": Shows.objects.get(id=id),
    }
    return render(request,'edit_show.html',context)

def edit(request,id):
    error = Shows.objects.basic_validation(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect(f"/show/{id}/edit")
    else:
        edit = Shows.objects.get(id=id)
        edit.title = request.POST['title']
        edit.network = request.POST['network']
        edit.release_date = request.POST['release_date']
        edit.description = request.POST['description']
        edit.save()
        messages.success(request, "Show successfully Updated.")
        return redirect(f"/show/{id}")

def delete(request,id):
    delete = Shows.objects.get(id=id)
    delete.delete()
    return redirect('/shows')