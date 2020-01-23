from flask import Flask,render_template,request,redirect,session
import random
import datetime
app = Flask(__name__,template_folder='template')
app.secret_key = 'sessionninjagold'

@app.route('/')
def home():
	if "gold_count" not in session:
		session["gold_count"] = 0

	if "actLog" not in session:
		session["actLog"] = []

	goldCount = session["gold_count"]
	actLog = session["actLog"]

	return render_template("ninjagold.html",goldCount=goldCount,actLog=actLog)

@app.route('/process_money',methods=['POST'])
def processmoney():
	print(request.form)
	if request.form['whichForm'] == 'farm':
		randomFarmGold = random.randint(10,20)
		now=datetime.datetime.now()
		timestamp=now.strftime("%Y/%m/%d  %I:%M %p")
		eventLog= "<p class='green'>Earned %s gold from Farm! (%s)</p>" %(str(randomFarmGold),timestamp)
		session["actLog"].append(eventLog)
		session["gold_count"] += randomFarmGold

	if request.form['whichForm'] == 'cave':
		randomCaveGold = random.randint(5,10)
		now=datetime.datetime.now()
		timestamp=now.strftime("%Y/%m/%d  %I:%M %p")
		eventLog= "<p class='green'>Earned %s gold from cave! (%s)</p> " %(str(randomCaveGold),timestamp)
		session["actLog"].append(eventLog)
		session["gold_count"] += randomCaveGold

	if request.form['whichForm'] == 'house':
		randomHouseGold = random.randint(2,5)
		now=datetime.datetime.now()
		timestamp=now.strftime("%Y/%m/%d  %I:%M %p")
		eventLog= "<p class='green'>Earned %s gold from House! (%s)</p>" %(str(randomHouseGold),timestamp)
		session["actLog"].append(eventLog)
		session["gold_count"] += randomHouseGold

	if request.form['whichForm'] == 'casino':
		earnorLoose = random.randint(1,2)
		now=datetime.datetime.now()
		timestamp=now.strftime("%Y/%m/%d  %I:%M %p")
		randomCasinoGold = random.randint(0,50)
		session.modified = True

		if earnorLoose == 1:
			eventLog= "<p class='green'>Entered a casino and earned %s golds... ohooo.. (%s)</p>" %(str(randomCasinoGold),timestamp)
			session["actLog"].append(eventLog)
			session["gold_count"] += randomCasinoGold
		elif earnorLoose == 2:
			eventLog= "<p class='red'>Entered a casino and lost %s golds... Ouch..(%s)</p> " %(str(randomCasinoGold),timestamp)
			session["actLog"].append(eventLog)
			session["gold_count"] -= randomCasinoGold
			
	return redirect('/')
	
@app.route('/clear',methods=['POST'])
def clear():
    session['gold_count'] = 0
    session['actLog'] = []
    return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)