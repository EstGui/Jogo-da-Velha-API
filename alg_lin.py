def refletir_horizontal(matriz):
    corr = ([(0, 0), (2, 0)], [(0, 1), (2, 1)], [(0, 2), (2, 2)], [(1, 0)], [(1, 1)], [(1, 2)])

    for i in range(3):
        if matriz[i] != matriz[2 - i]:
            return []
        
    return [e for e in corr if matriz[e[0][0]][e[0][1]] == '']


def refletir_vertical(matriz):
    corr = ([(0, 0), (0, 2)], [(0, 1)], [(1, 0), (1, 2)], [(1, 1)], [(2, 0), (2, 2)], [(2, 1)])
    
    for i in range(3):
        if matriz[i] != matriz[i][::-1]:
            return []
    
    return [e for e in corr if matriz[e[0][0]][e[0][1]] == '']



def refletir_diagonal_principal(matriz):
    corr = [[(0, 0)], [(0, 1), (1, 0)], [(0, 2), (2, 0)], [(1, 1)], [(1, 2), (2, 1)], [(2, 2)]]
    nova_matriz = [[matriz[j][i] for j in range(3)] for i in range(3)]

    if matriz == nova_matriz:
        return [e for e in corr if matriz[e[0][0]][e[0][1]] == '']
    
    return []


def refletir_diagonal_secundaria(matriz):
    corr = [[(0, 0), (2, 2)], [(0, 1), (1, 2)], [(0, 2)], [(1, 0), (2, 1)], [(1, 1)], [(2, 0)]]
    nova_matriz = [[matriz[2-j][2-i] for j in range(3)] for i in range(3)]

    if matriz == nova_matriz:
        return [e for e in corr if matriz[e[0][0]][e[0][1]] == '']
    
    return []


def agruparCorrelacoes(lista):
    sets = [set(lst) for lst in lista]

    grouped = []
    while sets:
        current_set = sets.pop()
        combined_set = current_set.copy()
        
        i = 0
        while i < len(sets):
            if combined_set & sets[i]:
                combined_set.update(sets.pop(i))
            else:
                i += 1
        
        grouped.append(sorted(combined_set))
    
    for i in range(len(grouped)):
        for j in range(i + 1, len(grouped)):
            if set(grouped[i]) & set(grouped[j]):
                return agruparCorrelacoes(grouped)
    
    return grouped


def conferirSimetrias(matriz):
    simetrias = []

    simetrias.append(refletir_horizontal(matriz))
    simetrias.append(refletir_vertical(matriz))
    simetrias.append(refletir_diagonal_principal(matriz))
    simetrias.append(refletir_diagonal_secundaria(matriz))

    if len(simetrias) > 1:
        flattened_lists = [item for sublist in simetrias for item in sublist]
        simetrias = agruparCorrelacoes(flattened_lists)

    elif len(simetrias) == 1:
        simetrias = simetrias[0]

    return simetrias


# matriz = [['X', '', ''],
#           ['', 'O', ''],
#           ['', '', '']]

# print(conferirSimetrias(matriz))
