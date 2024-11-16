class Missao:
    def __init__(self, nome, descricao, objetivo, recompensa):
        self.nome = nome
        self.descricao = descricao
        self.objetivo = objetivo
        self.recompensa = recompensa
        self.completa = False

    def verificar_objetivo(self, jogador):
        if self.objetivo(jogador):
            self.completa = True
            print(f"Missão '{self.nome}' completa!")
            self.recompensa(jogador)
        else:
            print(f"Missão '{self.nome}' ainda não completa.")

def adicionar_missao(jogador, missao):
    jogador.missoes.append(missao)
    print(f"Missão '{missao.nome}' adicionada!")

def verificar_missoes(jogador):
    for missao in jogador.missoes:
        missao.verificar_objetivo(jogador)