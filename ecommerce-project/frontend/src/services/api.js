import axios from "axios";

const API = axios.create({
  baseURL: "https://ecommerce-production-bd08.up.railway.app",
});

export default API;