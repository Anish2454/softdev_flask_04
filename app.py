'''
Anish Shenoy
SoftDev Period 7
HW #4 -- Fill Up Yer Flask
2017-09-22
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('temp.html', title = "Anish's Page", Message = "Hello World!")
@app.route("/french")
def bonjour_le_monde():
    return render_template('temp.html', title = "Anish's Page", Message = "Bonjour Le Monde!")

@app.route("/spanish")
def hola_mundo():
    return render_template('temp.html', title = "Anish's Page", Message = "Hola Mundo!")

if(__name__ == "__main__"):
    app.debug = True
    app.run()
