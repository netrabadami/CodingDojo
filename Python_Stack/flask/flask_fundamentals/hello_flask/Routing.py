from flask import Flask, render_template
app = Flask(__name__, template_folder='template')

@app.route('/')
def helloWorld():
	return "Hellow World"

@app.route('/dojo')
def dojo():
	return "Dojo!"

@app.route('/say/<name>')
def say(name):
	return "Hi "+name+"!"

@app.route('/repeat/<int:num>/<msg>')
def repeat(num,msg):
	return msg * num



# app name 
@app.errorhandler(404) 
  
# inbuilt function which takes error as parameter 
def not_found(e):
	return render_template("404.html")
   	

if __name__ == "__main__":
	app.run(debug=True)

