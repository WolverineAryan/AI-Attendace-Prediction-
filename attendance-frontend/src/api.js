import axios from "axios";

const API = axios.create({
  baseURL: "https://ai-attendance-prediction.onrender.com",
});

export const predictAttendance = (data) =>
  API.post("/predict", data);
