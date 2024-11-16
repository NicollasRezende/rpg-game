# RPG em Python

## Descrição

Um jogo de RPG por texto desenvolvido em Python, com sistemas de combate, inventário, missões e exploração de mapas.

## Estrutura do Projeto

```
rpg_game/
├── models/
│   ├── character.py  # Classe base para personagens
│   ├── player.py     # Classe do jogador
│   ├── enemy.py      # Classe dos inimigos
│   └── item.py       # Sistema de itens
├── game/
│   ├── battle.py     # Sistema de combate
│   ├── inventory.py  # Gerenciamento de inventário
│   ├── map.py        # Sistema de exploração
│   └── quests.py     # Sistema de missões
├── data/
│   └── map.json      # Dados do mapa do jogo
├── utils.py          # Utilitários (save/load)
└── main.py          # Arquivo principal
```

## Funcionalidades

### Sistema de Personagens

-   **Jogador**

    -   Atributos: força, defesa, vida, agilidade
    -   Sistema de níveis e experiência
    -   Inventário personalizado
    -   Gerenciamento de missões

-   **Inimigos**
    -   Diferentes tipos e dificuldades
    -   Sistema de recompensas
    -   Drops de itens

### Sistema de Combate

-   Combate por turnos
-   Ações: Atacar, Defender, Usar Item, Fugir
-   Cálculo de dano baseado em atributos
-   Sistema de defesa temporária

### Sistema de Inventário

-   Adição/Remoção de itens
-   Uso de itens durante combate
-   Diferentes tipos de itens:
    -   Poções de cura
    -   Itens de buff temporário
    -   Equipamentos

### Sistema de Missões

-   Objetivos personalizáveis
-   Sistema de recompensas
-   Tracking de progresso
-   Missões completáveis

### Sistema de Mapas

-   Exploração livre
-   Múltiplas áreas
-   Navegação entre locais
-   Descrições detalhadas

### Sistema de Save/Load

-   Salvamento do progresso
-   Carregamento de jogos salvos
-   Persistência de dados em JSON

## Como Jogar

1. Execute o arquivo `main.py`
2. Escolha entre:
    - Novo Jogo
    - Carregar Jogo

### Comandos Básicos

-   Use números para selecionar opções nos menus
-   Durante exploração, digite direções (norte, sul, etc)
-   No combate, selecione ações numéricas (1-4)

## Requisitos

-   Python 3.6+
-   Bibliotecas padrão Python (json)

## Instalação

```bash
git clone [url-do-repositório]
cd rpg_game
python main.py
```

## Futuras Implementações

-   [ ] Sistema de classes com habilidades únicas
-   [ ] Mais variedade de itens e equipamentos
-   [ ] Sistema de comerciantes/lojas
-   [ ] Dungeons aleatórias
-   [ ] Sistema de crafting
-   [ ] Efeitos de status
-   [ ] Sistema de clima
-   [ ] Missões em cadeia
-   [ ] Sistema de reputação

## Autores

-   Nikz
