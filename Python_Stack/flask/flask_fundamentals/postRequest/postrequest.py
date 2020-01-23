from flask import Flask,render_template,request,redirect
app = Flask(__name__,template_folder='template')

@app.route('/')
def user():
	return render_template("postrequest.html")

@app.route('/user', methods=['POST'])
def create_user():
	name = request.form['name']
	email = request.form['email']
	return render_template("display.html", name=name, email=email)


if __name__ == "__main__":
	app.run(debug=True)
