import time
import random

def bucar_usuario_hash(hash, nome):
    return hash.get(nome, "Usuario não encontrado")

def buscar_usuario_lista(lista, nome):
    for usuario in lista:
        if usuario["nome_usuario"] == nome:
            return usuario
    return "Usuario não encontrado"

def cria_usuarios(num_usuarios):
    usuarios = []
    for i in range(num_usuarios):
        nome_usuario = f"usuario_{i}"
        nome = f"Usuario {i}"
        email = f"{nome_usuario}@example.com"
        usuarios.append({"nome_usuario": nome_usuario, "nome": nome, "email": email})
    return usuarios

lista_usuarios = cria_usuarios(10000)
hash_usuarios = {usuario["nome_usuario"]: usuario for usuario in lista_usuarios}
alvo = random.choice(lista_usuarios)["nome_usuario"]

# Hash
inicio_h = time.time()
bucar_usuario_hash(hash_usuarios, alvo)
hash_t = time.time() - inicio_h
print(f"Tempo (Hashtable): {hash_t:.6f}")

# Lista
inicio_l = time.time()
buscar_usuario_lista(lista_usuarios, alvo)
lista_t = time.time() - inicio_l
print(f"Tempo (Hashtable): {lista_t:.6f}")