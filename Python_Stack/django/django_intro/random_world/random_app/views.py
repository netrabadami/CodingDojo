from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request,"random.html")

def generate(request):
    print("in generate")
    if request.method == 'POST':
        request.session['word'] = get_random_string(length=13)
        request.session['counter'] += 1
    return redirect('/')

def reset(request):
	request.session['counter'] = 1
	return redirect('/')
