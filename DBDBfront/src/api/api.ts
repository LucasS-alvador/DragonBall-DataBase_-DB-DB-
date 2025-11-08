import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000", // Flask backend URL
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  },
  timeout: 5000, // 5 segundos de timeout
  validateStatus: function (status) {
    return status >= 200 && status < 300; // default
  }
});

// Interceptor para tratar datas antes do envio
api.interceptors.request.use((config) => {
  if (config.data) {
    // Remove campos undefined/null antes de enviar
    const cleanData = Object.fromEntries(
      Object.entries(config.data).filter(([_, v]) => v !== undefined && v !== null)
    );
    config.data = cleanData;
  }
  console.log(`[API Request] ${config.method?.toUpperCase()} ${config.url}`, {
    headers: config.headers,
    data: config.data
  });
  return config;
}, (error) => {
  console.error('[API Request Error]', error);
  return Promise.reject(error);
});

// Interceptor para tratar erros
api.interceptors.response.use(
  (response) => {
    console.log(`[API Response] ${response.config.method?.toUpperCase()} ${response.config.url}`, {
      status: response.status,
      data: response.data
    });
    return response;
  },
  (error) => {
    if (error.response) {
      // Servidor respondeu com status fora do range 2xx
      console.error('[API Response Error]', {
        status: error.response.status,
        data: error.response.data,
        headers: error.response.headers
      });
    } else if (error.request) {
      // Requisição foi feita mas não houve resposta
      console.error('[API No Response]', error.request);
    } else {
      // Erro na configuração da requisição
      console.error('[API Config Error]', error.message);
    }
    return Promise.reject(error);
  }
);

export default api;