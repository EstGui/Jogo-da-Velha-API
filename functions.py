from random import choice
from alg_lin import conferirSimetrias


def genCordinates(num):
    return divmod(num - 1, 3)


def genIndex(tuple):
    return tuple[0] * 3 + tuple[1]


def utility(state):
    actions = []
    possibilities = act(state)

    for pos in possibilities:
        new_state = result(state, pos[0])

        result_value, result_info = analyze_board(new_state)

        if result_info is not None:
            value = result_value
            actions.append((pos, value, 100 if value == 1 else 0))
        else:
            value, prob_x = utility(new_state)[1:]
            actions.append((pos, value, prob_x))


    if player(state) == 'X':
        minmax = max([a[1] for a in actions])
        melhor = max([p[2] for p in actions if p[1] == minmax])
    else:
        minmax = min([a[1] for a in actions])
        melhor = min([p[2] for p in actions if p[1] == minmax])

    mel_opts = [x for x in actions if x[1] == minmax and x[2] == melhor]
    rand_choice = choice(mel_opts)

    return (choice(rand_choice[0]), rand_choice[1], (sum([len(x[0]) for x in actions if x[1] == 1]) / sum(len(x[0]) for x in actions)) * 100)
    

def analyze_board(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return 1 if board[i][0] == 'X' else -1, [i * 3, i * 3 + 1, i * 3 + 2]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return 1 if board[0][i] == 'X' else -1, [i, i + 3, i + 6]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return 1 if board[0][0] == 'X' else -1, [0, 4, 8]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return 1 if board[0][2] == 'X' else -1, [2, 4, 6]

    if all(cell != '' for row in board for cell in row):
        return 0, True 

    return 0, None 


def player(board):
    qtd_x = sum([row.count('X') for row in board])
    qtd_o = sum([row.count('O') for row in board])

    if qtd_x < qtd_o or (qtd_x - qtd_o) > 1:
        raise Exception('Erro')
    
    return 'X' if qtd_x == qtd_o else 'O'


def act(board):
    simetrics = conferirSimetrias(board)

    if simetrics:
        return simetrics
    else:
        return [[(row, col)] for row in range(3) for col in range(3) if board[row][col] == '']


def result(state, action):
    new_state = [row[:] for row in state]
    new_state[action[0]][action[1]] = player(state)

    return new_state
