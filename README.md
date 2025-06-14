# Bot de Tormenta 20 para Telegram

Este é um bot para Telegram que fornece informações sobre o RPG Tormenta 20, incluindo magias, regras e poderes.

## Funcionalidades

- Menu inicial com várias opções
- Busca de magias por nome
- Listagem de todas as magias (com nível e detalhes)
- Busca rápida de regras
- Busca de poderes (de classe, raça, origem e da tormenta)

## Requisitos

- Python 3.7 ou superior
- Biblioteca python-telegram-bot (v20.0 ou superior)

## Instalação

1. Clone este repositório:
```
git clone <url-do-repositorio>
cd <nome-da-pasta>
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```
python -m venv .venv
```

3. Ative o ambiente virtual:
   - Windows:
   ```
   .venv\Scripts\activate
   ```
   - Linux/Mac:
   ```
   source .venv/bin/activate
   ```

4. Instale as dependências:
```
pip install -r requirements.txt
```

## Configuração

O token do bot já está configurado no arquivo `main.py`. Se você quiser usar seu próprio bot, substitua o token existente pelo seu.

## Executando o Bot

Para iniciar o bot, execute:
```
python main.py
```

O bot ficará online e responderá às mensagens no Telegram.

## Estrutura de Dados

O bot está configurado para criar as seguintes pastas para armazenar dados:
- `data/spells`: Para informações sobre magias
- `data/rules`: Para informações sobre regras
- `data/powers`: Para informações sobre poderes

Atualmente, o bot usa dados de exemplo. Para uma implementação completa, você pode adicionar arquivos JSON com os dados reais de Tormenta 20 nestas pastas.

## Personalização

Você pode expandir este bot adicionando mais dados e funcionalidades:

1. Adicione mais magias no dicionário `spell_details` na função `show_spell_details`
2. Implemente a busca de regras na função `handle_message` para o estado `searching_rules`
3. Implemente a busca de poderes na função `handle_message` para os estados `searching_powers_*`

## Licença

Este projeto é apenas para uso pessoal e educacional. Tormenta 20 é propriedade intelectual da Jambô Editora.#   T o r m e n t a _ B o t _ P y t h o n  
 