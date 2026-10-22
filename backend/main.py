from fastapi import FastAPI  # importa o FastAPI

from fastapi.middleware.cors import CORSMiddleware  # importa o middleware de CORS

from rotas import clientes         # importa as rotas de clientes
app = FastAPI()              # cria a aplicação

# Configura quais origens têm permissão de chamar a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # "*" = qualquer origem (usado em desenvolvimento)
    allow_methods=["*"],      # permite todos os métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],      # permite todos os cabeçalhos
)

app.include_router(clientes.router)  # registra as rotas de clientes na API

@app.get("/")                # define que essa função responde ao endereço "/"
def inicio():                # quando alguém acessar "/", essa função vai rodar
    return {"mensagem": "API do estúdio de tatuagem funcionando!"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rotas import clientes, senioridade   # ← adiciona senioridade aqui

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes.router)
app.include_router(senioridade.router)   # ← registra a nova rota


@app.get("/")
def inicio():
    return {"mensagem": "API do estúdio de tatuagem funcionando!"}