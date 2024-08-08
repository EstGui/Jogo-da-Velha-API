import copy 
from random import choice


board = [[' ']*3 for _ in range(3)]


def genCordinates(num):
    row = (num - 1) // 3
    column = (num - 1) % 3

    return row, column


def genIndex(tuple):
    return tuple[0] * 3 + tuple[1]


def utility(state):
    if all([cell == '' for row in state for cell in row]):
        ini_opts = [[(0, 0), ''], [(0, 2), ''], [(2, 0), ''], [(2, 2), '']]
        return choice(ini_opts)

    actions = []
    possibilities = act(state)

    for pos in possibilities:
        new_state = result(state, pos)

        if terminal(new_state):
            value = get_state_value(new_state)
            actions.append((pos, value, 100 if value == 1 else 0))

        else:
            value, prob_x = utility(new_state)[1:]
            actions.append((pos, value, prob_x))

    if len(actions) == 8:
        pass

    if player(state) == 'X':
        maior = max([a[1] for a in actions])
        melhor = max([p[2] for p in actions if p[1] == maior])
        mel_opts = [x for x in actions if x[2] == melhor and x[1] == maior]

        rand_choice = choice(mel_opts)

        return (rand_choice[0], rand_choice[1], ([x[1] for x in actions].count(1) / len(actions)) * 100)
    
    else:
        menor = actions[0]
        for a in actions:
            if a[1] < menor[1]:
                menor = a

        return (menor[0], menor[1], ([x[1] for x in actions].count(1) / len(actions)) * 100)
    

def get_state_value(state):
    for row in state:
        if all([cell == row[0] and cell != ' ' for cell in row]):
            return 1 if row[0] == 'X' else -1 

    for col in range(3):
        if all([state[row][col] == state[0][col] and state[0][col] != ' ' for row in range(3)]):
            return 1 if state[0][col] == 'X' else -1

    if (state[0][0] == state[1][1] == state[2][2] and state[0][0] != ' ') or \
       (state[0][2] == state[1][1] == state[2][0] and state[1][1] != ' '):
        return 1 if state[1][1] == 'X' else -1
        
    return 0


def terminal(board):
    for row in board:
        if all([cell == row[0] and cell != ' ' for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == board[0][col] and board[0][col] != ' ' for row in range(3)]):
            return True

    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ') or \
       (board[0][2] == board[1][1] == board[2][0] and board[1][1] != ' '):
        return True
        
    if all([cell != ' ' for row in board for cell in row]):
        return True

    return False


def player(board):
    qtd_x = sum([row.count('X') for row in board])
    qtd_o = sum([row.count('O') for row in board])

    if qtd_x < qtd_o or (qtd_x - qtd_o) > 1:
        raise Exception('Erro')
    
    return 'X' if qtd_x == qtd_o else 'O'


def act(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']


def result(state, action):
    new_state = copy.deepcopy(state)
    new_state[action[0]][action[1]] = player(state)

    return new_state
