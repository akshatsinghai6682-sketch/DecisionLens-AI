import axios, { AxiosInstance } from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const authAPI = {
  getUsers: () => api.get('/auth/users'),
  signin: (userId: string, userName: string) =>
    api.post('/auth/signin', { user_id: userId, user_name: userName }),
  signup: (email: string, name: string) =>
    api.post('/auth/signup', { email, name }),
  logout: () => api.post('/auth/logout'),
};

export const decisionAPI = {
  create: (userId: string, title: string, description: string) =>
    api.post(`/decisions/?user_id=${userId}`, { title, description }),
  get: (decisionId: string) => api.get(`/decisions/${decisionId}`),
  listByUser: (userId: string) => api.get(`/decisions/user/${userId}`),
  updateContext: (decisionId: string, context: any) =>
    api.patch(`/decisions/${decisionId}/context`, context),
  markComplete: (decisionId: string) =>
    api.patch(`/decisions/${decisionId}/complete`),
};

export const chatAPI = {
  getQuestions: () => api.get('/chat/questions'),
  startSession: (userId: string, decisionId: string) =>
    api.post(`/chat/start-session?user_id=${userId}&decision_id=${decisionId}`),
  sendMessage: (sessionId: string, message: string) =>
    api.post(`/chat/send?session_id=${sessionId}&message=${encodeURIComponent(message)}`),
  getHistory: (sessionId: string) => api.get(`/chat/session/${sessionId}`),
};

export const scenarioAPI = {
  getByDecision: (decisionId: string) =>
    api.get(`/scenarios/decision/${decisionId}`),
  get: (scenarioId: string) => api.get(`/scenarios/${scenarioId}`),
  generate: (decisionId: string) =>
    api.post(`/scenarios/decision/${decisionId}/generate`),
};

export const reportAPI = {
  getReport: (decisionId: string) => api.get(`/reports/decision/${decisionId}`),
  exportPDF: (decisionId: string) =>
    api.post(`/reports/decision/${decisionId}/export-pdf`, {}, { responseType: 'blob' }),
};

export default api;
