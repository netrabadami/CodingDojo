from flask import Flask,render_template,request,redirect,session,Markup
import random
app = Flask(__name__,template_folder='template')
app.secret_key = 'counter session'

@app.route('/')
def game():
	guess_number = random.randint(0,101)

	if "guess" not in session:
		session["guess"] = guess_number
	return render_template("greatnumber.html")	
    
    
        
	

@app.route('/guess',methods=['POST'])
def get_input():
	input_value = int(request.form["input_guess"])
	random_guess = session["guess"]
	print("random",random_guess)
	if input_value == random_guess:
		session["ans"] = "True"
		boxText = "Great!!! that was the number"
		boxColor = "green"
		hideDiv=Markup('<div class="displayBox">')
		closeDiv = Markup('</div>')
		displayProp="block"
		reset= Markup('<a href="/"><button type="submit" value="Submit">Try Again</button><a>')
		session.clear()
		return render_template("greatnumber.html",random_guess=random_guess,boxText=boxText,boxColor=boxColor,reset_button=reset,hideDiv=hideDiv,closeDiv=closeDiv)
	if input_value > random_guess:
		boxText = "Too high!!"
		hideDiv=Markup('<div class="displayBox">')
		closeDiv = Markup('</div>')
		boxColor = "red"
		displayProp="block"
		return render_template("greatnumber.html",random_guess=random_guess,boxText=boxText,boxColor=boxColor,hideDiv=hideDiv,closeDiv=closeDiv)
	if  input_value < random_guess:
		boxText = "Too Low!!"
		hideDiv=Markup('<div class="displayBox">')
		closeDiv = Markup('</div>')
		boxColor = "red"
		displayProp="block"
		return render_template("greatnumber.html",random_guess=random_guess,boxText=boxText,boxColor=boxColor,hideDiv=hideDiv,closeDiv=closeDiv)



if __name__ == "__main__":
	app.run(debug=True)
