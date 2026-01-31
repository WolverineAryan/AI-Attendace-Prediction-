import React, { useState } from "react";
import { predictAttendance } from "../api";

const PredictionCard = () => {
  const [form, setForm] = useState({
    attendance: "",
    late_days: "",
    leaves: "",
    discipline_score: ""
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handlePredict = async () => {
    setLoading(true);
    try {
      const res = await predictAttendance(form);
      setResult(res.data);
    } catch (err) {
      alert("Backend not reachable");
    }
    setLoading(false);
  };

  return (
    <div className="card">
      <h2>🎓 Attendance Risk Predictor</h2>

      <input
        type="number"
        name="attendance"
        placeholder="Attendance %"
        onChange={handleChange}
      />

      <input
        type="number"
        name="late_days"
        placeholder="Late Days"
        onChange={handleChange}
      />

      <input
        type="number"
        name="leaves"
        placeholder="Leaves"
        onChange={handleChange}
      />

      <input
        type="number"
        name="discipline_score"
        placeholder="Discipline Score"
        onChange={handleChange}
      />

      <button onClick={handlePredict}>
        {loading ? "Predicting..." : "Predict Risk"}
      </button>

      {result && (
        <div className={`result ${result.risk_level.toLowerCase()}`}>
          <h3>Risk Level: {result.risk_level}</h3>
          <p>Reason: {result.risk_reason}</p>
        </div>
      )}
    </div>
  );
};

export default PredictionCard;
