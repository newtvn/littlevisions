import axios from "axios";

function getHeaders() {
  var token = localStorage.getItem("token");
  if (token != null && token != "") {
    return {
      Authorization: token,
    };
  }
  return {};
}
let baseURL = "http://54.164.141.168:8000/";
const api = axios.create({
  baseURL: baseURL,
  headers: getHeaders(),
});

export default api