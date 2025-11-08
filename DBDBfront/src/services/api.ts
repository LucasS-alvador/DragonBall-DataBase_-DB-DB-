import api from '../api/api';
import { Obra, Saga, Raca, Transformacao, PersonagemBase, PersonagemSaga } from '../types/models';

// Obras
export const obraService = {
  getAll: () => api.get('/obra').then(res => res.data.details),
  getById: (id: number) => api.get(`/obra/${id}`).then(res => res.data),
  create: (obra: Omit<Obra, 'id'>) => {
    console.log('[API] Criando obra:', obra);
    return api.post('/obra', obra)
      .then(res => {
        console.log('[API] Resposta da criação:', res.data);
        return res.data;
      })
      .catch(error => {
        console.error('[API] Erro ao criar obra:', error.response?.data || error);
        throw error;
      });
  },
  delete: (id: number) => api.delete(`/obra/${id}`).then(res => res.data),
};

// Sagas
export const sagaService = {
  getAll: () => api.get('/saga').then(res => res.data.details),
  getById: (id: number) => api.get(`/saga/${id}`).then(res => res.data),
  create: (saga: Omit<Saga, 'id'>) => {
    console.log('[API] Criando saga:', saga);
    return api.post('/saga', saga)
      .then(res => {
        console.log('[API] Resposta da criação:', res.data);
        return res.data;
      })
      .catch(error => {
        console.error('[API] Erro ao criar saga:', error.response?.data || error);
        throw error;
      });
  },
  delete: (id: number) => api.delete(`/saga/${id}`).then(res => res.data),
};

// Raças
export const racaService = {
  getAll: () => api.get('/raca').then(res => res.data.details),
  getById: (id: number) => api.get(`/raca/${id}`).then(res => res.data),
  create: (raca: Omit<Raca, 'id'>) => api.post('/raca', raca).then(res => res.data),
  delete: (id: number) => api.delete(`/raca/${id}`).then(res => res.data),
};

// Transformações
export const transformacaoService = {
  getAll: () => api.get('/transformacao').then(res => res.data.details),
  getById: (id: number) => api.get(`/transformacao/${id}`).then(res => res.data),
  create: (trans: Omit<Transformacao, 'id'>) => api.post('/transformacao', trans).then(res => res.data),
  delete: (id: number) => api.delete(`/transformacao/${id}`).then(res => res.data),
};

// Personagens Base
export const personagemBaseService = {
  getAll: () => api.get('/personagembase').then(res => res.data.details),
  getById: (id: number) => api.get(`/personagembase/${id}`).then(res => res.data),
  create: (pers: Omit<PersonagemBase, 'id'>) => api.post('/personagembase', pers).then(res => res.data),
  delete: (id: number) => api.delete(`/personagembase/${id}`).then(res => res.data),
};

// Personagens em Sagas
export const personagemSagaService = {
  getAll: () => api.get('/personagemsaga').then(res => res.data.details),
  getById: (id: number) => api.get(`/personagemsaga/${id}`).then(res => res.data),
  create: (pers: Omit<PersonagemSaga, 'id'>) => api.post('/personagemsaga', pers).then(res => res.data),
  delete: (id: number) => api.delete(`/personagemsaga/${id}`).then(res => res.data),
};