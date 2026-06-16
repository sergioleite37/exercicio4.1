from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Store em memória. Zera quando o processo reinicia.
_tarefas: dict[int, dict] = {}
_proximo_id = 1


class TarefaIn(BaseModel):
    titulo: str


class TarefaUpdate(BaseModel):
    titulo: str
    concluida: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tarefas", status_code=201)
def criar(tarefa: TarefaIn):
    global _proximo_id
    nova = {"id": _proximo_id, "titulo": tarefa.titulo, "concluida": False}
    _tarefas[_proximo_id] = nova
    _proximo_id += 1
    return nova

@app.get("/tarefas/{id}")
def obter_tarefa(id: int):
    if id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    return _tarefas[id]

# TODO: implemente GET /tarefas e PUT /tarefas/{id}
