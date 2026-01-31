import axios from "axios";

export const predictAttendance = (data) => {
  return axios.post("/predict", data);
};
