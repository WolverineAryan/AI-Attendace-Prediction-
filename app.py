from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# ✅ MANUAL CORS FIX (100% WORKING)
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    return response


model = joblib.load("model/attendance_risk_model.pkl")


@app.route("/")
def home():
    return "AI Attendance Prediction Backend Running"


@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():

    # ✅ handle browser preflight
    if request.method == "OPTIONS":
        return "", 200

    data = request.json

    attendance = float(data["attendance"])
    late_days = int(data["late_days"])
    leaves = int(data["leaves"])
    discipline = int(data["discipline_score"])

    if attendance >= 85:
        risk = "Safe"
    elif attendance >= 70:
        risk = "Medium"
    else:
        risk = "High"

    if attendance < 60:
        reason = "Very low attendance"
    elif leaves > 10:
        reason = "Too many leaves"
    elif late_days > 10:
        reason = "Frequent late arrivals"
    elif discipline > 20:
        reason = "Poor discipline"
    else:
        reason = "Normal attendance"

    return jsonify({
        "risk_level": risk,
        "risk_reason": reason
    })


if __name__ == "__main__":
    app.run()
