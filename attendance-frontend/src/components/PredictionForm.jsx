import React, { useState } from "react";
import { predictAttendance } from "../api";

function PredictionForm() {
  const [form, setForm] = useState({
    attendance: "",
    late_days: "",
    leaves: "",
    discipline_score: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handlePredict = async () => {
    const res = await predictAttendance(form);
    setResult(res.data);
  };

  return (
    <div>
      <h2>Attendance Risk Prediction</h2>

      <input name="attendance" placeholder="Attendance %" onChange={handleChange} />
      <input name="late_days" placeholder="Late Days" onChange={handleChange} />
      <input name="leaves" placeholder="Leaves" onChange={handleChange} />
      <input name="discipline_score" placeholder="Discipline Score" onChange={handleChange} />

      <button onClick={handlePredict}>Predict</button>

      {result && (
        <div>
          <h3>Risk Level: {result.risk_level}</h3>
          <p>Reason: {result.risk_reason}</p>
        </div>
      )}
    </div>
  );
}

export default PredictionForm;
    