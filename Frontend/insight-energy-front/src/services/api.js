import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // ou o link do backend no render após o deploy
});

export default api;
