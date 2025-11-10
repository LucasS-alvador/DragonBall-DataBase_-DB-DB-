# Setup do Backend DragonBall-DataBase

## 1. Criar e Ativar o Ambiente Virtual

Na pasta `DBDBback`, execute:

Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:
```
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Instalar Dependências

Com o ambiente virtual ativado:
```
pip install -r setup/requirements.txt
```

## 3. Configurar Variáveis de Ambiente

Windows (PowerShell):
```
$env:PYTHONPATH="."
$env:MY_DB="SQLITE"
```

Windows (CMD):
```
set PYTHONPATH=.
set MY_DB=SQLITE
```

Linux/macOS:
```
export PYTHONPATH=.
export MY_DB=SQLITE
```

## 4. Criar o Banco de Dados

```
python setup/create_database.py
```

## 5. Popular o Banco de Dados (Opcional)

Se desejar adicionar dados iniciais:
```
python setup/populate_db.py
```

## 6. Executar o Backend

Da pasta `DBDBback`:
```
python src/app.py
```

O servidor estará disponível em: http://localhost:5000

## 7. Executar Testes (Opcional)

Para executar os testes:
```
python -m pytest
```

## Notas:
- O arquivo `fix_imports.py` e `cleanup_duplicate_races.py` não são mais necessários, pois foram usados apenas para correções pontuais.
- Mantenha o ambiente virtual (.venv) na raiz do projeto (pasta DBDBback)
- Se precisar adicionar novas dependências, use `pip install <pacote>` e depois atualize o requirements.txt:
  ```
  pip freeze > setup/requirements.txt
  ```