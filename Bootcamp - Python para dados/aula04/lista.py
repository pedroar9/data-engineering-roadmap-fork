# Criando uma lista de produtos
produto: str = "tênis"
produto2: str = "camiseta"
produto3: str = "calça"
produto4: str = "jaqueta"
produto5: str = "boné"
produto6: str = "meia"
produto7: str = "bermuda"

# Criando uma lista de produtos
lista_de_produtos: list = []

# Adicionando produtos à lista "lista_de_produtos"
lista_de_produtos.append(produto)
lista_de_produtos.append(produto2)
lista_de_produtos.append(produto3)
lista_de_produtos.append(produto4)
lista_de_produtos.append(produto5)
lista_de_produtos.append(produto6)
lista_de_produtos.append(produto7)

# Ordenando a lista de produtos
lista_de_produtos.sort()

# Invertendo a lista de produtos
lista_de_produtos.reverse()

# removendo um produto da lista
lista_de_produtos.remove(produto)  # Removendo o produto "tênis" da lista

# Adicionando o produto "tênis" na primeira posição da lista
lista_de_produtos.insert(0, produto)

# Removendo o último produto da lista
lista_de_produtos.pop()

print(lista_de_produtos)
