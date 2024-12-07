def selection_sort(jogadores):
    n = len(jogadores) 
    
    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if jogadores[j]['pontos'] < jogadores[min_index]['pontos']: 
                min_index = j
        jogadores[i], jogadores[min_index] = jogadores[min_index], jogadores[i]

    return jogadores

jogadores = [
    {'nome': 'Regina', 'pontos': 781},
    {'nome': 'Fabio', 'pontos': 250},
    {'nome': 'Carla', 'pontos': 987},
    {'nome': 'Alberto', 'pontos': 351}
]

jogadores_ordenaods = selection_sort(jogadores)
for jorgador in jogadores_ordenaods:
    print(f"{jorgador['nome']}: {jorgador['pontos']}")