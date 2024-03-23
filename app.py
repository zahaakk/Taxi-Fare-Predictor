   
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template("index.html")
 
@app.route("/predict", methods = ["POST"])
def predict():
    passenger_count = float(request.form['passenger_count'])
    Month = float (request.form['Month'])
    Date = float (request.form['Date'])
    Day = float (request.form['Day'])
    Hour  = float (request.form['Hour'])
    distance = float (request.form['distance'])
    result = model.predict([[passenger_count,Month,Date,Day,Hour,distance]])[0]
    result = np.exp(result)
    result = round(result,2)
    print(result)
    return render_template("index.html", **locals())

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)