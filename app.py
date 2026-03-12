from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

FEATURES = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
]

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    probability = None
    values = {f: "" for f in FEATURES}

    if request.method == "POST":
        for f in FEATURES:
            values[f] = request.form.get(f, "0")

        x = np.array([[float(values[f]) for f in FEATURES]], dtype=float)

        pred = int(model.predict(x)[0])
        prediction = pred

        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(x)[0][1])

    return render_template(
        "index.html",
        features=FEATURES,
        values=values,
        prediction=prediction,
        probability=probability
    )

if __name__ == "__main__":
    app.run(debug=True)