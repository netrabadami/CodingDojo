from flask import Flask,render_template,request,redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__,template_folder='template')

@app.route('/')
def fetch_pets():
	mysql = connectToMySQL('first_flask')
	fetchPets = mysql.query_db('SELECT * FROM pets')
	print("fetch All Pets: ",fetchPets)
	return render_template("pets.html",fetchPets=fetchPets)

@app.route('/createpets',methods=['POST'])
def create_pets():
	myDb = connectToMySQL('first_flask')
	createPets = "INSERT INTO pets(name,type,created_at,updated_at) VALUES(%(petName)s,%(petType)s,NOW(),NOW())"
	data = {
	'petName': request.form['petName'],
	'petType': request.form['petType']
	}
	query = myDb.query_db(createPets,data)
	return redirect('/')



if __name__ == "__main__":
	app.run(debug=True)