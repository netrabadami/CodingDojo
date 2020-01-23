from flask import Flask, render_template,request,redirect,flash,session
from mysqlconnection import connectToMySQL
import re

email_reg=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__,template_folder='template')
app.secret_key = 'formvalidation'
@app.route("/")
def index():
    mysql = connectToMySQL('first_flask')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print("My First Flask SQL: ",friends)
    return render_template("index.html",all_friends=friends)

@app.route('/create',methods=['POST'])
def create():
	if len(request.form['fName']) < 1:
		flash("Please enter first name")
	if len(request.form['lName']) < 1:
		flash("Please enter last name")
	if len(request.form['ocptn']) < 2:
		flash("Please enter occupation")
	if len(request.form['email']) < 10:
		flash("Please enter email")
	print("email",request.form['email'])
	if not email_reg.match(request.form['email']):
		flash("Please enter valid email")

	if not '_flashes' in session.keys():
		dbSql = connectToMySQL('first_flask')
		creatQuery = "INSERT INTO friends(first_name,last_name,occupation,email,created_at,updated_at) VALUES(%(fn)s,%(ln)s,%(occ)s,%(email)s,NOW(),NOW())"
		data = {
			'fn':request.form['fName'],
			'ln':request.form['lName'],
			'occ':request.form['ocptn'],
			'email':request.form['email']
		}
		create=dbSql.query_db(creatQuery,data)

	return redirect('/')

            
if __name__ == "__main__":
    app.run(debug=True)