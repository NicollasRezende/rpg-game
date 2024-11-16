from models.player import Player
from models.enemy import Enemy

def iniciar_combate(jogador, inimigo):
    print(f"Você encontrou um {inimigo.nome}!")
    
    while jogador.vida > 0 and inimigo.vida > 0:
        print(f"\n{jogador.nome} (Vida: {jogador.vida}) vs {inimigo.nome} (Vida: {inimigo.vida})")
        acao = input("Escolha sua ação: [1] Atacar [2] Defender [3] Fugir: ")

        if acao == "1":
            dano = jogador.atacar(inimigo)
            inimigo.receber_dano(dano)
            print(f"Você atacou {inimigo.nome} e causou {dano} de dano.")
        elif acao == "2":
            print("Você se defendeu.")
            jogador.defesa += 2  # Aumenta a defesa temporariamente
        elif acao == "3":
            print("Você fugiu da batalha!")
            break
        else:
            print("Ação inválida!")

        if inimigo.vida > 0:
            dano = inimigo.atacar(jogador)
            jogador.receber_dano(dano)
            print(f"{inimigo.nome} atacou você e causou {dano} de dano.")
        
        if acao == "2":
            jogador.defesa -= 2  # Remove o bônus de defesa após o turno

    if jogador.vida <= 0:
        print("Você foi derrotado!")
    elif inimigo.vida <= 0:
        print(f"Você derrotou {inimigo.nome}!")
        jogador.ganhar_experiencia(inimigo.recompensa_experiencia)
        print(f"Você ganhou {inimigo.recompensa_experiencia} de experiência.")