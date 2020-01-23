from django.shortcuts import render, HttpResponse
import datetime
def timedisplay(request):
    now = datetime.datetime.utcnow()
    currDate = now.strftime("%B %d, %Y")
    currTime = now.strftime("%I:%M %p")
    context = {
        "date": currDate,
        "time": currTime

    }
    return render(request,'time.html',context)