import random
import time

def bubble_sort(lista): 
    n = len(lista) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if lista[j] > lista[j+1]: 
                lista[j], lista[j+1] = lista[j+1], lista[j] 

# Lista 1K
lista_1k = [random.randint(1, 1000) for _ in range(1000)]
inicio = time.time()
lista_1k_result = bubble_sort(lista_1k)
fim = time.time()
tempo_1k = fim - inicio
print(f"Tempo de execução para 1.000 elementos: {tempo_1k:.6f} segundos")

# Lista 1K
lista_10k = [random.randint(1, 10000) for _ in range(10000)]
inicio = time.time()
lista_10k_result = bubble_sort(lista_10k)
fim = time.time()
tempo_10k = fim - inicio
print(f"Tempo de execução para 10.000 elementos: {tempo_10k:.6f} segundos")