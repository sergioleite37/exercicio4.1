from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

_tarefas: dict[int, dict] = {}
_proximo_id = 1


class TarefaIn(BaseModel):
    titulo: str


class TarefaUpdate(BaseModel):
    titulo: str
    concluida: bool


class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tarefas", status_code=status.HTTP_201_CREATED, response_model=Tarefa)
def criar_tarefa(payload: TarefaIn):
    global _proximo_id

    tarefa = {
        "id": _proximo_id,
        "titulo": payload.titulo,
        "concluida": False
    }

    _tarefas[_proximo_id] = tarefa
    _proximo_id += 1
    return tarefa


@app.get("/tarefas/{id}", response_model=Tarefa)
def obter_tarefa(id: int):
    if id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    return _tarefas[id]


@app.get("/tarefas", response_model=list[Tarefa])
def listar_tarefas():
    return list(_tarefas.values())


@app.put("/tarefas/{id}", response_model=Tarefa)
def atualizar_tarefa(id: int, payload: TarefaUpdate):
    if id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")

    tarefa = {
        "id": id,
        "titulo": payload.titulo,
        "concluida": payload.concluida
    }

    _tarefas[id] = tarefa
    return tarefa