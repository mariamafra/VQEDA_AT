class Fila:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, item):
        self.itens.append(item)
        print(f"Chamado '{item}' adicionado à fila.")

    def dequeue(self):
        if self.is_empty():
            print("Nenhum chamado na fila para atender.")
            return None
        else:
            item = self.itens.pop(0)
            print(f"Chamado '{item}' atendido.")
            return item

    def display(self):
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:", end=" ")
            for item in self.itens:
                print(item, end=" ")
            print()

sistema_atendimento = Fila()

sistema_atendimento.enqueue("Chamado 1")
sistema_atendimento.enqueue("Chamado 2")
sistema_atendimento.enqueue("Chamado 3")

sistema_atendimento.display()

sistema_atendimento.dequeue()
sistema_atendimento.dequeue()

sistema_atendimento.display()

# Tentando atender mais chamados
sistema_atendimento.dequeue()
sistema_atendimento.dequeue()
