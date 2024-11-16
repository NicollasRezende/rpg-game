class Item:
    def __init__(self, nome, tipo, efeito):
        self.nome = nome
        self.tipo = tipo
        self.efeito = efeito

    def usar(self, alvo):
        if self.tipo == "poção":
            if self.efeito == "cura":
                alvo.vida += 10  # Cura 10 pontos de vida
                print(f"{alvo.nome} recuperou 10 pontos de vida.")
            # Adicionar mais efeitos conforme necessário
        elif self.tipo == "arma":
            alvo.forca += 5  # Aumenta a força temporariamente
            print(f"{alvo.nome} aumentou a força em 5 pontos.")
        # Adicionar mais tipos conforme necessário