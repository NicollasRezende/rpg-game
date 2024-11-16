from .character import Character

class Player(Character):
    def __init__(self, nome, classe, forca, defesa, vida, agilidade):
        super().__init__(nome, forca, defesa, vida, agilidade)
        self.classe = classe
        self.nivel = 1
        self.experiencia = 0
        self.inventario = []
        self.missoes = []
        self.max_vida = vida  # Adicionar vida máxima
        self.dinheiro = 0     # Sistema de moeda
        
    def ganhar_experiencia(self, exp):
        self.experiencia += exp
        exp_necessaria = self.nivel * 100  # Fórmula para level up
        if self.experiencia >= exp_necessaria:
            self.subir_nivel()
    
    def subir_nivel(self):
        self.nivel += 1
        self.forca += 2
        self.defesa += 1
        self.max_vida += 5
        self.vida = self.max_vida
        print(f"Nível {self.nivel}! Seus atributos aumentaram!")