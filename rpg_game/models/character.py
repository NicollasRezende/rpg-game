class Character:
    def __init__(self, nome, forca, defesa, vida, agilidade):
        self.nome = nome
        self.forca = forca
        self.defesa = defesa
        self.vida = vida
        self.agilidade = agilidade

    def atacar(self, alvo):
        dano = self.forca - alvo.defesa
        return max(dano, 0)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0