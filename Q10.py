
class Navegador:
    def __init__(self):
        self.pilha_voltar = []
        self.pilha_avancar = []
        self.pagina_atual = None

    def navegar(self, pagina):
        if self.pagina_atual:
            self.pilha_voltar.append(self.pagina_atual)
        self.pagina_atual = pagina
        print(f"Navegando para: {pagina}")
        self.pilha_avancar.clear() 

    def voltar(self):
        if not self.pilha_voltar:
            print("Não há páginas para voltar.")
            return

        self.pilha_avancar.append(self.pagina_atual)
        self.pagina_atual = self.pilha_voltar.pop()
        print(f"Voltando para: {self.pagina_atual}")

    def avancar(self):
        if not self.pilha_avancar:
            print("Não há páginas para avançar.")
            return

        self.pilha_voltar.append(self.pagina_atual)
        self.pagina_atual = self.pilha_avancar.pop()
        print(f"Avançando para: {self.pagina_atual}")

    def mostrar_estado(self):
        print(f"Página atual: {self.pagina_atual}")
        print(f"Histórico (Voltar): {self.pilha_voltar}")
        print(f"Histórico (Avançar): {self.pilha_avancar}")

navegador = Navegador()

navegador.navegar("Instagram")
navegador.navegar("TikTok")
navegador.navegar("Pinterest")
navegador.mostrar_estado()

navegador.voltar()
navegador.mostrar_estado()

navegador.voltar()
navegador.mostrar_estado()

navegador.avancar()
navegador.mostrar_estado()

navegador.navegar("Twitter")
navegador.mostrar_estado()

navegador.voltar()
navegador.voltar()
navegador.avancar()
navegador.mostrar_estado()
