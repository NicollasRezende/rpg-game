import json

def carregar_mapa(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        mapa = json.load(arquivo)
    return mapa

def explorar_area(jogador, mapa):
    print("Você está em:", mapa["nome"])
    print("Descrição:", mapa["descricao"])
    print("Saídas:", ", ".join(mapa["saidas"].keys()))

    while True:
        acao = input("Escolha uma direção para explorar ou 'sair' para encerrar: ")
        if acao in mapa["saidas"]:
            nova_area = mapa["saidas"][acao]
            explorar_area(jogador, nova_area)
        elif acao == "sair":
            break
        else:
            print("Direção inválida!")