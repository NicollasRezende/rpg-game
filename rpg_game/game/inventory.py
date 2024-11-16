def mostrar_inventario(jogador):
    print("\nInventário:")
    for item in jogador.inventario:
        print(f"- {item.nome} ({item.tipo})")

def adicionar_item(jogador, item):
    jogador.inventario.append(item)
    print(f"Você obteve um {item.nome}!")

def usar_item(jogador, item_nome):
    for item in jogador.inventario:
        if item.nome == item_nome:
            item.usar(jogador)  # Passar o jogador como alvo
            jogador.inventario.remove(item)
            print(f"Você usou um {item.nome}.")
            return
    print("Item não encontrado no inventário.")