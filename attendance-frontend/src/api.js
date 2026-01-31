import axios from "axios";

const API = axios.create({
  baseURL: "https://ai-attendance-prediction.onrender.com",
  timeout: 30000
});

export const predictAttendance = (data) =>
  API.post("/predict", data);
