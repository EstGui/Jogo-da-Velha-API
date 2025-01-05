from random import choice
from linear_algebra import conferirSimetrias


def genCordinates(index: int) -> tuple:
    """
    Retorna coordenadas de uma matriz 3x3 a partir de indice de array.

    Args:
        index = index

    Returns:
        tuple: coordenadas da matriz.
    """
    return divmod(index - 1, 3)


def genIndex(tuple: tuple) -> int:
    """
    Retorna o index de uma matriz 3x3 após dump

    Args:
        Tupla com coordenadas de matriz 3x3

    Returns:
        int: índice correspondete à coordenada.
    """
    return tuple[0] * 3 + tuple[1]


def utility(state):
    possibilities = act(state)
    actions = []

    if possibilities:
        for p in possibilities:
            new_state = result(state, p[0])

            result_value, result_info = analyzeBoard(new_state)

            if result_info:
                actions.append((p, result_value, 100 if result_value == 1 else 0))
            else:
                value, prob_x = utility(new_state)[1:]
                actions.append((p, value, prob_x))

        rand_choice = getBestMove(state, actions)

        return (choice(rand_choice[0]),
                rand_choice[1],
                (sum([len(x[0]) for x in actions if x[1] == 1]) / sum(len(x[0]) for x in actions)) * 100)
    else:
        return None


def getBestMove(state, actions):
    if player(state) == 'X':
        minmax = max([a[1] for a in actions])
        melhor = max([p[2] for p in actions if p[1] == minmax])
    else:
        minmax = min([a[1] for a in actions])
        melhor = min([p[2] for p in actions if p[1] == minmax])

    mel_opts = [x for x in actions if x[1] == minmax and x[2] == melhor]
    rand_choice = choice(mel_opts)

    return rand_choice


def analyzeBoard(board):
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] and board[i * 3] != None:
            return 1 if board[i * 3] == 'X' else -1, [i * 3, i * 3 + 1, i * 3 + 2]
        if board[i] == board[i + 3] == board[i + 6] and board[i] != None:
            return 1 if board[i] == 'X' else -1, [i, i + 3, i + 6]

    if board[0] == board[4] == board[8] and board[0] != None:
        return 1 if board[0] == 'X' else -1, [0, 4, 8]
    if board[2] == board[4] == board[6] and board[2] != None:
        return 1 if board[2] == 'X' else -1, [2, 4, 6]

    if all(cell != None for cell in board):
        return 0, True

    return 0, None


def player(board):
    qtd_x = board.count('X') 
    qtd_o = board.count('O')

    if qtd_x < qtd_o or (qtd_x - qtd_o) > 1:
        raise Exception('Erro')

    return 'X' if qtd_x == qtd_o else 'O'


def act(board):
    simetrics = conferirSimetrias(board)

    if simetrics:
        return simetrics

    return [[cell] for cell, value in enumerate(board) if value is None]


def result(state, action):
    new_state = state[:]
    new_state[action] = player(state)

    return new_state
