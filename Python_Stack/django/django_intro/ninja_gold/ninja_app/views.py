from django.shortcuts import render,redirect
import random
import datetime

# Create your views here.
def index(request):
    if "gold_count" not in request.session:
        request.session["gold_count"] = 0
    if "actLog" not in request.session:
        request.session["actLog"] = []
    
    goldCount = request.session["gold_count"]
    actLog = request.session["actLog"]
    return render(request,'index.html')

def process_money(request):	
    if request.POST['whichForm'] == 'farm':
        randomFarmGold = random.randint(10,20)
        now=datetime.datetime.now()
        timestamp=now.strftime("%Y/%m/%d  %I:%M %p")
        eventLog= "<p class='green'>Earned %s gold from Farm! (%s)</p>" %(str(randomFarmGold),timestamp)
        request.session["actLog"].append(eventLog)
        request.session["gold_count"] += randomFarmGold

    if request.POST['whichForm'] == 'cave':
        randomCaveGold = random.randint(5,10)
        now=datetime.datetime.now()
        timestamp=now.strftime("%Y/%m/%d  %I:%M %p")
        eventLog= "<p class='green'>Earned %s gold from cave! (%s)</p> " %(str(randomCaveGold),timestamp)
        request.session["actLog"].append(eventLog)
        request.session["gold_count"] += randomCaveGold

    if request.POST['whichForm'] == 'house':
        randomHouseGold = random.randint(2,5)
        now=datetime.datetime.now()
        timestamp=now.strftime("%Y/%m/%d  %I:%M %p")
        eventLog= "<p class='green'>Earned %s gold from House! (%s)</p>" %(str(randomHouseGold),timestamp)
        request.session["actLog"].append(eventLog)
        request.session["gold_count"] += randomHouseGold

    if request.POST['whichForm'] == 'casino':
        earnorLoose = random.randint(1,2)
        now=datetime.datetime.now()
        timestamp=now.strftime("%Y/%m/%d  %I:%M %p")
        randomCasinoGold = random.randint(0,50)
        request.session.modified = True
        if earnorLoose == 1:
            eventLog= "<p class='green'>Entered a casino and earned %s golds... ohooo.. (%s)</p>" %(str(randomCasinoGold),timestamp)
            request.session["actLog"].append(eventLog)
            request.session["gold_count"] += randomCasinoGold
        elif earnorLoose == 2:
            eventLog= "<p class='red'>Entered a casino and lost %s golds... Ouch..(%s)</p> " %(str(randomCasinoGold),timestamp)
            request.session["actLog"].append(eventLog)
            request.session["gold_count"] -= randomCasinoGold
    return redirect('/')

def clear(request):
    request.session['gold_count'] = 0
    request.session['actLog'] = []
    return redirect('/')

    


    
    
    