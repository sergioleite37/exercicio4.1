# Exercício 4.1 — API REST de uma aplicação de TODO list (POST, GET e PUT)

Aluno: Sérgio Ribeiro Leite
Disciplina: IDP-TD 2026
Framework: FastAPI + Uvicorn

## O que esta API faz

API REST que serve de backend de uma aplicação de TODO list. Gerencia tarefas
(`id`, `titulo`, `concluida`) em memória, exposta em `http://localhost:8000`.

## Estrutura

```
app/
├── __init__.py
└── main.py          # implementação da API
requirements.txt     # fastapi e uvicorn
.autograde-exercise  # marcador do autograder (conteúdo: 4.1)
```

## Contrato da API

| Método | Rota            | Corpo                                    | Resposta                                        |
|--------|-----------------|------------------------------------------|-------------------------------------------------|
| GET    | /health         | —                                        | 200 `{"status":"ok"}`                           |
| POST   | /tarefas        | `{"titulo": "<str>"}`                    | 201 `{"id":<int>,"titulo":"<str>","concluida":false}` |
| GET    | /tarefas/{id}   | —                                        | 200 tarefa; 404 se não existe                   |
| GET    | /tarefas        | —                                        | 200 lista de tarefas                            |
| PUT    | /tarefas/{id}   | `{"titulo":"<str>","concluida":<bool>}`  | 200 tarefa atualizada; 404 se não existe        |

## Como rodar

```bash
pip install -r requirements.txt
uvicorn app.main:app --port 8000
```

## Testes manuais

```bash
# Reinicie a API antes de validar (store em memória zera ao reiniciar)
curl -s http://localhost:8000/health
curl -s -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" -d '{"titulo":"estudar APIs"}'
curl -s http://localhost:8000/tarefas/1
curl -s http://localhost:8000/tarefas
curl -s -X PUT http://localhost:8000/tarefas/1 \
  -H "Content-Type: application/json" \
  -d '{"titulo":"estudar APIs REST","concluida":true}'
```

## Validação

```bash
autograde validar 4.1
```
