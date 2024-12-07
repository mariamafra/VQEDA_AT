def verificar_duplicatas_hash(lista):
    checked = {}
    for elem in lista:
        if elem in checked:
            return True
        checked[elem] = True
    return False

lista = [1, 5, 7, 9, 9, 0]
print(f"A lista {lista} tem duplicatas? {verificar_duplicatas_hash(lista)}")
lista = [1, 5, 7, 8, 9, 0]
print(f"A lista {lista} tem duplicatas? {verificar_duplicatas_hash(lista)}")