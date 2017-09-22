from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<center><font size="40sp" color="Red">Hello World!</font></center>'

@app.route("/french")
def bonjour_le_monde():
    return '<center><font size="40sp" color="Blue">Bonjour Le Monde!</font></center>'

@app.route("/spanish")
def hola_mundo():
    return '<center><font size="40sp" color="Green">Hola Mundo!</font></center>'

if(__name__ == "__main__"):
    app.debug = True
    app.run()
