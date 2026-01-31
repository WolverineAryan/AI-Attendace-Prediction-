import axios from "axios";

const API = axios.create({
  baseURL: "https://attendance-backend.onrender.com",
  timeout: 20000
});

export const predictAttendance = async (data) => {
  try {
    const res = await API.post("/predict", data);
    return res;
  } catch (err) {
    console.error("API ERROR:", err);
    throw err;
  }
};
