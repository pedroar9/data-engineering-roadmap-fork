import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
print("Exercício 1 - De soma de dois números inteiros")

numero_1 = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite outro número inteiro: "))
resultado = numero_1 + numero_2

print(f"A soma de {numero_1} + {numero_2} é: {resultado}")
print("\n")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print("Exercício 2 - Resto da divisão por 5")

numero_1 = int(input("Digite um número inteiro: "))
resultado = numero_1 // 5

print(f"O resto da divisão de {numero_1} por 5 é: {resultado}")
print("\n")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print("Exercício 3 - Multiplicação de dois números inteiros")

numero_1 = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite outro número inteiro: "))
resultado = numero_1 * numero_2

print(f"A multiplicação de {numero_1} * {numero_2} é: {resultado}")
print("\n")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print("Exercício 4 - Divisão inteira de dois números inteiros")

numero_1 = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite outro número inteiro: "))
resultado = numero_1 // numero_2

print(f"A divisão inteira de {numero_1} por {numero_2} é: {resultado}")
print("\n")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
print("Exercício 5 - Quadrado de um número inteiro")

numero_1 = int(input("Digite um número inteiro: "))
resultado = numero_1 ** 2   

print(f"O quadrado de {numero_1} é: {resultado}")   
print("\n")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
print("Exercício 6 - Soma de dois números flutuantes")

numero_1 = float(input("Digite um número flutuante: "))
numero_2 = float(input("Digite outro número flutuante: "))
resultado = numero_1 + numero_2

print(f"A soma de {numero_1} + {numero_2} é: {resultado}")
print("\n")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print("Exercício 7 - Média de dois números flutuantes")

numero_1 = float(input("Digite um número flutuante: "))
numero_2 = float(input("Digite outro número flutuante: "))
resultado = (numero_1 + numero_2) / 2

print(f"A média de {numero_1} e {numero_2} é: {resultado}")
print("\n")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
print("Exercício 8 - Potência de um número")

numero_1 = int(input("Digite a base da potência: "))
numero_2 = int(input("Digite o expoente da potência: "))  
resultado = numero_1 ** numero_2

print(f"{numero_1} elevado a {numero_2} é: {resultado}")
print("\n")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
print("Exercício 9 - Conversão de temperatura de Celsius para Fahrenheit")

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C é equivalente a {fahrenheit}°F")
print("\n")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
print("Exercício 10 - Área de um círculo")

raio = float(input("Digite o raio do círculo: "))
area = math.pi * (raio ** 2)

print(f"A área do círculo de raio {raio} é: {area}")
print("\n")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
print("Exercício 11 - Conversão de string para maiúsculas")

string = input("Digite qualquer palavra: ")
string = string.upper() 

print(f"A string em maiúsculas é: {string}")
print("\n")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
print("Exercício 12 - Conversão de string para minúsculas")

nome_completo = input("Digite seu nome completo: ")
nome_completo = nome_completo.lower()

print(f"Seu nome em minúsculas é: {nome_completo}")
print("\n")


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
print("Exercício 13 - Remoção de espaços em branco")
frase = input("Digite uma frase: ")
frase = frase.strip()

print(f"A frase sem espaços em branco no início e no final é: {frase}")
print("\n")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
print("Exercício 14 - Separação de data")

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")

print(f"Dia: {dia}\nMês: {mes}\nAno: {ano}")
print("\n")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
print("Exercício 15 - Concatenação de strings")

string_1 = input("Digite a primeira string: ")
string_2 = input("Digite a segunda string: ")   
resultado = string_1 + string_2

print(f"A concatenação das strings é: {resultado}")
print("\n")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
print("Exercício 16 - Operação AND")

expressao_1 = bool(input("Digite a primeira expressão booleana: Ex: True ou False "))
expressao_2 = bool(input("Digite a segunda expressão booleana: Ex: True ou False "))
resultado = expressao_1 and expressao_2
print(f"O resultado da operação AND é: {resultado}")
print("\n")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
print("Exercício 17 - Operação OR")

expressao_1 = bool(input("Digite a primeira expressão booleana: Ex: True ou False "))
expressao_2 = bool(input("Digite a segunda expressão booleana: Ex: True ou False "))
resultado = expressao_1 or expressao_2

print(f"O resultado da operação OR é: {resultado}")
print("\n") 

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
print("Exercício 18 - Inversão de valor booleano")
expressao_1 = bool(input("Digite uma expressão booleana: Ex: True ou False "))
resultado = not expressao_1

print(f"O valor booleano invertido é: {resultado}")
print("\n")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
print("Exercício 19 - Comparação de dois números")

numero_1 = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite outro número inteiro: "))
resultado = numero_1 == numero_2

print(f"Os números {numero_1} e {numero_2} são iguais? {resultado}")
print("\n")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print("Exercício 20 - Verificação de diferença entre dois números")
numero_1 = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite outro número inteiro: "))
resultado = numero_1 != numero_2

print(f"Os números {numero_1} e {numero_2} são diferentes? {resultado}")
print("\n")

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

