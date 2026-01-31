import axios from "axios";


export const predictAttendance = (data) =>
  API.post("/predict", data);
