import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

MODEL_PATH = '/home/prachipatel19/IPL_score_prediction/IPL_score_prediction/ipl_score_model.pkl'
import os

ipl_score_model = pickle.load(open(MODEL_PATH, 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        runs = float(request.form["runs"])
        wickets = float(request.form["wickets"])
        overs = float(request.form["overs"])
        runs_last_5 = float(request.form["runs_last_5"])
        wickets_last_5 = float(request.form["wickets_last_5"])
        features = [[runs, wickets, overs, runs_last_5, wickets_last_5]]
        prediction = model.predict(features)[0]
        return render_template("index.html", prediction_text=f"Predicted Final Score: {int(prediction)}")
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

