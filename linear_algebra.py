def refletir_horizontal(array):
    corr = [
        [0, 6], [1, 7], [2, 8],
        [3], [4], [5]
    ]
    
    for i in range(3):
        if array[i] != array[6 + i]:
            return []
    
    return [pair for pair in corr if all(array[idx] is None for idx in pair)]


def refletir_vertical(array):
    corr = [
        [0, 2], [1],
        [3, 5], [4],
        [6, 8], [7]
    ]
    
    for i in range(3):
        if array[i * 3:i * 3 + 3] != array[i * 3:i * 3 + 3][::-1]:
            return []
    
    return [pair for pair in corr if all(array[idx] is None for idx in pair)]


def refletir_diagonal_principal(array):
    corr = [
        [0],
        [1, 3],
        [2, 6],
        [4],
        [5, 7],
        [8]
    ]

    nova_array = [
        array[0], array[3], array[6],
        array[1], array[4], array[7],
        array[2], array[5], array[8]
    ]

    if array == nova_array:
        return [pair for pair in corr if all(array[idx] is None for idx in pair)]
    
    return []


def refletir_diagonal_secundaria(array):
    corr = [
        [0, 8], [1, 5], [2],
        [3, 7], [4],
        [6]
    ]
    
    nova_array = [
        array[8], array[5], array[2],
        array[7], array[4], array[1],
        array[6], array[3], array[0]
    ]

    if array == nova_array:
        return [pair for pair in corr if all(array[idx] is None for idx in pair)]
    
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
