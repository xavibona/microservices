from flask import Flask

app = Flask(__name__)

@app.route
def funcion():
    pass

app.run(debug=True, port:5000)