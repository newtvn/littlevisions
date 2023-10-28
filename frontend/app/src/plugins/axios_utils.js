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
let baseURL = "https://littlevisions.meevy.me/";
const api = axios.create({
  baseURL: baseURL,
  headers: getHeaders(),
});

export default api