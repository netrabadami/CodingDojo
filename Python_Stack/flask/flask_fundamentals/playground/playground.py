from flask import Flask, render_template
app = Flask(__name__,template_folder='template')

@app.route('/play')
def box():
    return render_template("box.html",times=3)

# 7 BOXES
@app.route('/play/<times>')
def box_play_x(times):
    return render_template('box.html', times=int(times),color="none")

# CHANGE BOX COLOR
@app.route('/play/<times>/<color>') 
def box_play_color(times, color):
    return render_template('box.html', times=int(times), color=color)

if __name__=="__main__":
	app.run(debug=True)

