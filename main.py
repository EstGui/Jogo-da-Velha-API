from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from functions import *

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "https://estgui.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class State(BaseModel):
    board: list

@app.post("/play/")
def get_data(state: State):
    board = state.model_dump()['board']
    new_board = genIndex(utility(board)[0])
    return new_board


@app.post("/isTerminal/")
def getStatus(state: State):
    board = state.model_dump()['board']
    return terminal(board)
