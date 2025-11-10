# DragonBall DataBase — Guia Completo

Este documento descreve o projeto completo (backend + frontend), explica a estrutura do repositório, como configurar o ambiente, criar e popular o banco, executar a aplicação localmente, onde estão as rotas e modelos e dicas de troubleshooting.

Resumo rápido
- Backend: Python + Flask, arquivos em `DBDBback/src`.
- Frontend: Next.js + React (TypeScript), arquivos em `DBDBfront/src`.
- Ambiente virtual recomendado: `.venv` na pasta `DBDBback`.

Índice
- Visão Geral
- Estrutura do Repositório
- Backend
  - Requisitos
  - Criar e ativar o venv
  - Instalar dependências
  - Variáveis de ambiente
  - Criar e popular o banco de dados
  - Executar o backend
  - Rotas / API endpoints importantes
  - Testes
- Frontend
  - Requisitos
  - Instalar dependências e rodar
  - Rotas / Páginas importantes
  - Tipos e serviços de API
- Desenvolvimento e Troubleshooting
  - Problemas comuns e soluções
  - Notas sobre imports e `PYTHONPATH`
  - Aviso Next.js sobre `params` sendo Promise
- Contribuição
- Licença / Notas

---

**Visão Geral**

Este projeto é um CRUD simples para armazenar e exibir dados do universo Dragon Ball: Obras, Sagas, Raças, Transformações, Personagens (base e por saga). O backend fornece endpoints REST em Flask; o frontend é um app Next.js que consome esses endpoints.

---

**Estrutura do repositório (resumida)**

- `DBDBback/` — backend
  - `src/` — código-fonte Python
    - `app.py` — entrypoint Flask
    - `database.py` — configuração SQLAlchemy
    - `config.py` — configurações e leitura de variáveis
    - `model/` — modelos SQLAlchemy (Obra, Saga, Raca, Transformacao, PersonagemBase, PersonagemSaga)
    - `route/routes.py` — rotas e endpoints
    - `service/` — lógica comum (create/get/delete)
  - `setup/` — scripts de utilitários: `create_database.py`, `populate_db.py`, `requirements.txt`, `readme.MD` (setup específico)
- `DBDBfront/` — frontend Next.js (TypeScript)
  - `src/` — código front
    - `app/` — páginas (incluindo `racas`, `obras`, etc.)
    - `components/` — componentes React (Card, FormField...)
    - `services/` — client API (axios wrapper)
    - `types/` — interfaces TypeScript

---

## Backend

Requisitos
- Python 3.10+ (o projeto foi testado com Python 3.13 no ambiente de desenvolvimento)
- Git (para clonar)

Criar e ativar ambiente virtual (na pasta `DBDBback`)

Windows (CMD):

```cmd
cd DBDBback
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS:

```bash
cd DBDBback
python3 -m venv .venv
source .venv/bin/activate
```

Instalar dependências:

```bash
pip install -r setup/requirements.txt
```

Variáveis de ambiente
- `PYTHONPATH` deve incluir a pasta `DBDBback/src` (normalmente o README e scripts cuidam disso adicionando `.` ou `src` ao sys.path)
- `MY_DB` pode ser usado para selecionar o tipo de DB (o código usa `SQLITE` por padrão)

Exemplos (Windows CMD):

```cmd
set PYTHONPATH=.
set MY_DB=SQLITE
```

Criar o banco de dados

O projeto inclui um script para criar o banco e outro para popular dados de exemplo. Antes de rodar, certifique-se de estar na raiz `DBDBback` e do venv ativado.

```cmd
python setup/create_database.py
python setup/populate_db.py  # opcional: popula com exemplos
```

Observação: os scripts `create_database.py` e `populate_db.py` foram ajustados para adicionar `src` ao `sys.path`, então podem ser executados a partir da raiz `DBDBback`.

Executar o backend

Você pode iniciar o servidor diretamente:

```cmd
cd DBDBback
.venv\Scripts\activate
set PYTHONPATH=.
python src/app.py
```

O servidor ficará em `http://localhost:5000` por padrão.

Rotas / API endpoints (resumo)
- `GET /api/<model>` — lista todos (ex: `/api/raca`)
- `GET /api/<model>/<id>` — busca por id (ex: `/api/raca/1`)
- `POST /raca` — cria raça (corpo JSON)
- `POST /saga` — cria saga (ver validações em routes.py)
- `DELETE /raca/<id>` — deleta por id

Além disso existem endpoints específicos listados em `src/route/routes.py` (recomendo abrir e conferir as validações e exemplos de retorno).

Testes backend

Há testes em `tests/` e `DBDBback/tests/pytest`. Rodar:

```cmd
cd DBDBback
.venv\Scripts\activate
python -m pytest
```

---

## Frontend (Next.js + TypeScript)

Requisitos
- Node.js 18+ (ou recomendado pela versão do projeto)
- npm ou yarn

Instalar dependências e rodar em dev:

```bash
cd DBDBfront
npm install
npm run dev
```

O frontend normalmente roda em `http://localhost:3000`.

Arquitetura no frontend
- `src/services/api.ts` contém os serviços que consomem a API do backend (ex.: `racaService.getAll()`, `personagemBaseService.getById(id)`).
- `src/types/models.ts` descreve as interfaces usadas no cliente. Mantenha estas interfaces alinhadas aos campos que o backend envia (ex.: `dataNasc`, `descricao`).
- Páginas de listagem (ex.: `/racas`) mapeiam dados para o componente `Card` e linkam para páginas de detalhes em `/racas/[id]`.
- Páginas de detalhe (em cada pasta `[id]`) usam um `useEffect` para buscar por id do serviço `getById`.

Nota importante (Next.js):
- Em versões recentes do Next.js (app router), o objeto `params` pode ser uma Promise em runtime; acessar `params.id` diretamente pode disparar um aviso no console. Nas páginas de detalhes foi adotado um padrão seguro:

```ts
const p = await Promise.resolve(params);
const id = typeof p.id === 'string' ? parseInt(p.id) : p.id;
```

Isso evita o aviso e funciona tanto se `params` vier sincronamente quanto como Promise.

Testes e build

Para checar erros TypeScript:

```bash
cd DBDBfront
npx tsc --noEmit
```

Para gerar um build de produção:

```bash
npm run build
npm run start
```

---

## Desenvolvimento e Troubleshooting

Problemas comuns

- "ModuleNotFoundError: No module named 'src'" ou "No module named 'app'":
  - Execute scripts a partir da raiz `DBDBback`.
  - Use `set PYTHONPATH=.` (Windows) ou `export PYTHONPATH=.` (Linux/macOS) antes de rodar, ou confie nos scripts em `setup/` que adicionam `src` ao `sys.path`.

- Erros de tipos no frontend (VSCode apontando `data_nasc` vs `dataNasc`):
  - Garanta que `src/types/models.ts` esteja alinhado com os campos que o backend retorna (`to_dict()` nos modelos). Ajuste nomes (campos como `dataNasc`, `descricao`, `poderMult` etc.).

- Aviso Next.js sobre `params` ser Promise:
  - Use `await Promise.resolve(params)` nas páginas client-side antes de acessar `id`.
  - Alternativa: converter a página para Server Component (buscar dados no servidor) para evitar hooks no cliente.

Logs e debugging
- Verifique o terminal do backend ao reproduzir erros — exceptions aparecem lá.
- No frontend, abra DevTools → Network para ver requisições que retornam 4xx/5xx e a URL exata.

Scripts auxiliares
- `setup/fix_imports.py` foi usado para ajustar rapidamente imports `from src.*` para imports relativos. Não é necessário para execução, foi uma correção rápida local.
- `setup/cleanup_duplicate_races.py` é um script de manutenção opcional para limpar dados duplicados no DB.

---

## Como adicionar uma nova entidade (ex.: "Item") — passo rápido
1. Backend:
   - Criar `src/model/item.py` definindo a classe SQLAlchemy e `to_dict()`.
   - Registrar rotas (GET/POST/DELETE) em `src/route/routes.py` (ou criar um módulo de rotas e importar em `app.py`).
2. Frontend:
   - Adicionar interface em `DBDBfront/src/types/models.ts`.
   - Criar serviço em `DBDBfront/src/services/api.ts` com `getAll/getById/create/delete` apontando para `/api/item`.
   - Criar página de listagem e página de detalhe seguindo o padrão das outras entidades.

---

## Contribuição
- Faça fork e PR. Mantenha alterações pequenas e documentadas.
- Adicione testes sempre que possível.

---