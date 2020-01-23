from flask import Flask,render_template,request,redirect,session
app = Flask(__name__,template_folder='template')
app.secret_key = 'Keep safe session'

@app.route('/')
def user():
	return render_template("dojosurvey.html")

@app.route('/result', methods=['POST'])
def submitSurvey():
	print(request.form)
	session['yourName'] = request.form['yourName']
	session['dojoLocation'] = request.form['dojoLocation']
	session['comments'] =request.form['comment']
	return redirect('/display')

@app.route('/display')
def display():
	print("Showing the User Info From the Form")
	return render_template("displaysurvey.html")
    

if __name__ == "__main__":
	app.run(debug=True)