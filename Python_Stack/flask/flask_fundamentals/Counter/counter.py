from flask import Flask,render_template,request,redirect,session
app = Flask(__name__,template_folder='template')
app.secret_key = 'counter session'

@app.route('/')
def visit():
	if "counter" in session:
		print('key exists!')
		session["counter"] += 1
		print("counter ",session["counter"])

	else:
		session["counter"] = 1
		print("counter ",session["counter"])
		print("key 'key_name' does NOT exist")
	return render_template("counter.html")

@app.route('/add', methods=['POST'])
def alter():
	if request.form['add'] == "add":
		session["counter"] += 1
	elif request.form['add'] == "reset":
		session["counter"] = 0

	return redirect('/')

@app.route('/increment',methods=['POST'])
def increment():
	incrTimes = request.form['incmt']
	session["counter"] = session["counter"] + int(incrTimes) -1
	return redirect('/')




	
	

@app.route('/destroy_session')
def destroy():
	session.clear()
	return redirect('/')
	
	


if __name__ == "__main__":
	app.run(debug=True)