
def busca_linear_contato(lista_contatos, nome):
    for contato in lista_contatos:
        if contato["nome"] == nome:
            return contato["telefone"]
    return None

def exibir(telefone, nome):
    if telefone:
        print(f"Número de telefone de {nome}: {telefone}")
    else:
        print(f"Contato {nome} não encontrado.")

lista_contatos = [
    {"nome": "Maria", "telefone": "874445236"},
    {"nome": "Jota", "telefone": "988577412"},
    {"nome": "Ana", "telefone": "253641523"},
    {"nome": "Paulo", "telefone": "985458985"}
]

nome = "Paulo"
telefone = busca_linear_contato(lista_contatos, nome)
exibir(telefone, nome)

nome = "Cris"
telefone = busca_linear_contato(lista_contatos, nome)
exibir(telefone, nome)