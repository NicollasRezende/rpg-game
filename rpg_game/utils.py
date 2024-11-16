import json
from models.player import Player
from models.item import Item
from game.quests import Missao

def salvar_jogo(jogador, caminho_arquivo):
    dados_jogo = {
        "jogador": {
            "nome": jogador.nome,
            "classe": jogador.classe,
            "forca": jogador.forca,
            "defesa": jogador.defesa,
            "vida": jogador.vida,
            "agilidade": jogador.agilidade,
            "nivel": jogador.nivel,
            "experiencia": jogador.experiencia,
            "inventario": [{"nome": item.nome, "tipo": item.tipo, "efeito": item.efeito} for item in jogador.inventario],
            "missoes": [{"nome": missao.nome, "descricao": missao.descricao, "completa": missao.completa} for missao in jogador.missoes]
        }
    }
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(dados_jogo, arquivo)
    print("Jogo salvo com sucesso!")

def carregar_jogo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados_jogo = json.load(arquivo)
    
    jogador_dados = dados_jogo["jogador"]
    jogador = Player(
        nome=jogador_dados["nome"],
        classe=jogador_dados["classe"],
        forca=jogador_dados["forca"],
        defesa=jogador_dados["defesa"],
        vida=jogador_dados["vida"],
        agilidade=jogador_dados["agilidade"]
    )
    jogador.nivel = jogador_dados["nivel"]
    jogador.experiencia = jogador_dados["experiencia"]
    jogador.inventario = [Item(nome=item["nome"], tipo=item["tipo"], efeito=item["efeito"]) for item in jogador_dados["inventario"]]
    jogador.missoes = [Missao(nome=missao["nome"], descricao=missao["descricao"], objetivo=None, recompensa=None) for missao in jogador_dados["missoes"]]
    
    print("Jogo carregado com sucesso!")
    return jogador