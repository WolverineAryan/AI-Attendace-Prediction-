from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load("model/attendance_risk_model.pkl")

@app.route("/")
def home():
    return "AI Attendance Prediction Backend Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    attendance = float(data["attendance"])
    late_days = int(data["late_days"])
    leaves = int(data["leaves"])
    discipline = int(data["discipline_score"])

    features = np.array([[attendance, late_days, leaves, discipline]])
    prediction = model.predict(features)[0]

    # ---------- RISK LEVEL ----------
    if attendance >= 85:
        risk_level = "Safe"
    elif attendance >= 70:
        risk_level = "Medium"
    else:
        risk_level = "High"

    # ---------- RISK REASON ----------
    if attendance < 60:
        reason = "Very low attendance"
    elif leaves > 10:
        reason = "Too many leaves"
    elif late_days > 10:
        reason = "Frequent late arrivals"
    elif discipline > 20:
        reason = "Poor discipline"
    else:
        reason = "Normal attendance behavior"

    return jsonify({
        "risk_level": risk_level,
        "risk_reason": reason
    })
