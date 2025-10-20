export interface Obra {
  id: number;
  nome: string;
  dtIni: string;
  dtFim: string;
  imagem: string;
}

export interface Saga {
  id: number;
  desc: string;
  epIni: number;
  epFim: number;
  obra_id: number;
}

export interface Raca {
  id: number;
  nome: string;
  cor: string;
  desc: string;
  poderBase: number;
  imagem: string;
}

export interface PersonagemBase {
  id: number;
  nome: string;
  dataNasc: string;
  dataMorte?: string;
  sexo: string;
  imagem: string;
  raca_id: number;
}

export interface PersonagemSaga {
  id: number;
  poderMult: number;
  imagem: string;
  persBase_id: number;
  saga_id: number;
}

export interface Transformacao {
  id: number;
  nome: string;
  cor: string;
  especial: string;
  efeitoCol: string;
  poderMult: number;
  imagem: string;
  limMinutos: number;
}
