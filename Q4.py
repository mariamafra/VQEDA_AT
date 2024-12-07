import random
import time

def busca_binaria(lista, alvo): 
    inicio = 0
    fim = len(lista) - 1 
    count = 0

    while inicio <= fim: 
        count += 1
        meio = (inicio + fim) // 2 

        if lista[meio] == alvo: 
            return meio, count
        elif lista[meio] > alvo: 
            fim = meio - 1 
        else:
            inicio = meio + 1 
    
    return -1

def busca_linear(lista, alvo):
    count = 0
    for i in range(len(lista)):
        count += 1
        if lista[i] == alvo:
            return i, count
    return -1

lista_ISBNS = sorted([random.randint(1, 1000000) for i in range(100000)])
alvo = random.choice(lista_ISBNS)

# Busca Binária
inicio = time.time()
resultado_b, count_b = busca_binaria(lista_ISBNS, alvo)
fim = time.time()
tempo_binario = fim - inicio
print(f"Busca Binária - ISBN {alvo} encontrado no índice {resultado_b} em {count_b} iterações e {tempo_binario:.6f} segundos.")

# Busca Linear
inicio = time.time()
resultado_l, count_l = busca_linear(lista_ISBNS, alvo)
fim = time.time()
tempo_linear = fim - inicio
print(f"Busca Linear - ISBN {alvo} encontrado no índice {resultado_l} em {count_l} iterações e {tempo_linear:.6f} segundos.")