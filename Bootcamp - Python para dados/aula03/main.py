# x = 2

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')
    
###
    
# lista_nome = ['João', 'Maria', 'José', 'Pedro', 'Ana', 'Paulo', 'Carlos', 'Lucas', 'Marta']

# for nome in lista_nome:
#     print(nome)
    
#####  

texto = "Python para análise de dados. Dados são o novo petróleo. A análise de dados é o novo petróleo. Python é a linguagem mais popular para análise de dados. Python é a linguagem mais popular para análise de dados."
novo_texto = texto.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '').replace('(', '').replace(')', '').replace('"', '').replace("'", '').lower()
palavras = novo_texto.split()
print(palavras)

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)

######