from .character import Character

class Enemy(Character):
    def __init__(self, nome, forca, defesa, vida, agilidade, dificuldade, recompensa_experiencia, itens_drop):
        super().__init__(nome, forca, defesa, vida, agilidade)
        self.dificuldade = dificuldade
        self.recompensa_experiencia = recompensa_experiencia
        self.itens_drop = itens_drop