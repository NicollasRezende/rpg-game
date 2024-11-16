from models.player import Player
from models.enemy import Enemy
from models.item import Item
from game.battle import iniciar_combate
from game.inventory import mostrar_inventario, adicionar_item, usar_item
from game.map import carregar_mapa, explorar_area
from game.quests import Missao, adicionar_missao, verificar_missoes

def main():
    print("Bem-vindo ao RPG em Python!")
    
    opcao = input("Escolha uma opção: [1] Novo Jogo [2] Carregar Jogo: ")
    if opcao == "1":
        # Criar jogador e inimigo para teste
        jogador = Player(nome="Herói", classe="Guerreiro", forca=10, defesa=5, vida=30, agilidade=3)
    elif opcao == "2":
        from utils import carregar_jogo
        jogador = carregar_jogo('savegame.json')
    else:
        print("Opção inválida!")
        return

    inimigo = Enemy(nome="Goblin", forca=6, defesa=2, vida=20, agilidade=2, dificuldade=1, recompensa_experiencia=10, itens_drop=[])

    # Adicionar item ao inventário
    pocao = Item(nome="Poção de Cura", tipo="poção", efeito="cura")
    adicionar_item(jogador, pocao)
    
    # Mostrar inventário
    mostrar_inventario(jogador)
    
    # Usar item
    usar_item(jogador, "Poção de Cura")
    
    # Iniciar combate
    iniciar_combate(jogador, inimigo)
    
    # Carregar e explorar mapa
    mapa = carregar_mapa('rpg_game\data\map.json')
    explorar_area(jogador, mapa)
    
    # Adicionar e verificar missões
    def objetivo_matar_goblin(jogador):
        return jogador.experiencia >= 10

    def recompensa_matar_goblin(jogador):
        jogador.ganhar_experiencia(20)
        print("Você ganhou 20 de experiência como recompensa!")

    missao_matar_goblin = Missao(
        nome="Matar Goblin",
        descricao="Derrote um Goblin para ganhar experiência.",
        objetivo=objetivo_matar_goblin,
        recompensa=recompensa_matar_goblin
    )

    adicionar_missao(jogador, missao_matar_goblin)
    verificar_missoes(jogador)

    # Salvar jogo
    from utils import salvar_jogo
    salvar_jogo(jogador, 'savegame.json')

if __name__ == "__main__":
    main()