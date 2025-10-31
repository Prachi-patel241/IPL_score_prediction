import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

with open("ipl_score_model.pkl", "rb") as f:
    model = pickle.load(f)

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

if __name__ == "__main__":
    app.run(debug=True)