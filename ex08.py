def selection_sort(jogadores):
    n = len(jogadores)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if jogadores[j]['pontuação'] < jogadores[min_index]['pontuação']:
                min_index = j

        jogadores[i], jogadores[min_index] = jogadores[min_index], jogadores[i]
    return jogadores

jogadores = [
    {"nome": "Joao", "pontuação": 2},
    {"nome": "Pedro", "pontuação": 7.5},
    {"nome": "Carol", "pontuação": 9.9},
    {"nome": "Diego", "pontuação": 4}
]


print(selection_sort(jogadores))
