from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from algorithm import *

app = FastAPI()

origins = [
    "https://estgui.github.io",
    "https://tic-tac-toe-site-pxg.vercel.app"
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
    play = utility(board)
    status = analyzeBoard(board)

    result = {
        "play": play[0] if play else None,
        "victory": status[0],
        "playFields": status[1]
    }

    return result


@app.post("/isTerminal/")
def getStatus(state: State):
    board = state.model_dump()['board']

    status = analyzeBoard(board)

    result = {
        "victory": status[0],
        "playFields": status[1]
    }

    return result
