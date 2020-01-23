from flask import Flask,render_template
app = Flask(__name__,template_folder='template')

@app.route('/')
def checker():
	return render_template("checker.html",input1=8, input2=8)

@app.route("/<x>/<y>")
def checker_board(x,y):
    return render_template("checker.html", input1=int(x), input2=int(y))

if __name__ == "__main__":
	app.run(debug=True)
