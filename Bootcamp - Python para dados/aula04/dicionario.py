
import json

# lista: list = ["sapato", 39, 100.00, 50, True]

produto_01: dict = {
    "nome": "sapato",
    "preco": 100.00,
    "quantidade": 10,
    "disponivel": True
}

produto_02: dict = {
    "nome": "camiseta",
    "preco": 50.00,
    "quantidade": 0,
    "disponivel": False
}
produto_03: dict = {
    "nome": "calça",
    "preco": 80.00,
    "quantidade": 5,
    "disponivel": True
}
produto_04: dict = {
    "nome": "jaqueta",
    "preco": 150.00,
    "quantidade": 2,
    "disponivel": True
}
produto_05: dict = {
    "nome": "boné",
    "preco": 30.00,
    "quantidade": 20,
    "disponivel": True
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)
carrinho.append(produto_03)
carrinho.append(produto_04)
carrinho.append(produto_05)

# convertendo o dicionário em JSON
# O parâmetro indent serve para formatar a saída JSON
# O parâmetro ensure_ascii=False serve para não converter os caracteres especiais
# para unicode
carrinho_json = json.dumps(carrinho, indent=4, ensure_ascii=False)
print(carrinho_json)
